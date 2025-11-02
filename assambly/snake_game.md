
## Quick overview (what actually happens)

* A Wayland compositor (Hyprland) normally **owns** the DRM device (`/dev/dri/card0`) as **DRM master** and controls the display mode/CRTCs.
* To use DRM/KMS yourself you must become DRM master (or otherwise have the kernel allow you to modeset on that VT/seat). That normally only happens when:

  * the compositor is **not** running on that seat and
  * you switch to a text virtual terminal (VT) that is not under the compositor, or you run on a different *seat* (advanced).
* Practically: **switch to a VT and make sure Hyprland is not holding the DRM device**, then your program can open `/dev/dri/card0` and perform KMS ioctls to set a mode, create buffers, and page-flip.

---

## Practical safety checklist (do this every time)

1. **Switch to a clean VT** before trying to take DRM master:

   * Press `Ctrl+Alt+F3` (or `chvt 3` from a shell) to go to tty3 and log in.
2. **Stop / exit Hyprland first** (if it still owns the DRM device):

   * Log out of the Wayland session (preferred) or from another VT kill the compositor process. *Do not* try to modeset while Hyprland holds the device.
3. **Prefer to run as your user (not root)** if possible — the device node permissions matter (users in `video` group may access `/dev/dri/card0`). If you can’t open the device as your user, you can run as root for testing, but be careful.
4. **Always restore the previous KMS state on exit**:

   * Save the old mode, CRTC, and framebuffer, and restore them on normal exit and on signals (SIGINT, SIGTERM). Otherwise your display may remain blank or stuck at an unexpected mode.
5. **Test on a spare machine or VM first** if possible — mistakes can make your display go black until you reboot.
6. **Handle VT switches & signals**: implement handlers to gracefully release DRM master and restore on `SIGINT`, `SIGTERM`, `SIGSEGV`, and on VT release events.
7. **Use dumb buffers for simplicity** (no GPU acceleration needed). Later you can use GBM/EGL for hardware acceleration.

---

## The minimal DRM/KMS flow you must implement in assembly

(These are the ioctls / syscalls and the order you’ll need to call.)

1. `open("/dev/dri/card0", O_RDWR | O_CLOEXEC)`
2. `ioctl DRM_IOCTL_MODE_GETRESOURCES` — get connectors, CRTCs, encoders (or use `drmModeGetResources` semantics)
3. `ioctl DRM_IOCTL_MODE_GETCONNECTOR` — find a connected connector and supported modes
4. (optionally) `ioctl DRM_IOCTL_MODE_GETENCODER` — find encoder/CRTC pairing
5. **Create a dumb buffer**

   * `DRM_IOCTL_MODE_CREATE_DUMB` → returns handle, pitch, size
6. `mmap(NULL, size, PROT_READ|PROT_WRITE, MAP_SHARED, fd, offset_from_MAP)`

   * (use `DRM_IOCTL_MODE_MAP_DUMB` to get offset for mmap)
7. `drmModeAddFB` / `DRM_IOCTL_MODE_ADDFB` (or `DRM_IOCTL_MODE_ADDFB2`) — get a framebuffer id from the handle
8. **Set mode / CRTC**

   * `DRM_IOCTL_MODE_SETCRTC` (legacy) or preferred: **DRM Atomic API** (`DRM_IOCTL_MODE_ATOMIC`) — set the CRTC to use your framebuffer & mode
9. Draw into the mmap() area (fill pixels)
10. Present:

    * `DRM_IOCTL_MODE_PAGE_FLIP` or DRM atomic commit with pageflip (preferred atomic commit). Wait for vsync/event.
11. On exit (or VT switch): restore previous CRTC/framebuffer, `drmModeRmFB` (or `DRM_IOCTL_MODE_RMFB`), `DRM_IOCTL_MODE_DESTROY_DUMB`, `munmap`, `close`.

---

## Input handling (keyboard/mouse) — how to get controls

