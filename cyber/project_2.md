# Cybersecurity Internship — Short Report: Basic Anonymity Workflow on Kali Linux

**Author:** Yuvraj Mahilange

**Date:** 2025-10-30

---

## 1. Scope

This report covers:

* Installing and configuring `tor` and `proxychains4`.
* Basic usage examples of `proxychains4` with applications.
* Installing and using `macchanger` to randomize or set a specific MAC address.
* How to revert MAC changes.
* Quick verification steps.

---

## 2. Environment

* OS: Kali Linux (Debian-based)
* Tools used: `tor`, `proxychains4`, `macchanger`, `ip` / `ifconfig`, `nmcli` (if NetworkManager used)
* Privileges: `sudo` required for install and network interface changes

---

## 3. Tools & Installation

### 4.1 Install `proxychains4` and `tor`

```bash
sudo apt update
sudo apt install -y proxychains4 tor
```

### 4.2 Install `macchanger`

```bash
sudo apt update
sudo apt install -y macchanger
```

---

## 4. Configure proxychains to use Tor

Open the proxychains configuration file and ensure Tor (local SOCKS) is configured as an endpoint:

```bash
sudo nano /etc/proxychains4.conf
```

Near the bottom of the file, set the chaining behavior and add a SOCKS5 line that points to the local Tor proxy (default port 9050):

```text
# use dynamic_chain or strict_chain depending on your preference
# dynamic_chain
# or strict_chain
socks5  127.0.0.1 9050
```

Save the file. Ensure Tor is running:

```bash
sudo systemctl enable --now tor
ss -ltnp | grep 9050
```

---

## 5. Using `proxychains4`

Run commands through `proxychains4` to force them through the configured chain (Tor in this example):

```bash
proxychains4 curl https://check.torproject.org
proxychains4 firefox
```


## 6. MAC address management with `macchanger`

> Always bring the interface down before changing the MAC address and back up afterwards.

### 6.1 Check interface name

```bash
ip link
# or
ifconfig -a
```

### 6.2 Temporarily change MAC (random)

```bash
sudo ip link set dev wlan0 down
sudo macchanger -r wlan0
sudo ip link set dev wlan0 up
ip link show wlan0
```

### 6.3 Set a specific MAC

```bash
sudo ip link set dev wlan0 down
sudo macchanger --mac=12:34:56:78:9A:BC wlan0
sudo ip link set dev wlan0 up
ip link show wlan0
```

### 6.4 Revert to original hardware MAC

```bash
sudo ip link set dev wlan0 down
sudo macchanger -p wlan0
sudo ip link set dev wlan0 up
ip link show wlan0
```

### 6.5 NetworkManager interaction

If NetworkManager is active it may override manual `macchanger` changes. Use `nmcli` to set a cloned MAC on a connection or edit `/etc/NetworkManager/NetworkManager.conf` to enable randomization. Example `nmcli` commands:

```bash
nmcli connection show
sudo nmcli connection modify "WIFI-CON-NAME" 802-3-ethernet.cloned-mac-address random
sudo nmcli connection down "WIFI-CON-NAME"
sudo nmcli connection up "WIFI-CON-NAME"
```

Or globally enable MAC randomization in `/etc/NetworkManager/NetworkManager.conf`:

```ini
[device]
wifi.scan-rand-mac-address=yes

[connection]
wifi.cloned-mac-address=random
```

Then restart NetworkManager:

```bash
sudo systemctl restart NetworkManager
```

---

## 7. Verification & Quick Checks

* Verify external IP (when using proxy/VPN):

```bash
curl ifconfig.me
```

* Confirm Tor usage with `proxychains4`:

```bash
proxychains4 curl https://check.torproject.org
```

* Confirm MAC address (before/after):

```bash
cat /sys/class/net/wlan0/address
ip link show wlan0
```

---

