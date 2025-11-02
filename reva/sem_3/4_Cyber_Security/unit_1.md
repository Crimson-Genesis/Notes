# Unit - 1

## Overview of Cyber Security
- Introduction
- Cyber Security increasing threat landscape
- Cyber Security terminologies - Cyberspace, attack, attack vector, attack surface, threat, risk, vulnerability, exploit, exploitation, hacker, Non-state actores, Cyber terrorist, Protaction of end user machine, Critical IT and National Critical Infrastucture, Cyberwarfare, Case Studies.

- Exercises:
    - Use Nmap to scan a network for live hosts and identify open ports.
    - Explore different scan types (e.g., SYN scan, UDP scan) to understand how they gather information about networked devices.
    - Use tools like hohn the Ripper or Hashcat to crack passwords from hashed files.

---
---

# 🧠 **Introduction to Cyber Security**

---

## 🔍 What Is Cyber Security?

**Cyber Security** refers to the practice of protecting **systems, networks, programs, and data** from **digital attacks**.
These attacks are usually aimed at:

* Accessing, changing, or destroying sensitive information,
* Extorting money from users (ransomware), or
* Interrupting normal business processes.

It’s a combination of **technologies, processes, and best practices** designed to **defend computing systems and networks** from cyber threats.

---

## 🌐 Why Cyber Security Matters

| Aspect                  | Description                                                                             |
| ----------------------- | --------------------------------------------------------------------------------------- |
| **Data Protection**     | Prevents unauthorized access to personal, financial, and organizational data.           |
| **Business Continuity** | Ensures critical systems remain operational even under attack.                          |
| **National Security**   | Protects critical infrastructure like power grids, defense systems, and healthcare.     |
| **Public Trust**        | Builds confidence in digital services like banking, e-commerce, and government portals. |

---

## 💥 The Growing Threat Landscape

Cyber threats are evolving faster than ever due to:

* Increased **internet-connected devices (IoT)**
* Use of **cloud computing** and **AI**
* **Remote work** expanding the attack surface
* The **dark web** facilitating cybercrime trades

🧩 **Statistics (as of recent years):**

* Every **39 seconds** a cyberattack occurs globally.
* The **average cost of a data breach** exceeds **$4 million** (IBM report).
* Over **70% of cyberattacks** target small and medium-sized businesses.

---

## 🔐 Goals of Cyber Security

Cyber Security is often summarized by the **CIA Triad**:

| Principle           | Description                                                  | Example                                     |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------- |
| **Confidentiality** | Ensuring information is only accessible to authorized users. | Encryption of user data.                    |
| **Integrity**       | Ensuring data is accurate and not tampered with.             | Using hash functions for file verification. |
| **Availability**    | Ensuring systems and data are accessible when needed.        | Redundant servers and DDoS protection.      |

---

## 🧱 Layers of Cyber Security

To protect a digital ecosystem, security is applied at multiple levels:

| Layer                    | Example Controls                              |
| ------------------------ | --------------------------------------------- |
| **Network Security**     | Firewalls, IDS/IPS, VPNs                      |
| **Application Security** | Secure coding, input validation               |
| **Endpoint Security**    | Antivirus, patch management                   |
| **Data Security**        | Encryption, data masking                      |
| **User Awareness**       | Training to avoid phishing/social engineering |
| **Operational Security** | Policies, access control, incident response   |

---

## 🧰 Example Diagram: Cyber Security Ecosystem

```
             ┌──────────────────────────────┐
             │          Internet            │
             └──────────────────────────────┘
                          │
            ┌─────────────▼─────────────┐
            │     Firewall / IDS / IPS  │
            └─────────────┬─────────────┘
                          │
            ┌─────────────▼─────────────┐
            │   Internal Network Layer  │
            │ (Servers, Databases, IoT) │
            └─────────────┬─────────────┘
                          │
           ┌──────────────▼──────────────┐
           │     Endpoint Protection     │
           │ (PCs, Laptops, Mobiles)     │
           └──────────────┬──────────────┘
                          │
            ┌─────────────▼─────────────┐
            │   Users / Admin Access    │
            └────────────────────────────┘
```

---

## ⚙️ Example: A Simple Security Practice

```bash
# Example: Enable a firewall on Linux (UFW)
sudo apt install ufw
sudo ufw enable
sudo ufw status
```

🧩 **Explanation:**
The above ensures your system only allows specific network connections — an essential first layer of protection.

---

## 🚨 Common Cyber Threats Overview

| Threat Type                  | Description                               | Example                    |
| ---------------------------- | ----------------------------------------- | -------------------------- |
| **Malware**                  | Software designed to harm systems.        | Viruses, Worms, Ransomware |
| **Phishing**                 | Deceptive messages to steal credentials.  | Fake bank emails           |
| **DDoS Attacks**             | Overloading servers to take them offline. | Botnet-based flooding      |
| **Man-in-the-Middle (MITM)** | Intercepting communication.               | Fake Wi-Fi access points   |
| **Zero-Day Exploits**        | Attacks on unpatched vulnerabilities.     | New OS flaw exploitation   |

---

## 🧩 Case Example

**WannaCry Ransomware Attack (2017):**

* Exploited a vulnerability in Windows (EternalBlue).
* Spread across 150+ countries.
* Affected hospitals, banks, and telecoms.
* Caused **billions in losses**.

🧠 *Lesson:* Always keep systems patched and perform regular backups.

---

## 🧭 Summary

| Key Idea                                                                       | Description |
| ------------------------------------------------------------------------------ | ----------- |
| Cyber Security = Protecting digital assets from unauthorized access or damage. |             |
| Evolving threat landscape → constant learning needed.                          |             |
| CIA Triad forms the foundation of security principles.                         |             |
| Security must be multi-layered and proactive.                                  |             |
| Awareness and vigilance are as vital as technology.                            |             |

---

# 🌍 **Cyber Security Increasing Threat Landscape**

---

## 🧠 What Does “Threat Landscape” Mean?

The **cyber threat landscape** refers to the **complete view of all potential and existing cyber threats** that can target individuals, organizations, or nations at any given time.

It’s not static — it **evolves constantly** as technology, user behavior, and attacker capabilities change.

> 🧩 Think of it like a battlefield: as defenders improve their walls and shields, attackers find new weapons and tactics.

---

## 📈 How the Threat Landscape Is Expanding

