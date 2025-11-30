# create malware/payloads
> Create a report

1. Introduction to malware
    - what
    - types
    - mitigation
2. Brief about the msvenom
3. Create a payload using msfvenom
4. Check the payload in the virustotal (to see the AV ventors are identifing or not)
5. Utilize Encoders using msfvenom
6. Test it in virustotal.com

7. Summary: types  of payloads and techniques

> Due on: 20th of NOV

send to **manoj@acmegrade.in**

---
---

# Introduction to malware
## Waht is Malware ?

Malware (malicious software) is any software created to harm, exploit, or gain unauthorized control over a computer system, network, or device.
Its goal is to break Confidentiality, Integrity, or Availability (CIA Triad).

## Types of Malware

1. Virus
    * Injects itself into clean files
    * Executes only when the host file is opened
    * Spread is slower because it needs user action

2. Worm
    * Self-replicating
    * Spreads automatically across networks
    * Famous: WannaCry worm

3. Trojan
    * Looks legitimate but carries malicious code
    * Common in cracked games/apps

4. Ransomware
    * Encrypts files and demands payment
    * Extremely damaging (e.g., LockBit, WannaCry)

5. Spyware
    * Secretly monitors user activity
    * Can log keystrokes, passwords, browsing history

6. Keylogger
    * Specialized spyware that captures keyboard inputs

7. Adware
    * Shows unwanted ads
    * Sometimes used as a pathway to more malware

8. Rootkit
    * Hides malicious activity
    * Provides stealthy admin-level access

9. Backdoor
    * Creates unauthorized remote access into the system

10. Botnet Malware
    * Turns infected machines into "bots"
    * Used for DDoS, spam, automated attacks

Mitigation (How to Prevent & Reduce Malware Risk)
1. Preventive Controls
    * Update OS and apps regularly
    * Install and maintain antivirus/EDR
    * Enable firewalls (host + network)
    * Avoid running unknown or pirated software
    * Block macros in documents

2. Detection Controls
    * Antivirus signature scanning
    * Heuristic and behavioral analysis
    * SIEM alerts
    * Sandboxing suspicious files
    * Network monitoring for anomalies

3. Response & Recovery
    * Isolate infected system
    * Remove malware using AV/EDR tools
    * Restore from backups
    * Patch exploited vulnerabilities
    * Change compromised credentials

4. User Awareness
    * Recognize phishing
    * Avoid unknown USBs
    * Don’t install random apps
    * Verify websites before entering credentials

# Msfvenom

Msfvenom is a combination of two older Metasploit tools:
    * msfpayload (for generating payloads)
    * msfencode (for encoding/obfuscating payloads)
    * Both were merged to create a single, powerful tool called msfvenom.

Msfvenom is mainly used to:

1. Generate Payloads
    * It can create payloads for:
    * Windows
    * Linux
    * Android (.apk)
    * macOS
    * Python
    * PHP
    * ASP, JSP, etc.

2. Encode Payloads
    * Encoders attempt to:
    * Obfuscate the payload
    * Make it harder for basic detection systems to recognize
    * Avoid pattern-based signature detection

3. Format Output Files
    * msfvenom can output payloads in many formats:
    * Executable files
    * Shellcode
    * Scripts
    * Raw bytes
    * HEX
    * C, Python, Ruby formats

4. Customize Payloads
    * Using options like:
    * LHOST (attacker IP for testing)
    * LPORT (listener port)
    * Platform selection
    * Architecture (x86, x64)


# Creating Payload's in msfvenom

> Step 1: Choose the Payload
A payload defines what action will occur when the file executes.
Example categories (safe to mention):
    * Reverse shells
    * Bind shells
    * Meterpreter-based interactions
    * Platform-specific payloads (Windows, Linux, Android, etc.)
You select:
    * Platform (Windows / Linux / Android)
    * Architecture (x86 / x64)

> Step 2: Set Payload Options

Every payload requires configuration parameters such as:
    * LHOST → your testing machine’s IP (attack side in lab)
    * LPORT → port that will receive the connection

These are needed so that the payload knows where to connect back (again, only in a controlled lab).

> Step 3: Choose Output Format

msfvenom supports many formats such as:
    * .exe (executables)
    * .apk (Android apps)
    * .elf (Linux binaries)
    * .ps1 (PowerShell)
    * Script formats like Python, C, Ruby, etc.

> Step 4: Generate the Output File

When the tool runs, it produces a binary or script file that contains:
    * Encoded payload
    * Necessary stubs to run
    * Metadata

![[2025-11-20-214411_hyprshot.png]]
# Checking the Payload in VirusTotal (to see if AV vendors identify it or not)
![[2025-11-20-214832_hyprshot.png]]
![[2025-11-20-214843_hyprshot.png]]
![[2025-11-20-214850_hyprshot.png]]

# Utilizing Encoders in msfvenom

Encoders in msfvenom are used to modify the structure of a payload so that its byte pattern changes.

![[2025-11-20-215344_hyprshot.png]]
# Test the encoded payload in virustotal.com

![[2025-11-20-215610_hyprshot.png]]
![[2025-11-20-215619_hyprshot.png]]
![[2025-11-20-215626_hyprshot.png]]

