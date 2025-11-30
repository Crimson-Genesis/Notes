# 🟦 **FTP = File Transfer Protocol**

FTP’s purpose is simple:

### ✔️ upload files

### ✔️ download files

### ✔️ list directories

### ✔️ delete/rename/manage files

It is NOT designed for websites or browsers.

---

# 🔥 **BIG IDEA: FTP uses *two* connections**

This is the most important part.

### **1️⃣ Control connection (command channel)**

Port **21** ← always

Used for sending:

* USER
* PASS
* LIST
* RETR (download)
* STOR (upload)

### **2️⃣ Data connection (data channel)**

Port **20** or a **random port**
Used for:

* actual file data
* directory listing contents

Because of this **two-channel design**, FTP is tricky with firewalls.

---

# 🟩 **FTP Operating Modes**

FTP works in **two modes**:

## 🟢 Mode 1 — Active FTP

* Client opens port X
* Client sends: “open port X for data”
* Server connects back to client on that port

Problem:
Clients behind NAT/firewalls usually block incoming connections.

---

## 🟢 Mode 2 — Passive FTP (PASV)

This is the modern one.

* Client sends command: `PASV`
* Server replies with:
  “OK, I opened port 52012 for data”
* Client connects to server’s port 52012

Works better behind firewalls and NAT.

---

# 🟦 **FULL FTP EXCHANGE (with commands)**

Let’s say client connects:

```
ftp 19.60.89.40
```

## 🟢 **1. TCP connection to port 21**

Control channel opens.

Server says:

```
220 FTP Server Ready
```

---

## 🟢 **2. Login**

Client sends:

```
USER yuvraj
```

Server:

```
331 Password required
```

Client:

```
PASS mypassword
```

Server:

```
230 Login successful
```

⚠️ ALL OF THIS IS PLAIN TEXT
FTP does not encrypt anything.

---

## 🟢 **3. Set mode (Active or Passive)**

Client sends:

```
PASV
```

Server replies:

```
227 Entering Passive Mode (19,60,89,40,203,12)
```

This means:

```
Port = 203*256 + 12 = 52012
```

Client will open data connection to **19.60.89.40:52012**

---

## 🟢 **4. List directory**

Client sends over control channel:

```
LIST
```

Server sends directory listing over **data connection**:

```
-rw-r--r-- 1 root root 1042 index.html
-rw-r--r-- 1 root root 3872 style.css
drwxr-xr-x 1 root root 4096 images
```

After sending data, server closes data connection.

---

## 🟢 **5. Download a file** (RETR)

Client:

```
RETR index.html
```

Server:

* Opens new data channel
* Sends file contents
* Closes data channel

---

## 🟢 **6. Upload a file** (STOR)

Client:

```
STOR newfile.txt
```

Client then sends file data through the data connection.

---

## 🟢 **7. Quit**

Client:

```
QUIT
```

Server:

```
221 Goodbye
```

---

# 🟥 **Diagram: FTP Workflow**

```
Client                                 Server
──────────────────────────────────────────────────────────────

TCP CONNECT to port 21  ─────────────▶  (Control channel)

USER username           ─────────────▶
PASS password           ─────────────▶

PASV                    ─────────────▶
                       ◀────────────  227 Entering Passive Mode (ip,port)

TCP CONNECT to port N   ─────────────▶ (Data channel)

LIST                    ─────────────▶
                       ◀────────────  directory listing (data channel)

RETR filename           ─────────────▶
                       ◀────────────  file data (data channel)

QUIT                    ─────────────▶
                       ◀────────────  221 Goodbye
```

---

# 🟧 **Why FTP uses 2 channels**

Because when FTP was invented in 1971:

* networks were simple
* splitting commands and data was considered elegant
* allowed pipes, batch transfers, etc.

Today it causes:

* firewall problems
* NAT problems
* complexity

That’s why HTTP won for web, and SFTP won for secure file transfers.

---

# 🟦 **Modern replacements for FTP**

### ✔️ SFTP (SSH File Transfer Protocol)

Totally different from FTP.
Uses **1 connection** on port **22**.
Encrypted.
Most popular replacement.

### ✔️ FTPS (FTP + TLS)

FTP but encrypted.

### ✔️ HTTP/HTTPS file upload/download

Web browsers use this.

### ✔️ Cloud storage

(S3, Google Cloud Storage, Dropbox)

---

# 🟥 **FINAL SUMMARY**

### ✔️ FTP = old file transfer protocol

### ✔️ Uses 2 connections:

* Port 21 for commands
* Random port for data

### ✔️ Sends USER/PASS in plain text (insecure)

### ✔️ Browser does NOT use FTP

### ✔️ Still used in legacy systems, IoT, factories

### ✔️ Modern secure replacement = SFTP (SSH)

---