Over the years, the number and complexity of attacks have grown dramatically.
Here’s why 👇

| Factor                       | Explanation                                                           | Example                                        |
| ---------------------------- | --------------------------------------------------------------------- | ---------------------------------------------- |
| **Digital Transformation**   | Everything — from homes to industries — is connected to the internet. | Smart homes, IoT sensors, online banking.      |
| **Remote Work Culture**      | Employees connect from unsecured networks.                            | VPN misuse, phishing targeting remote workers. |
| **Cloud Adoption**           | Data stored on shared infrastructure.                                 | Cloud misconfiguration leading to leaks.       |
| **AI/Automation in Attacks** | Attackers use AI to automate reconnaissance and phishing.             | Deepfake-based social engineering.             |
| **Use of Darknet**           | Cybercriminals share tools, exploits, and stolen data.                | Selling credit card dumps, ransomware kits.    |
| **Supply Chain Weakness**    | Attackers compromise a third-party vendor to reach the main target.   | SolarWinds supply chain attack.                |
| **Global Connectivity**      | Borders don’t stop cybercrime.                                        | Cross-country DDoS or ransomware campaigns.    |

---

## ⚔️ Major Categories of Emerging Cyber Threats

### 1. **Ransomware Attacks**

* Encrypt user data and demand ransom to decrypt it.
* Spread via email attachments or unpatched systems.

💡 *Example:* WannaCry, Petya, LockBit

---

### 2. **Phishing and Social Engineering**

* Attackers trick users into revealing credentials or installing malware.
* Highly personalized (spear phishing) attacks using data from social media.

💡 *Example:* Fake “password reset” emails from “Google” or “Microsoft.”

---

### 3. **IoT-Based Attacks**

* IoT devices often lack strong security (no firewalls, default passwords).
* Used in large botnets like **Mirai**, which launched massive DDoS attacks.

💡 *Example:* Hacked CCTV cameras flooding a website with requests.

---

### 4. **Advanced Persistent Threats (APT)**

* Long-term, stealthy attacks by organized groups or nation-states.
* Goal: espionage, data theft, or system disruption.

💡 *Example:* Stuxnet (used against Iran’s nuclear facility).

---

### 5. **Cloud Security Threats**

* Misconfigured cloud storage and unsecured APIs are top causes.
* Attackers exploit poor access control and lack of monitoring.

💡 *Example:* Misconfigured AWS S3 bucket leaking millions of user records.

---

### 6. **Cryptojacking**

* Attackers secretly use your CPU/GPU to mine cryptocurrency.
* Causes system slowdowns and high electricity usage.

💡 *Example:* Browser-based miners running hidden JavaScript.

---

### 7. **AI-Generated Threats**

* Deepfake videos, voice impersonations, and synthetic identities.
* Used in scams, misinformation, and blackmail.

💡 *Example:* Deepfake CEO calls tricking employees to transfer money.

---

### 8. **Mobile Threats**

* Malicious apps, SMS phishing (Smishing), and mobile Trojans.
* Exploit app permissions and OS vulnerabilities.

💡 *Example:* Fake banking apps stealing login credentials.

---

### 9. **Insider Threats**

* Employees or contractors intentionally or unintentionally compromise data.
* Often harder to detect because insiders already have access.

💡 *Example:* Disgruntled employee leaking trade secrets.

---

### 10. **Critical Infrastructure Attacks**

* Targets power grids, water supply, transport, or healthcare.
* Can lead to national-level crises.

💡 *Example:* 2021 Colonial Pipeline ransomware attack in the U.S.

---

## 📊 Diagram: Expanding Cyber Threat Landscape

```
                 ┌──────────────────────┐
                 │    Nation-State APT  │
                 └──────────┬───────────┘
                            │
 ┌──────────────┬────────────┼─────────────┬──────────────┐
 │              │            │             │              │
 ▼              ▼            ▼             ▼              ▼
Ransomware   Phishing     IoT Attacks   Cloud Threats  Insider Threats
   │             │            │             │              │
   ▼             ▼            ▼             ▼              ▼
 Data Loss   Identity Theft  DDoS       Data Leakage   IP Theft
   │             │            │             │              │
   └─────────────┴────────────┴─────────────┴──────────────┘
                    🔥 Global Cyber Threats 🔥
```

---

## 🌐 Real-World Examples

| Year     | Attack                  | Description                                          | Impact                                                  |
| -------- | ----------------------- | ---------------------------------------------------- | ------------------------------------------------------- |
| **2017** | **WannaCry**            | Ransomware spreading via Windows SMB vulnerability.  | 230,000+ systems infected in 150 countries.             |
| **2020** | **SolarWinds**          | Supply chain APT attack on U.S. government networks. | 18,000 organizations compromised.                       |
| **2021** | **Colonial Pipeline**   | Ransomware on energy infrastructure.                 | Fuel shortages across U.S. East Coast.                  |
| **2022** | **Log4j Vulnerability** | Open-source logging library flaw exploited.          | Millions of systems affected globally.                  |
| **2023** | **MOVEit Data Breach**  | File transfer software exploited.                    | Sensitive data stolen from enterprises and governments. |

---

## 🧩 Impact of an Expanding Threat Landscape

| Category              | Impact                                                 |
| --------------------- | ------------------------------------------------------ |
| **Economic**          | Loss of billions in damages and recovery costs.        |
| **Reputational**      | Organizations lose customer trust and market value.    |
| **Operational**       | Downtime in services like banking or healthcare.       |
| **Legal**             | Heavy fines under data protection laws (e.g., GDPR).   |
| **National Security** | Potential disruption to power, defense, and transport. |

---

## 🛡️ How to Respond to the Growing Threat Landscape

| Strategy                        | Description                                                 |
| ------------------------------- | ----------------------------------------------------------- |
| **Zero Trust Security**         | Never trust, always verify; every request is authenticated. |
| **Regular Patching**            | Keep all systems and software up to date.                   |
| **User Awareness Training**     | Prevent phishing and social engineering attacks.            |
| **Network Segmentation**        | Isolate sensitive systems to reduce attack spread.          |
| **Threat Intelligence Sharing** | Collaborate with CERTs and security communities.            |
| **Incident Response Planning**  | Prepare and practice for cyber incidents.                   |

---

## 🧭 Summary