* Read directly from `/dev/input/event*` (evdev) (open, read `struct input_event`). You’ll need to find the correct event device for keyboard/mouse (e.g. `grep -l keyboard /proc/bus/input/devices`), or scan for devices with `EV_KEY`.
* Optionally use libinput protocol — but raw evdev is simpler to implement in pure asm.

---

## API choices — which to use (recommended order)

* **Use DRM atomic API** (preferred): safer, avoids tearing, and is the modern kernel path. But atomic ioctls require constructing big attribute blobs (more work).
* **Legacy mode-set ioctls** (`SETCRTC`, `PAGE_FLIP`) are easier to prototype but less robust.
* **Use dumb buffers first** — easier than GBM/DRM buffers or EGL.
* **Avoid direct GPU commands / GEM complexity** for initial project.

---

## Permissions & seats

* If Hyprland is running on the same seat, it holds DRM master. You must ensure the compositor releases the DRM device (by logging out or switching to a different seat).
* If you want to avoid killing Hyprland, you could create a separate seat and have your program run on that seat — but that’s advanced (systemd-logind integration) and not necessary for a one-off test.

---

## Common pitfalls & how to avoid them

* **Screen stays blank after exit** — you didn’t restore the old CRTC/framebuffer. ALWAYS save and restore.
* **“Device or resource busy” opening `/dev/dri/card0`** — Hyprland still owns DRM master; exit compositor or switch seat/VT.
* **Permission denied** — check `/dev/dri/*` group ownership; add your user to `video` or run as root for testing.
* **VT switching while you own DRM** — you must handle VT release/grab ioctls (VT_ACTIVATE/VT_WAITACTIVE or handle `KMS` and master release) so compositor can come back. Many compositors expect to regain modes at resume — be careful.
* **Not listening for page-flip events** — you might overwrite a buffer while the scanout is using it. Use page-flip callbacks or double-buffer.

---

## Minimal safe test plan (step-by-step)

1. Save & close any important work.
2. Switch to VT3: `Ctrl+Alt+F3` (or `chvt 3`). Log in as your normal user.
3. Stop/exit Hyprland from its session or ensure it’s not running on the same seat.
4. Make sure you can open DRM device:

   ```bash
   ls -l /dev/dri/card0
   groups   # check if you are in video group
   ```

   If not, run test as `sudo` for the first run.
5. Run a small test program that:

   * opens card0, queries resources,
   * picks a connector and mode,
   * creates dumb buffer, mmap, paints solid color,
   * sets CRTC to the framebuffer,
   * waits 5 seconds,
   * restores previous CRTC and exits.
6. If screen is restored after exit you’re good. If not, switch back to VT1/VT2 where your compositor was and log in/restart it.

---

## Do you really need to write a compositor?

* **No** — you don’t need to write a full compositor just to run Snake using DRM/KMS. You only need to **take modesetting control of the device** (be DRM master on a VT) and present buffers. A compositor is a continuous program that manages multiple clients, windows, input composition, etc. For a single full-screen Snake, you only need a small "display server" like program that sets a KMS mode and draws frames — far smaller than a full compositor.
* If your end-goal is to replace Hyprland or support multiple windows, then yes you would implement compositor features (buffers from clients, compositing, layering). But for a single full-screen game you do not need that complexity.

---

## Would I recommend this for your first pure-ASM project?

* It’s an **excellent low-level learning project**, but it’s also **ambitious**:

  * The DRM ioctl structs and constants are fairly involved (you’ll need to encode C structs and ioctl numbers).
  * You must carefully manage resources and error handling in assembly.
* **Recommendation**: do it — but in two stages:

  1. Implement a simple DRM “present a colored framebuffer” program in assembly first (create dumb buffer → set CRTC → present → restore). Confirm you can safely set and restore modes.
  2. Add evdev keyboard handling and the snake game loop drawing into the buffer, double-buffering and pageflip.
* I can scaffold stage (1) entirely in NASM for you (complete code + exact ioctl constants, struct byte layouts and build commands). After that we’ll extend to input & game logic.

---