| Key Point                                                                    | Description |
| ---------------------------------------------------------------------------- | ----------- |
| Cyber threats are expanding due to technology, connectivity, and automation. |             |
| Attackers use AI, IoT, and supply chain vulnerabilities to gain entry.       |             |
| Ransomware, phishing, and APTs dominate the current landscape.               |             |
| A proactive, layered defense is essential.                                   |             |
| Awareness, monitoring, and rapid incident response are key to survival.      |             |

---

# 🧩 **Cyber Security Terminologies**

---

## 🌐 1. **Cyberspace**

### 📖 Definition:

**Cyberspace** refers to the **virtual environment** formed by interconnected digital devices, networks, software, and users that exchange information over the internet.

It includes:

* Computers, mobile devices, IoT devices
* Communication networks (LAN, WAN, Internet)
* Data centers, cloud infrastructure
* Online services and applications

### 💡 Example:

When you send an email, stream a video, or access a cloud app — you’re operating in **cyberspace**.

### 🧭 Visualization:

```
┌───────────────────────────────────────────────┐
│                 CYBERSPACE                    │
│  Users  ↔  Devices  ↔  Networks  ↔  Data      │
│  (Human)    (Machines)   (Internet)  (Cloud)  │
└───────────────────────────────────────────────┘
```

---

## ⚔️ 2. **Attack**

### 📖 Definition:

A **cyberattack** is a **deliberate attempt** by an individual or organization to **breach information systems** — to steal, damage, or disrupt data or services.

### 🧠 Types of Attacks:

| Type               | Description                            | Example                        |
| ------------------ | -------------------------------------- | ------------------------------ |
| **Active Attack**  | Alters or disrupts the system.         | DDoS, ransomware               |
| **Passive Attack** | Only observes or steals data silently. | Packet sniffing, eavesdropping |

---

## 🎯 3. **Attack Vector**

### 📖 Definition:

An **attack vector** is the **path or method** used by attackers to gain unauthorized access to a target system.

| Attack Vector              | Description                         | Example                              |
| -------------------------- | ----------------------------------- | ------------------------------------ |
| **Email Phishing**         | Tricking users via fake emails.     | "Your bank account is locked" email. |
| **Malware**                | Infected files or apps.             | Trojan horse, ransomware             |
| **Social Engineering**     | Manipulating human behavior.        | Fake tech-support calls              |
| **Network Exploits**       | Using open ports or weak protocols. | Exploiting SMB or Telnet             |
| **USB or Physical Access** | Using infected devices.             | Plugging a malicious USB drive       |

---

## 🧱 4. **Attack Surface**

### 📖 Definition:

An **attack surface** is the **total number of points** (digital, physical, human) where an attacker can attempt to enter or extract data.

### 🧩 Example:

If your system includes:

* Web app
* Database server
* API endpoints
* Untrained employees
  → all of these combined form your **attack surface**.

### 📊 Diagram:

```
           ┌───────────────────────────┐
           │       ATTACK SURFACE       │
           ├───────────────────────────┤
           │ • Web Applications         │
           │ • APIs                     │
           │ • Network Ports            │
           │ • Endpoints (PCs, Mobiles) │
           │ • Human Users              │
           └───────────────────────────┘
```

---

## ⚠️ 5. **Threat**

### 📖 Definition:

A **threat** is a **potential danger** that could exploit a vulnerability and cause harm.

| Threat Type          | Description                  | Example                     |
| -------------------- | ---------------------------- | --------------------------- |
| **Human Threat**     | Malicious insider or hacker. | Employee leaking data.      |
| **Technical Threat** | Software/hardware flaws.     | Unpatched OS vulnerability. |
| **Natural Threat**   | Environmental factors.       | Flood damaging servers.     |

---

## 📉 6. **Risk**

### 📖 Definition:

**Risk** is the **probability** that a threat will exploit a vulnerability and cause damage.

### ⚙️ Formula:

$$
\text{Risk} = \text{Threat} \times \text{Vulnerability} \times \text{Impact}
$$

| Component     | Example                   |
| ------------- | ------------------------- |
| Threat        | Malware                   |
| Vulnerability | Outdated antivirus        |
| Impact        | System crash or data loss |

So, if a hospital uses outdated software, the **risk** of ransomware attack is high.

---

## 🧩 7. **Vulnerability**

### 📖 Definition:

A **vulnerability** is a **weakness or flaw** in software, hardware, or human behavior that can be exploited.

| Type                       | Example                        |
| -------------------------- | ------------------------------ |
| **Software Vulnerability** | Unpatched OS, buffer overflow  |
| **Hardware Vulnerability** | Meltdown, Spectre              |
| **Human Vulnerability**    | Weak passwords, phishing click |

---

## 💣 8. **Exploit**

### 📖 Definition:

An **exploit** is a **piece of code or tool** designed to take advantage of a vulnerability.

💡 Example:
If there’s a buffer overflow vulnerability, a hacker may write an **exploit** to execute arbitrary code and gain access.

---

## 🧨 9. **Exploitation**

### 📖 Definition:

**Exploitation** is the **act of using an exploit** to attack a system and achieve a malicious objective.

🧩 Example:

* Vulnerability: Weak admin password.
* Exploit: Brute-force script.
* Exploitation: Hacker gains admin access.

---

## 🧑‍💻 10. **Hacker**

### 📖 Definition:

A **hacker** is someone who gains unauthorized access to systems or data — but not all hackers are bad.

| Type              | Description                                   | Example              |
| ----------------- | --------------------------------------------- | -------------------- |
| **White Hat**     | Ethical hacker; tests security legally.       | Penetration testers. |
| **Black Hat**     | Malicious hacker; breaks systems for profit.  | Cybercriminals.      |
| **Grey Hat**      | Explores without permission but not for harm. | Bug bounty seekers.  |
| **Script Kiddie** | Uses prebuilt tools without deep knowledge.   | Amateur hacker.      |

---

## 🌍 11. **Non-State Actors**

### 📖 Definition:

**Non-state actors** are individuals or groups **not officially connected to any government** but capable of performing cyber operations.

They can be:

* Hacktivists (e.g., Anonymous)
* Cybercriminal groups
* Terrorist organizations
* Private hacker-for-hire teams

💡 *Example:* “Lazarus Group” — a non-state actor linked to North Korea, involved in cyber espionage.

---

## 💣 12. **Cyber Terrorist**

### 📖 Definition:

A **cyber terrorist** uses digital attacks to **cause fear, disruption, or physical damage** for ideological or political reasons.

| Target                 | Example                                        |
| ---------------------- | ---------------------------------------------- |
| **Government Systems** | Attacks on defense or election infrastructure. |
| **Public Utilities**   | Disrupting power grids or transport.           |
| **Finance Systems**    | Shutting down ATMs or banks.                   |

🧩 *Example:* Attacks on Estonia (2007) — websites of government and banks were shut down after political tension.

---

## 🧍‍♂️💻 13. **Protection of End User Machine**

### 📖 Definition:

End-user protection (endpoint security) secures **user devices** — computers, laptops, phones — against threats.

### 🛡️ Protection Techniques:

| Method                                | Example                                      |
| ------------------------------------- | -------------------------------------------- |
| **Antivirus & Firewall**              | Block malicious files and traffic.           |
| **Patch Management**                  | Keep OS and software updated.                |
| **Encryption**                        | Protect data at rest and in transit.         |
| **Multi-Factor Authentication (MFA)** | Add a second layer of identity verification. |
| **User Awareness Training**           | Recognize phishing or unsafe downloads.      |

### 🧰 Example Command:

```bash
# Enable automatic updates on Linux
sudo apt update && sudo apt upgrade -y
```

---

## 🏢 14. **Critical IT and National Critical Infrastructure**

### 📖 Definition:

**Critical IT Infrastructure** refers to the **essential systems** that support the nation’s economy, security, and health.

| Sector         | Examples                                 |
| -------------- | ---------------------------------------- |
| **Energy**     | Power grids, oil pipelines               |
| **Finance**    | Banks, stock exchanges                   |
| **Healthcare** | Hospital databases, life-support systems |
| **Transport**  | Air traffic control, railways            |
| **Government** | Military, law enforcement servers        |

### ⚙️ Security Measures:

* Network segmentation
* Redundant systems
* Continuous monitoring (SIEM)
* Physical security

---

## ⚔️ 15. **Cyberwarfare**

### 📖 Definition:

**Cyberwarfare** refers to **state-sponsored attacks** on another nation’s networks or systems to disrupt, spy, or damage infrastructure.

### 🧠 Characteristics:

* Political or military motivation
* Use of advanced persistent threats (APTs)
* Targets include defense, power, and communication networks

💡 *Example:*
**Stuxnet (2010)** — A worm used (allegedly by U.S. & Israel) to damage Iran’s nuclear centrifuges.
It marked the **first known cyberweapon** to cause **physical destruction**.

---

## 📚 Case Studies

| Case                                 | Description                                                  | Impact                                                        |
| ------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------- |
| **Stuxnet (2010)**                   | Worm targeting Iran’s nuclear plant via Siemens PLCs.        | Destroyed uranium centrifuges, showed cyberwarfare potential. |
| **WannaCry (2017)**                  | Ransomware exploiting SMB vulnerability.                     | Affected 200,000+ systems globally.                           |
| **NotPetya (2017)**                  | Malware disguised as ransomware, hit Ukraine infrastructure. | $10 billion in damages worldwide.                             |
| **Estonia Cyberattack (2007)**       | DDoS attack on Estonian government and banks.                | Shut down national online services for weeks.                 |
| **Ukraine Power Grid Attack (2015)** | Attackers remotely shut down substations.                    | 230,000 citizens lost power.                                  |

---

## 🧭 Summary

| Term                        | Meaning (Short)                                      |
| --------------------------- | ---------------------------------------------------- |
| **Cyberspace**              | Global digital environment of data and devices       |
| **Attack**                  | Attempt to damage or steal information               |
| **Attack Vector**           | Pathway of attack                                    |
| **Attack Surface**          | Total number of possible entry points                |
| **Threat**                  | Potential cause of harm                              |
| **Risk**                    | Probability of a threat exploiting a vulnerability   |
| **Vulnerability**           | Weakness in system or human behavior                 |
| **Exploit / Exploitation**  | Tool and act of taking advantage of a weakness       |
| **Hacker**                  | Individual exploiting systems (ethical or unethical) |
| **Non-State Actor**         | Independent cyber group not tied to government       |
| **Cyber Terrorist**         | Uses cyberattacks for ideological violence           |
| **End User Protection**     | Securing devices via antivirus, MFA, awareness       |
| **Critical Infrastructure** | Essential systems for nation’s function              |
| **Cyberwarfare**            | State-level digital attack for military goals        |

---

# Exercises:
# 🧭 **Nmap Network Scanning — Practical Explanation**

---

## ⚙️ 1. What Is Nmap?

**Nmap (Network Mapper)** is an **open-source tool** used for **network discovery and security auditing**.
It can:

* Discover hosts and services on a network
* Detect open ports
* Identify operating systems and versions
* Perform vulnerability assessments

---

## 🧰 2. Installing Nmap

### 🐧 On Linux (Arch/Ubuntu)

```bash
# Arch Linux
sudo pacman -S nmap

# Ubuntu/Debian
sudo apt install nmap
```

### 🪟 On Windows

Download from: [https://nmap.org/download.html](https://nmap.org/download.html)

---

## 🌐 3. Basic Syntax

```bash
nmap [options] [target]
```

| Term        | Meaning                                                             |
| ----------- | ------------------------------------------------------------------- |
| **target**  | IP address, domain, or subnet (e.g., 192.168.1.1 or 192.168.1.0/24) |
| **options** | Control what Nmap does (scan type, output format, etc.)             |

---

## 🧩 4. Step 1 — Scan for Live Hosts (Ping Sweep)

Before scanning ports, you need to know **which devices are alive** on your network.

### 🧠 Command:

```bash
sudo nmap -sn 192.168.1.0/24
```

### 🧾 Explanation:

| Option           | Meaning                                                         |
| ---------------- | --------------------------------------------------------------- |
| `-sn`            | “Ping Scan” — skips port scan, only checks which hosts respond. |
| `192.168.1.0/24` | Scans all 256 IPs in that subnet.                               |

### 📊 Sample Output:

```
Starting Nmap 7.94 ( https://nmap.org ) at 2025-11-01 17:00 IST
Nmap scan report for 192.168.1.1
Host is up (0.0020s latency).
Nmap scan report for 192.168.1.5
Host is up (0.0030s latency).
Nmap done: 256 IP addresses (2 hosts up) scanned in 2.15 seconds
```

✅ **Result:**
Found 2 live hosts — `192.168.1.1` and `192.168.1.5`

---

## 🧩 5. Step 2 — Identify Open Ports on a Host

Now, let’s scan one of the live hosts (say `192.168.1.5`) to find which **ports are open**.

### ⚙️ Command:

```bash
sudo nmap 192.168.1.5
```

### 📊 Sample Output:

```
Starting Nmap 7.94 ( https://nmap.org ) at 2025-11-01 17:05 IST
Nmap scan report for 192.168.1.5
Host is up (0.0010s latency).
Not shown: 996 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
MAC Address: 00:1A:2B:3C:4D:5E (Intel)
```

✅ **Result:**
The system has **SSH, HTTP, and SMB** services running.

---

## 🧠 6. Step 3 — Advanced Scan Types

| Scan Type              | Command                              | Description                                               |
| ---------------------- | ------------------------------------ | --------------------------------------------------------- |
| **SYN Scan (Stealth)** | `sudo nmap -sS 192.168.1.5`          | Most common; sends half-open TCP connections.             |
| **UDP Scan**           | `sudo nmap -sU 192.168.1.5`          | Scans UDP services (DNS, SNMP, etc.).                     |
| **Version Detection**  | `sudo nmap -sV 192.168.1.5`          | Shows software version of each open port.                 |
| **OS Detection**       | `sudo nmap -O 192.168.1.5`           | Detects operating system type.                            |
| **Aggressive Scan**    | `sudo nmap -A 192.168.1.5`           | Combines OS detection, version detection, and traceroute. |
| **Specific Port Scan** | `sudo nmap -p 22,80,443 192.168.1.5` | Scans only selected ports.                                |

---

## 📄 7. Step 4 — Save the Scan Results

To store scan results for later analysis:

```bash
sudo nmap -A 192.168.1.5 -oN scan_report.txt
```

| Option            | Meaning                           |
| ----------------- | --------------------------------- |
| `-oN`             | Save output in normal text format |
| `scan_report.txt` | Output file name                  |

Other formats:

* `-oX` → XML format
* `-oG` → Greppable format (for scripts)

---

## 🧩 8. Step 5 — Scan an Entire Network Range

To find **all live devices and their open ports**:

```bash
sudo nmap -sS 192.168.1.0/24
```

This gives a **network map** with all reachable systems and their running services.

---

## 🔍 9. Interpreting Results

| Port      | Service    | Risk Level | Description                    |
| --------- | ---------- | ---------- | ------------------------------ |
| 21        | FTP        | ⚠️ High    | Often left unprotected         |
| 22        | SSH        | 🟡 Medium  | Secure, but brute-forced often |
| 80 / 443  | HTTP/HTTPS | 🟢 Low     | Common web services            |
| 139 / 445 | SMB        | 🔥 High    | Exploited in WannaCry          |
| 3306      | MySQL      | ⚠️ High    | Exposed database risk          |

---

## 🧱 10. Security Use Cases

| Purpose                   | Example                                      |
| ------------------------- | -------------------------------------------- |
| **Network Inventory**     | Identify all connected devices.              |
| **Vulnerability Testing** | Check for unnecessary open ports.            |
| **Incident Response**     | Find compromised hosts in an attack.         |
| **Compliance Auditing**   | Ensure only authorized services are running. |

---

## ⚠️ 11. Ethical Usage Reminder

> 🚫 Never scan external or public networks without **explicit permission** — it’s considered **illegal hacking** under cyber laws (IT Act 2000, Section 66).

✅ Only perform scans on:

* Your own systems
* Authorized lab networks
* College or training environments

---

## 📘 Example Lab Scenario Summary

| Step | Action              | Command                                     | Result                       |
| ---- | ------------------- | ------------------------------------------- | ---------------------------- |
| 1    | Scan for live hosts | `sudo nmap -sn 192.168.1.0/24`              | 2 live hosts detected        |
| 2    | Scan open ports     | `sudo nmap 192.168.1.5`                     | Ports 22, 80, 139, 445 open  |
| 3    | Version detection   | `sudo nmap -sV 192.168.1.5`                 | SSH 7.9, Apache 2.4 detected |
| 4    | Save report         | `sudo nmap -oN scan_report.txt 192.168.1.5` | Results saved for analysis   |

---

## 🧠 Summary Points

* **Nmap** = Network Mapper for host & port discovery.
* Use **`-sn`** to find live hosts, **`-sS`** or **default scan** to find open ports.
* Always scan **only authorized networks**.
* Combine with vulnerability tools like **Nessus/OpenVAS** later (Unit 2).

---

# 🔍 Nmap Scan Types — Overview & When to Use Them

| Scan              | Command           | What it does (brief)                                                   |             Root needed? |         Stealth level         | Typical use                                                          |
| ----------------- | ----------------- | ---------------------------------------------------------------------- | -----------------------: | :---------------------------: | -------------------------------------------------------------------- |
| TCP Connect       | `-sT`             | Completes full TCP handshake (connect()).                              |                No (user) |           Low (loud)          | When you don’t have raw-socket privileges (Windows, non-root Linux). |
| SYN (half-open)   | `-sS`             | Sends SYN, waits for SYN/ACK → doesn’t finish handshake (RST instead). |                Yes (raw) |      Medium (stealthier)      | Fast host discovery & stealthy port scan.                            |
| UDP               | `-sU`             | Sends UDP packets, infers state from ICMP responses or UDP replies.    |                      Yes |    Low/Medium (noisy, slow)   | Scanning DNS, SNMP, NTP, etc.                                        |
| FIN / NULL / Xmas | `-sF -sN -sX`     | Sends unusual TCP flags to evade some firewalls.                       |                      Yes | Medium-high (evade basic IDS) | Evasion & fingerprinting; unreliable against modern stacks.          |
| ACK               | `-sA`             | Sends ACK to map firewall rules (filtered vs unfiltered).              |                      Yes |              Low              | Determine if a firewall is stateful.                                 |
| Window            | `-sW`             | Uses TCP window size to guess open ports (rare).                       |                      Yes |              Low              | Legacy technique.                                                    |
| Maimon            | `-sM`             | Special flag combo for BSD TCP stacks (legacy).                        |                      Yes |              Low              | Rare/legacy.                                                         |
| Idle (IP ID)      | `-sI <zombie>`    | Uses another host to perform scan (idle scan).                         |                Yes (raw) |   Very high (very stealthy)   | Completely blind stealth scan — hides your source IP.                |
| SCTP INIT/COOKIE  | `-sY -sZ`         | Scans SCTP ports (for telecom/SS7)                                     |                      Yes |             Medium            | Telecom & specialized services.                                      |
| Ping scan         | `-sn`             | Host discovery only (no port scan)                                     |                       No |              N/A              | Find live hosts quickly.                                             |
| Version detect    | `-sV`             | Probe open ports to identify service/version                           | No (but useful with -sS) |              N/A              | Fingerprinting services (combine with -sS).                          |
| OS detection      | `-O`              | TCP/IP stack fingerprinting to infer OS                                |                      Yes |              N/A              | Determine OS (best-effort).                                          |
| Aggressive        | `-A`              | `-sS -sV -O --traceroute --script=default` composite                   |                      Yes |              Loud             | Full reconnaissance in one run.                                      |
| Script scan       | `--script <name>` | Runs NSE scripts for deeper checks                                     |        Depends on script |             Varies            | Vulnerability checks, brute-force, info-gathering.                   |

---

## 1) TCP Connect Scan (`-sT`)

**Command**

```bash
nmap -sT 192.168.1.5
```

**How it works**

* Uses OS `connect()` to complete the TCP 3-way handshake. If connection succeeds, port is `open`.
  **Pros**
* Works without root.
* Reliable.
  **Cons**
* Very noisy; easy to spot in logs/IDS.
  **When to use**
* Quick scan from unprivileged account or Windows.

---

## 2) SYN Scan (`-sS`) — “Half-open” (Most common)

**Command**

```bash
sudo nmap -sS 192.168.1.5
```

**How it works**

* Sends `SYN`. If `SYN/ACK` returned → port likely **open** (Nmap sends `RST` to avoid completing handshake). If `RST` → **closed**. If no response or ICMP unreachable → **filtered**.
  **Pros**
* Faster, stealthier (doesn’t complete handshake), used for reconnaissance.
  **Cons**
* Requires raw sockets (root). Modern IDS can still detect SYN flood patterns.
  **When to use**
* Standard port discovery on LAN or authorized pentest.

---

## 3) UDP Scan (`-sU`)

**Command**

```bash
sudo nmap -sU -p 53,67,161 192.168.1.5
```

**How it works**

* Sends UDP packets to target ports. If response (UDP payload) → `open`. If ICMP port unreachable (type3/code3) → `closed`. No response → `open|filtered` (ambiguous).
  **Pros**
* Finds UDP services (DNS, SNMP, NTP, syslog).
  **Cons**
* Slow (retransmits), many UDP services don’t respond → lots of `open|filtered` results. Firewalls often block ICMP which complicates results.
  **When to use**
* To discover UDP-based services, but expect longer scan time.

---

## 4) FIN / NULL / XMAS Scans (`-sF`, `-sN`, `-sX`)

**Commands**

```bash
sudo nmap -sF 192.168.1.5
sudo nmap -sN 192.168.1.5
sudo nmap -sX 192.168.1.5
```

**How they work**

* Send unusual TCP flag combinations. RFC-compliant stacks will respond with `RST` for closed ports; open ports often ignore these unusual flags → stealthy signal.
  **Pros**
* Can bypass poorly configured IDS/firewalls that only look for SYNs.
  **Cons**
* Modern stacks/IDS detect these. Not reliable on Windows targets (Windows responds differently).
  **When to use**
* Legacy evasion attempts, curiosity in lab environments.

---

## 5) ACK Scan (`-sA`)

**Command**

```bash
sudo nmap -sA 192.168.1.5
```

**How it works**

* Sends ACK packets; used to determine whether a firewall is stateful/filtered. If port responds RST → unfiltered; no response/ICMP unreachable → filtered.
  **Use**
* Map firewall rulesets and detect stateful behavior.

---

## 6) Idle / Zombie Scan (`-sI`)

**Command**

```bash
sudo nmap -sI zombie_ip 192.168.1.5
```

**How it works**

* Uses a third-party “zombie” host to generate packets; analyzes IP ID sequence side-effects to infer port status — the scanner’s IP is hidden.
  **Pros**
* Extremely stealthy; target logs zombie IP, not you.
  **Cons**
* Requires a suitable idle zombie (predictable IP ID); complex; slow.
  **When to use**
* Advanced stealthy recon in lab/authorized testing.

---

## 7) SCTP Scans (`-sY`, `-sZ`)

**Command**

```bash
sudo nmap -sY -p 385 192.168.1.5
```

**Use**

* Scans SCTP services (telecom). Rare in general networks.

---

## 8) Ping Scan (`-sn`)

**Command**

```bash
nmap -sn 192.168.1.0/24
```

**What it does**

* Host discovery only — uses ICMP, TCP/ACK pings, ARP on local networks.
  **When to use**
* Quickly list live hosts before port scanning.

---

## 9) Version Detection (`-sV`) & OS Detection (`-O`)

**Commands**

```bash
sudo nmap -sV 192.168.1.5
sudo nmap -O 192.168.1.5
```

**What they do**

* `-sV`: Send probes to open ports to identify the service and versions.
* `-O`: Analyze TCP/IP fingerprint to guess target OS.
  **Notes**
* Combine with `-sS` and `-Pn` for detailed results; `-A` bundles many checks.

---

## 10) NSE (Nmap Scripting Engine) — `--script`

**Command**

```bash
sudo nmap --script vuln 192.168.1.5
sudo nmap -sV --script=http-enum 192.168.1.5 -p 80,443
```

**What it does**

* Scripts can do everything from banner grabbing to vulnerability checks, brute force, and advanced fingerprinting.
  **When to use**
* In-depth checks after initial discovery. Use `--script-help <name>` to learn what a script does.

---

## 🧾 Example Scan Workflows (Practical)

### a) Quick host discovery + common ports (fast):

```bash
sudo nmap -sn 192.168.1.0/24
sudo nmap -sS -Pn -p 22,80,443 192.168.1.100
```

### b) Full recon of a host (detailed):

```bash
sudo nmap -A -p- 192.168.1.100 -oN full_recon.txt
# -p- : scan all 65535 ports
```

### c) UDP + TCP combo (discover both protocols):

```bash
sudo nmap -sS -sU -p T:1-1024,U:53,67,69,123 192.168.1.100
```

### d) Stealthy / evasive attempts (lab only):

```bash
sudo nmap -sS -D RND:10 -f --mtu 24 192.168.1.100
# -D : decoys, -f : fragment packets, --mtu : smaller packets
```

---

## 🔎 Interpreting Common Nmap Port States

| State          | Meaning                                                                       |                               |
| -------------- | ----------------------------------------------------------------------------- | ----------------------------- |
| **open**       | Service is actively accepting connections.                                    |                               |
| **closed**     | No service listening; reachable.                                              |                               |
| **filtered**   | Packets blocked (firewall or no response); Nmap cannot determine open/closed. |                               |
| **unfiltered** | Port is reachable but Nmap can’t tell open/closed (ACK scan).                 |                               |
| **open         | filtered**                                                                    | No response (common for UDP). |
| **closed       | filtered**                                                                    | Ambiguous (rare).             |

---

## 🛡️ Detection, IDS, and Ethics

* **Stealth ≠ undetectable.** Modern IDS/IPS and EDR detect patterns (SYN bursts, fragmented packets, odd flags).
* **Use `-T` timing templates** to slow scans and reduce detection:

  * `-T0` snoop (paranoid), `-T1` sneaky, `-T3` default, `-T4` faster (LAN), `-T5` insane.
* **Always have explicit authorization** to scan: scanning without permission can be illegal (IT Act, computer misuse laws).
* **Log your scans** and keep results secure.

---

## ⚙️ Practical Tips & Gotchas

* **Root required** for raw packet scans (`-sS`, `-sU`, OS detection). Use `-sT` if unprivileged.
* **ARP is best on LAN**: on local networks Nmap uses ARP for fastest, most accurate host discovery.
* **UDP scans are slow**: limit ports or use `--top-ports` to speed up (e.g., `--top-ports 100`).
* **Combine scans smartly**: `sudo nmap -sS -sV -O --script vuln target` gives good reconnaissance in one go (but loud).
* **Use `-oA <basename>`** to save output in all formats (`.nmap`, `.xml`, `.gnmap`).
* **Firewalls & load balancers** can cause misleading results (many services behind one IP).

---

## ✅ Quick Reference Cheat-Sheet (common commands)

```bash
# Ping sweep (find live hosts)
nmap -sn 192.168.1.0/24

# SYN stealth scan (default port list)
sudo nmap -sS 192.168.1.10

# Full TCP connect scan (no root)
nmap -sT 192.168.1.10

# UDP scan (common UDP ports)
sudo nmap -sU -p 53,69,123 192.168.1.10

# Version + OS detection + traceroute (aggressive)
sudo nmap -A 192.168.1.10

# Scan all ports
sudo nmap -sS -p- 192.168.1.10

# Run vulnerability scripts
sudo nmap --script vuln 192.168.1.10

# Save outputs (all formats)
sudo nmap -A -oA myscan 192.168.1.10

# Stealthy idle scan using zombie
sudo nmap -sI 10.0.0.5 192.168.1.10
```

---

## Final Notes

* Start with **host discovery** (`-sn`), then `-sS` for TCP service discovery, then `-sV` and scripts for deeper inspection.
* Use **UDP scans** selectively; they’re slow and noisy.
* Use **timing and fragmentation** options to tune stealth/speed — but remember modern defenses may still detect you.
* **Legal & ethical reminder:** only scan networks you own or have explicit permission to test.

---

# 🔐 Cracking Password Hashes — Overview (quick)

1. **Identify** the hash type (MD5, NTLM, bcrypt, etc.).
2. **Prepare** the hash file in the correct format.
3. **Choose tool**: *Hashcat* for GPU-accelerated cracking; *John* (Jumbo) for flexible CPU/OpenCL + convenient pre/post processing.
4. **Select attack mode**: wordlist (dictionary), mask (brute-force with patterns), hybrid, rules, or combinations.
5. **Run** with appropriate options, monitor progress, and extract cracked passwords from the potfile.
6. **Analyze** results and improve strategy (better wordlists, rules, masks).

---

## ⚖️ Legal / Ethical Reminder (read this first)

* **Only** crack hashes for systems you own or where you have explicit authorization (lab, CTF, pentest with written consent).
* Unauthorized cracking is illegal and unethical. Follow laws (IT Act/Computer Misuse laws) and your organization’s policy.

---

## 🧾 Step 0 — Example lab hash files

Create simple hash files for tests.

**MD5 example (file: `hashes_md5.txt`)**

```
5f4dcc3b5aa765d61d8327deb882cf99
```

(That's the MD5 of `"password"`.)

**NTLM example (file: `hashes_ntlm.txt`)**

```
8846f7eaee8fb117ad06bdd830b7586c
```

(NTLM of `"password"`.)

---

## 🛠️ John the Ripper (Jumbo) — Quick primer

> Use **John the Ripper Jumbo** for best format and OpenCL/GPU support.

### Basic usage (dictionary + rules)

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt --rules hashes_md5.txt
```

Explanation:

* `--wordlist` / `--wordlist:` specify wordlist.
* `--rules` applies built-in mangling rules (common variations).
* John auto-detects format in many cases, but you can force it with `--format=raw-md5` etc.

### Force format explicitly

```bash
john --format=raw-md5 --wordlist=rockyou.txt hashes_md5.txt
```

### Show cracked passwords

```bash
john --show hashes_md5.txt
```

### Incremental / brute-force (CPU)

```bash
john --incremental hashes_md5.txt
```

`--incremental` uses pre-configured charset & lengths (slow on CPU for long/complex passwords).

### Dealing with /etc/shadow (Unix passwd)

Combine files with `unshadow`:

```bash
sudo unshadow /etc/passwd /etc/shadow > myshadow.txt
john --wordlist=rockyou.txt myshadow.txt
```

### Jumbo features

* OpenCL support (GPU) if built with it.
* `john.conf` contains rulesets, and you can create custom rules.

### Notes about John

* John stores cracked results in `john.pot` (potfile). Use `--pot=FILE` to customize.
* Use `john --list=formats` to see supported formats.

---

## ⚡ Hashcat — GPU-powered cracking

Hashcat is the go-to for large-scale cracking because it uses GPU acceleration and has many optimized kernels.

### Common attack modes (flag `-a`)

| Mode                |   Code | Description                          |
| ------------------- | -----: | ------------------------------------ |
| Straight (wordlist) | `-a 0` | Use wordlist and optionally rules    |
| Combination         | `-a 1` | Combine words from two wordlists     |
| Brute-force / Mask  | `-a 3` | Mask-based brute force (fast on GPU) |
| Hybrid (word+mask)  | `-a 6` | Wordlist + mask suffix               |
| Hybrid (mask+word)  | `-a 7` | Mask prefix + wordlist               |

### Example: basic wordlist attack

```bash
hashcat -m 0 -a 0 hashes_md5.txt /usr/share/wordlists/rockyou.txt --status --potfile-path=hashcat.pot
```

* `-m 0` = MD5 (common mapping; you can check `hashcat --help` for mapping list).
* `--status` shows progress; `--potfile-path` sets potfile.

> **Important:** Hash mode numbers (`-m`) are numeric codes; check `hashcat --help` or online docs for the correct `-m` for your hash type (NTLM, bcrypt, sha1, etc.).

### Example: NTLM with wordlist + rules

```bash
hashcat -m 1000 -a 0 hashes_ntlm.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule
```

* `-r` applies rule file (e.g., `best64.rule`) to mutate words.

### Example: mask attack (brute-force pattern)

```bash
# mask: 8 chars, 6 lowercase letters then 2 digits
hashcat -m 0 -a 3 hashes_md5.txt ?l?l?l?l?l?l?d?d
```

Mask tokens:

* `?l` = lowercase, `?u` = uppercase, `?d` = digits, `?s` = symbols, `?a` = all, `?1`..`?4` = custom charsets.

### Example: hybrid (wordlist + mask suffix)

```bash
# try each word + two digits suffix
hashcat -m 0 -a 6 hashes_md5.txt /usr/share/wordlists/rockyou.txt ?d?d
```

### Example: resuming a session & status

```bash
# start command with --session=name
hashcat --session=myrun -m 0 -a 0 hashes_md5.txt rockyou.txt
# to resume
hashcat --session=myrun --restore
```

### Show cracked passwords

```bash
hashcat --show -m 0 hashes_md5.txt --potfile-path=hashcat.pot
```

---

## 🧭 Hash Identification (crucial)

You must know the hash type. Mistaking it wastes time.

Methods:

* **Visual cues:** bcrypt starts with `$2a$`/`$2b$`/`$2y$`; MD5 is 32 hex chars; SHA1 is 40 hex chars; NTLM is 32 hex (but different content).
* **Tools:** `hashid`, `hash-identifier`, or `John` can often auto-detect.
* **John:** `john --list=formats` and try `--format=...` if auto-detection fails.

---

## 🧠 Salts & Special Formats

* **Salted hashes** (e.g., `sha256crypt`, bcrypt) include salt; cracking must respect the salt — both John and Hashcat handle these formats when the hash is in correct canonical representation (e.g., `/etc/shadow` formats, bcrypt `$2b$...` strings).
* **WPA/WPA2** uses EAPOL/PMKID capture files; Hashcat needs `-m 22000` (new unified format) or older `-m 2500` for pcap/handshake. Converting capture files to `.hccapx` used to be required for older modes.

---

## 🔁 Workflows & Examples (putting it together)

### Workflow A — Small lab MD5 with Hashcat (GPU)

1. `hashes_md5.txt` contains one MD5 hash.
2. Run:

```bash
hashcat -m 0 -a 0 hashes_md5.txt /usr/share/wordlists/rockyou.txt --status
```

3. If not cracked, add rules:

```bash
hashcat -m 0 -a 0 hashes_md5.txt /usr/share/wordlists/rockyou.txt -r rules/best64.rule
```

4. If still not cracked, try mask:

```bash
hashcat -m 0 -a 3 hashes_md5.txt ?l?l?l?l?l?d?d
```

### Workflow B — /etc/shadow with John

1. `unshadow /etc/passwd /etc/shadow > target_unshadowed.txt`
2. Run:

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt --rules target_unshadowed.txt
```

3. Check results:

```bash
john --show target_unshadowed.txt
```

---

## 🏁 Optimization Tips (practical)

* **Start with targeted wordlists** (company names, variants, leaked corp lists). `rockyou` is a good starting point for labs/CTFs.
* **Use rules** (Hashcat rules or John rules) to mutate wordlist entries (caps, leetspeak, suffix/prefix).
* **Use masks** for predictable patterns (like `?u?l?l?l?d?d` for `Aabc12`). Mask attacks are extremely fast on GPUs.
* **Benchmark first**: `hashcat -b` shows performance; helps choose strategies.
* **Use multiple strategies** in sequence: wordlist+rules → hybrid → mask → incremental.
* **Split job across GPUs** (hashcat auto-manages multi-GPU) or distribute across systems.
* **Exclude already cracked** with potfile to save time (`--potfile-path`).

---

## 🔎 Monitoring & Results

* **John**: `john --status` or check `john.pot`.
* **Hashcat**: `--status` prints progress; use `hashcat --show` with the potfile to list cracked entries.

---

## 📂 Common Practical Gotchas

* Hash file formatting: some hashes must be `username:hash` (e.g., NTLM from a SAM dump) — use `--username` or preprocess to supply only hashes.
* **Salted formats** must be in canonical representation (e.g., `/etc/shadow` lines for crypt hashes).
* **Rate-limiting**: Some systems add throttling or lockouts — on live systems prefer offline hashes only.
* **GPU heating/power**: long GPU runs require proper cooling and power management.

---

# ✅ Quick Command Cheat Sheet

**John**

```bash
john --wordlist=/path/to/rockyou.txt --rules hashes.txt
john --format=raw-md5 --wordlist=rockyou.txt hashes.txt
john --show hashes.txt
unshadow /etc/passwd /etc/shadow > myshadow && john myshadow --wordlist=rockyou.txt
```

**Hashcat**

```bash
# wordlist
hashcat -m <mode> -a 0 hashes.txt /usr/share/wordlists/rockyou.txt --status

# wordlist + rules
hashcat -m <mode> -a 0 hashes.txt wordlist.txt -r rules/best64.rule --status

# mask (brute-force)
hashcat -m <mode> -a 3 hashes.txt ?l?l?l?l?d?d

# hybrid (word+mask)
hashcat -m <mode> -a 6 hashes.txt wordlist.txt ?d?d

# show cracked
hashcat --show -m <mode> hashes.txt
```

*(Replace `<mode>` with the correct hash mode code — e.g., `0` for MD5, `1000` for NTLM — check `hashcat --help` or docs.)*

---

