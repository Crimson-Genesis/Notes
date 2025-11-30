# Network scanning
> target: mataspolitable 2
``` md
1. Introduction to network scanning 
    - what is network scanning
    - types
    - methodology
2. Introduction to Nmap
3. Perform different types of network scanning.
    - tcp scanning
    - udp scanning
    - syn scanning
    - fin scanning
    - attach all the scanning of the results
4. Follow the network scanning methodology for each steps (include ports, service version, OS)
5. Summary of the report
    - probably vulnerablilitys you found using searchsploit  or exploit-db.com
```

> Due on : 18th of NOV
---
---

# Introduction to Netowrk Scanning.
1. Network scanning is one of the earliest and most critical phases in penetration testing, ethical hacking, and network security assessment.
2. Before attacking or defending a system, you must first understand what systems exist, what ports are open, what services are running, what version they use, and how they may be exploited.
3. Network scanning acts like a digital reconnaissance step - identifying the structure, components, and vulnerabilities in the target environment.

## What is Network Scanning ? 
    1. Discovering live hosts.
    2. Enumerating open ports.
    3. Identifying services and versions.
    4. Detecting operating systems and system fingerprints.
    5. Mapping attack surface for later exploitation.

    > Why is Network Scanning Important.
    Helps understand what systems are rachable.
    reveals open ports -> protential entry points.
    gives service version info -> useful to search for vulnerabilities.
    helps determine IS type -> tailor exploits accordingly.
    helps identify weak configurations.

## Types of Network Scanning ?
    1. port scanning
        > TCP Scanning
        > SYN Scanning
        > FIN / XMAS / NULL scans
        > UDP Scanning
    2. Network scanning - which is also knows as host discovery.
    3. Vulnerability scanning
        > Outdated version
        > misconfigurations
        > CVEs
        > weak service banners
    4. service & version detection
    5. OS detection

## The Network Scanning Methodology ?
    Step 1 - Information gathering (Reconnaissance)
    Passive Recon:
        Collect info without touching the target (DNS, WHOIS, OSINT).
    Active Recon:
        Using ping, Nmap, ARP scans to identigy live hosts.

    Step 2 - Host discovery
        Identify which IPs are active.
        Tools: ARP scan, Ping sweep, Nmap discovery probes.

    Step 3 - Port scanning
        Scan the target's TCP / UDP ports to identify:
        > open
        > closed
        > filtered
        > unfiltered
        This reveals the attack surface.

    Step 4 - Service Enumeration
        Identify:
        > Service name (SSH / FTP / HTTP / etc.)
        > Version number
        > Service banners

    Step 5 - OS Fingerprinting
        Determiner OS, kernel, and device type.

    Step 6 - Vulnerability Mapping
        Use service / version info to exploit databases
        > exploit-db.com
        This step creates a list of probable vulnerabilities.

    Step 7 - Reporting
        Create a structured repote that includes:
        > methodology
        > scan results
        > identified vulnerabilities
        > screenshots or terminal output
        > CVE numbers
        > probable exploits
        > convlusion

# Introduction to Nmap
1. Nmap (Network Mapper) is the world's most widely-used network scanning, host discovery, and security auditing tool.
2. It is free, open-source utility built for network administrators, penetration tester, cyter-security analysts, and researchers.
3. Nmap works by sending raw packets to a target and analyzing the response to determine:
    > Which hosts are online
    > Which ports are open
    > Which services are running
    > What version these service use
    > What operating system the host is running
    > What vulnerabilityes may exist
    > Hos the network is configured and secured
    This makes Nmap the foundation tool for any penetration test.

# Different types of network scanning
1. TCP Scan.
A TCP Connect Scan (-sT) Complets the full three-way handshake with the target:
    1. SYN ->
    2. SYN-ACK <-
    3. ACK ->

![[2025-11-16-201124_hyprshot.png]]

2. SYN Scan (Half-open Scan)
SYN scan (-sS) is the most commonly used scan in pentetration testing.
It sends only:
    1. SYN ->
    2. SYN-ACK <-
    3. RST -> (insted of ACK, so connection is never completed)

![[2025-11-16-201518_hyprshot.png]]

3. UDP Scan
UDP scans (-sU) are used to identify services running on UDP ports, such as:
    > DNS (53)
    > DHCP (67/68)
    > SNMP (161)
    > NTP (123)
    > TFTP (69)
UDP scanning is the slow because
    > UDP has no handshake
    > Many UDP ports simply don't respond
    > Firewalls often drop UDP packets

![[2025-11-16-211607_hyprshot.png]]

4. FIN Scan
FIN scanning (-sF) sends a packet with only the FIN flag set.
This violates normal TCP behavior and is used to trick some firewalls.

Hot it works:
    > Closed ports respond with RST
    > Open ports do not resopnd
    > Direwalls may not detect it as a scan

FIN scan often returns ONLY CLOSED PORTS clearly.
open ports appear as:
```
open|filtered
```

FIN scan is mainly usefull when:
    > Firewalls block SYN scans
    > You want to evade IDS
    > You want to bypass filering rules
FIN scans do not give full detail - used mostly for stealth.

# Network Scanning Methodology
This is the SAME methodology used in OSCP, CEH, and real-world pentesting.
1. Host discovery
2. Port Scanning
3. Service & Version detection
4. OS Fingerprinting
5. Script Scanning (NSE)
6. Vulnerability Mapping (with versions)

## Step - 1 Host discovery
```
Command:
nmap -sn 192.168.56.102
```

![[2025-11-17-034453_hyprshot.png]]

> The machine is alive, reachable, and ready to be scanned.

## Step - 2 Full Port Scan
```
Command:
nmap -sS -p- 192.168.56.102 -T4
```

![[2025-11-16-201518_hyprshot.png]]

> This machine is wide open - perfect for hacking.

## Step - 3 Service & Version Detection
```
Command:
nmap -sV -p 21,22,23,25,53,80,111,139,445,512,513,514,3306,5432,6667,8009,8180 192.168.56.102
```

![[2025-11-17-034910_hyprshot.png]]

> Now we have to exact software versions - this is the GOLD for finding CVEs.

## Step - 4 OS Detection
```
Command:
nmap -O 192.168.56.102
```

![[2025-11-17-035447_hyprshot.png]]

> Metasploitable 2 is based on an old Ubuntu Linux kernel (2.6).
> This is a strong hing for kernel exploits.

## Step - 5 Script scanning
```
Command:
nmap --script vuln 192.168.56.102

Output:
Starting Nmap 7.95 ( https://nmap.org ) at 2025-11-16 17:28 EST
Nmap scan report for 192.168.56.102
Host is up (0.00018s latency).
Not shown: 977 closed tcp ports (reset)
PORT     STATE SERVICE
21/tcp   open  ftp
| ftp-vsftpd-backdoor: 
|   VULNERABLE:
|   vsFTPd version 2.3.4 backdoor
|     State: VULNERABLE (Exploitable)
|     IDs:  CVE:CVE-2011-2523  BID:48539
|       vsFTPd version 2.3.4 backdoor, this was reported on 2011-07-04.
|     Disclosure date: 2011-07-03
|     Exploit results:
|       Shell command: id
|       Results: uid=0(root) gid=0(root)
|     References:
|       https://www.securityfocus.com/bid/48539
|       http://scarybeastsecurity.blogspot.com/2011/07/alert-vsftpd-download-backdoored.html
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2011-2523
|_      https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/unix/ftp/vsftpd_234_backdoor.rb
22/tcp   open  ssh
23/tcp   open  telnet
25/tcp   open  smtp
| ssl-poodle: 
|   VULNERABLE:
|   SSL POODLE information leak
|     State: VULNERABLE
|     IDs:  CVE:CVE-2014-3566  BID:70574
|           The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other
|           products, uses nondeterministic CBC padding, which makes it easier
|           for man-in-the-middle attackers to obtain cleartext data via a
|           padding-oracle attack, aka the "POODLE" issue.
|     Disclosure date: 2014-10-14
|     Check results:
|       TLS_RSA_WITH_AES_128_CBC_SHA
|     References:
|       https://www.openssl.org/~bodo/ssl-poodle.pdf
|       https://www.imperialviolet.org/2014/10/14/poodle.html
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3566
|_      https://www.securityfocus.com/bid/70574
| ssl-dh-params: 
|   VULNERABLE:
|   Anonymous Diffie-Hellman Key Exchange MitM Vulnerability
|     State: VULNERABLE
|       Transport Layer Security (TLS) services that use anonymous
|       Diffie-Hellman key exchange only provide protection against passive
|       eavesdropping, and are vulnerable to active man-in-the-middle attacks
|       which could completely compromise the confidentiality and integrity
|       of any data exchanged over the resulting session.
|     Check results:
|       ANONYMOUS DH GROUP 1
|             Cipher Suite: TLS_DH_anon_WITH_AES_128_CBC_SHA
|             Modulus Type: Safe prime
|             Modulus Source: postfix builtin
|             Modulus Length: 1024
|             Generator Length: 8
|             Public Key Length: 1024
|     References:
|       https://www.ietf.org/rfc/rfc2246.txt
|   
|   Transport Layer Security (TLS) Protocol DHE_EXPORT Ciphers Downgrade MitM (Logjam)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2015-4000  BID:74733
|       The Transport Layer Security (TLS) protocol contains a flaw that is
|       triggered when handling Diffie-Hellman key exchanges defined with
|       the DHE_EXPORT cipher. This may allow a man-in-the-middle attacker
|       to downgrade the security of a TLS session to 512-bit export-grade
|       cryptography, which is significantly weaker, allowing the attacker
|       to more easily break the encryption and monitor or tamper with
|       the encrypted stream.
|     Disclosure date: 2015-5-19
|     Check results:
|       EXPORT-GRADE DH GROUP 1
|             Cipher Suite: TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA
|             Modulus Type: Safe prime
|             Modulus Source: Unknown/Custom-generated
|             Modulus Length: 512
|             Generator Length: 8
|             Public Key Length: 512
|     References:
|       https://www.securityfocus.com/bid/74733
|       https://weakdh.org
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4000
|   
|   Diffie-Hellman Key Exchange Insufficient Group Strength
|     State: VULNERABLE
|       Transport Layer Security (TLS) services that use Diffie-Hellman groups
|       of insufficient strength, especially those using one of a few commonly
|       shared groups, may be susceptible to passive eavesdropping attacks.
|     Check results:
|       WEAK DH GROUP 1
|             Cipher Suite: TLS_DHE_RSA_WITH_AES_256_CBC_SHA
|             Modulus Type: Safe prime
|             Modulus Source: postfix builtin
|             Modulus Length: 1024
|             Generator Length: 8
|             Public Key Length: 1024
|     References:
|_      https://weakdh.org
|_sslv2-drown: ERROR: Script execution failed (use -d to debug)
| smtp-vuln-cve2010-4344: 
|_  The SMTP server is not Exim: NOT VULNERABLE
53/tcp   open  domain
80/tcp   open  http
| http-slowloris-check: 
|   VULNERABLE:
|   Slowloris DOS attack
|     State: LIKELY VULNERABLE
|     IDs:  CVE:CVE-2007-6750
|       Slowloris tries to keep many connections to the target web server open and hold
|       them open as long as possible.  It accomplishes this by opening connections to
|       the target web server and sending a partial request. By doing so, it starves
|       the http server's resources causing Denial Of Service.
|       
|     Disclosure date: 2009-09-17
|     References:
|       http://ha.ckers.org/slowloris/
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750
|_http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug)
|_http-trace: TRACE is enabled
| http-csrf: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.56.102
|   Found the following possible CSRF vulnerabilities: 
|     
|     Path: http://192.168.56.102:80/dvwa/
|     Form id: 
|     Form action: login.php
|     
|     Path: http://192.168.56.102:80/dvwa/login.php
|     Form id: 
|     Form action: login.php
|     
|     Path: http://192.168.56.102:80/mutillidae/index.php?page=register.php
|     Form id: id-bad-cred-tr
|     Form action: index.php?page=register.php
|     
|     Path: http://192.168.56.102:80/mutillidae/index.php?page=user-poll.php
|     Form id: idpollform
|_    Form action: index.php
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-sql-injection: 
|   Possible sqli for queries:
|     http://192.168.56.102:80/dav/?C=N%3BO%3DD%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=S%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=D%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=M%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=home.php&do=toggle-security%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=register.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=user-poll.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=show-log.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=capture-data.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=arbitrary-file-inclusion.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=user-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=login.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=notes.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=php-errors.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=documentation%2Fvulnerabilities.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=usage-instructions.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=site-footer-xss-discussion.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=documentation%2Fhow-to-access-Mutillidae-over-Virtual-Box-network.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=view-someones-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=change-log.htm%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=pen-test-tool-lookup.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=view-someones-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=framing.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=credits.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=secret-administrative-pages.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=home.php&do=toggle-hints%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=text-file-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=dns-lookup.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=add-to-your-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=source-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=captured-data.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=user-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=add-to-your-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=source-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=home.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=html5-storage.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=set-background-color.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=credits.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=login.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=text-file-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=installation.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?username=anonymous&page=password-generator.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=browser-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=show-log.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=N%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=S%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=D%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=M%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=N%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=S%3BO%3DD%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=D%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=M%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=N%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=M%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=S%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=D%3BO%3DD%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=M%3BO%3DD%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=N%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=S%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.56.102:80/dav/?C=D%3BO%3DA%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=home.php&do=toggle-security%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=register.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=user-poll.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=show-log.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=capture-data.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=arbitrary-file-inclusion.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=user-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=login.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=notes.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=php-errors.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=documentation%2Fvulnerabilities.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=usage-instructions.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=site-footer-xss-discussion.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=documentation%2Fhow-to-access-Mutillidae-over-Virtual-Box-network.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=view-someones-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=change-log.htm%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=pen-test-tool-lookup.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=view-someones-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=framing.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=credits.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=secret-administrative-pages.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=home.php&do=toggle-hints%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=text-file-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=dns-lookup.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=add-to-your-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=source-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=captured-data.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=user-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=add-to-your-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=source-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=home.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=html5-storage.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=set-background-color.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=credits.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=login.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=text-file-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=installation.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?username=anonymous&page=password-generator.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=browser-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=show-log.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=register.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=user-poll.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=show-log.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=capture-data.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=arbitrary-file-inclusion.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=user-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=login.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=documentation%2Fvulnerabilities.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=documentation%2Fhow-to-access-Mutillidae-over-Virtual-Box-network.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=site-footer-xss-discussion.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=pen-test-tool-lookup.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=home.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=change-log.htm%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=framing.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=view-someones-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=credits.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=secret-administrative-pages.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=user-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=text-file-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=dns-lookup.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=add-to-your-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=source-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=view-someones-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=add-to-your-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=source-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=captured-data.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=html5-storage.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=set-background-color.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=credits.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=login.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=text-file-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=installation.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?username=anonymous&page=password-generator.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=browser-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=show-log.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=register.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=user-poll.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=view-someones-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=arbitrary-file-inclusion.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=user-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=login.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=documentation%2Fvulnerabilities.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=documentation%2Fhow-to-access-Mutillidae-over-Virtual-Box-network.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=site-footer-xss-discussion.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=user-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=home.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=change-log.htm%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=framing.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=pen-test-tool-lookup.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=view-someones-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=credits.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=secret-administrative-pages.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=add-to-your-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=captured-data.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=text-file-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=dns-lookup.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=source-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=capture-data.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=show-log.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=add-to-your-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=source-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=show-log.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=html5-storage.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=set-background-color.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=credits.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=login.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=text-file-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=installation.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?username=anonymous&page=password-generator.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=browser-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=register.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=user-poll.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=show-log.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=arbitrary-file-inclusion.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=user-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=login.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=documentation%2Fvulnerabilities.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=documentation%2Fhow-to-access-Mutillidae-over-Virtual-Box-network.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=site-footer-xss-discussion.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=view-someones-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=change-log.htm%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=framing.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=pen-test-tool-lookup.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=view-someones-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=credits.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=secret-administrative-pages.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=add-to-your-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=captured-data.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=text-file-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=dns-lookup.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=source-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=capture-data.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=show-log.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=user-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=add-to-your-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=source-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=home.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=html5-storage.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=set-background-color.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=credits.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=login.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=text-file-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=installation.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?username=anonymous&page=password-generator.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=browser-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=register.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=user-poll.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=view-someones-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=capture-data.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=arbitrary-file-inclusion.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=user-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=login.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=capture-data.php&do=toggle-hints%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=documentation%2Fvulnerabilities.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=site-footer-xss-discussion.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=documentation%2Fhow-to-access-Mutillidae-over-Virtual-Box-network.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=change-log.htm%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=user-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=pen-test-tool-lookup.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=view-someones-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=framing.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=credits.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=secret-administrative-pages.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=capture-data.php&do=toggle-security%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=text-file-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=dns-lookup.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=add-to-your-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=source-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=home.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=show-log.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=add-to-your-blog.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=source-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=show-log.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=html5-storage.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=set-background-color.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=credits.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=login.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/?page=text-file-viewer.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=installation.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?username=anonymous&page=password-generator.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=browser-info.php%27%20OR%20sqlspider
|     http://192.168.56.102:80/mutillidae/index.php?page=captured-data.php%27%20OR%20sqlspider
|   Possible sqli for forms:
|     Form at path: /mutillidae/index.php, form's action: index.php. Fields that might be vulnerable:
|       choice
|       choice
|       choice
|       choice
|       choice
|       choice
|       choice
|       choice
|       choice
|       choice
|       choice
|       choice
|_      initials
| http-enum: 
|   /tikiwiki/: Tikiwiki
|   /test/: Test page
|   /phpinfo.php: Possible information file
|   /phpMyAdmin/: phpMyAdmin
|   /doc/: Potentially interesting directory w/ listing on 'apache/2.2.8 (ubuntu) dav/2'
|   /icons/: Potentially interesting folder w/ directory listing
|_  /index/: Potentially interesting folder
|_http-dombased-xss: Couldn't find any DOM based XSS.
111/tcp  open  rpcbind
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
512/tcp  open  exec
513/tcp  open  login
514/tcp  open  shell
1099/tcp open  rmiregistry
| rmi-vuln-classloader: 
|   VULNERABLE:
|   RMI registry default configuration remote code execution vulnerability
|     State: VULNERABLE
|       Default configuration of RMI registry allows loading classes from remote URLs which can lead to remote code execution.
|       
|     References:
|_      https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/misc/java_rmi_server.rb
1524/tcp open  ingreslock
2049/tcp open  nfs
2121/tcp open  ccproxy-ftp
3306/tcp open  mysql
|_ssl-ccs-injection: No reply from server (TIMEOUT)
5432/tcp open  postgresql
| ssl-ccs-injection: 
|   VULNERABLE:
|   SSL/TLS MITM vulnerability (CCS Injection)
|     State: VULNERABLE
|     Risk factor: High
|       OpenSSL before 0.9.8za, 1.0.0 before 1.0.0m, and 1.0.1 before 1.0.1h
|       does not properly restrict processing of ChangeCipherSpec messages,
|       which allows man-in-the-middle attackers to trigger use of a zero
|       length master key in certain OpenSSL-to-OpenSSL communications, and
|       consequently hijack sessions or obtain sensitive information, via
|       a crafted TLS handshake, aka the "CCS Injection" vulnerability.
|           
|     References:
|       http://www.cvedetails.com/cve/2014-0224
|       http://www.openssl.org/news/secadv_20140605.txt
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0224
| ssl-dh-params: 
|   VULNERABLE:
|   Diffie-Hellman Key Exchange Insufficient Group Strength
|     State: VULNERABLE
|       Transport Layer Security (TLS) services that use Diffie-Hellman groups
|       of insufficient strength, especially those using one of a few commonly
|       shared groups, may be susceptible to passive eavesdropping attacks.
|     Check results:
|       WEAK DH GROUP 1
|             Cipher Suite: TLS_DHE_RSA_WITH_AES_256_CBC_SHA
|             Modulus Type: Safe prime
|             Modulus Source: Unknown/Custom-generated
|             Modulus Length: 1024
|             Generator Length: 8
|             Public Key Length: 1024
|     References:
|_      https://weakdh.org
| ssl-poodle: 
|   VULNERABLE:
|   SSL POODLE information leak
|     State: VULNERABLE
|     IDs:  CVE:CVE-2014-3566  BID:70574
|           The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other
|           products, uses nondeterministic CBC padding, which makes it easier
|           for man-in-the-middle attackers to obtain cleartext data via a
|           padding-oracle attack, aka the "POODLE" issue.
|     Disclosure date: 2014-10-14
|     Check results:
|       TLS_RSA_WITH_AES_128_CBC_SHA
|     References:
|       https://www.openssl.org/~bodo/ssl-poodle.pdf
|       https://www.imperialviolet.org/2014/10/14/poodle.html
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3566
|_      https://www.securityfocus.com/bid/70574
5900/tcp open  vnc
6000/tcp open  X11
6667/tcp open  irc
|_irc-unrealircd-backdoor: Looks like trojaned version of unrealircd. See http://seclists.org/fulldisclosure/2010/Jun/277
8009/tcp open  ajp13
8180/tcp open  unknown
| http-cookie-flags: 
|   /admin/: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/index.html: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/login.html: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/admin.html: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/account.html: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/admin_login.html: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/home.html: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/admin-login.html: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/adminLogin.html: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/controlpanel.html: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/cp.html: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/index.jsp: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/login.jsp: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/admin.jsp: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/home.jsp: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/controlpanel.jsp: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/admin-login.jsp: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/cp.jsp: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/account.jsp: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/admin_login.jsp: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/adminLogin.jsp: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/view/javascript/fckeditor/editor/filemanager/connectors/test.html: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/includes/FCKeditor/editor/filemanager/upload/test.html: 
|     JSESSIONID: 
|       httponly flag not set
|   /admin/jscript/upload.html: 
|     JSESSIONID: 
|_      httponly flag not set
| http-slowloris-check: 
|   VULNERABLE:
|   Slowloris DOS attack
|     State: LIKELY VULNERABLE
|     IDs:  CVE:CVE-2007-6750
|       Slowloris tries to keep many connections to the target web server open and hold
|       them open as long as possible.  It accomplishes this by opening connections to
|       the target web server and sending a partial request. By doing so, it starves
|       the http server's resources causing Denial Of Service.
|       
|     Disclosure date: 2009-09-17
|     References:
|       http://ha.ckers.org/slowloris/
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750
| http-enum: 
|   /admin/: Possible admin folder
|   /admin/index.html: Possible admin folder
|   /admin/login.html: Possible admin folder
|   /admin/admin.html: Possible admin folder
|   /admin/account.html: Possible admin folder
|   /admin/admin_login.html: Possible admin folder
|   /admin/home.html: Possible admin folder
|   /admin/admin-login.html: Possible admin folder
|   /admin/adminLogin.html: Possible admin folder
|   /admin/controlpanel.html: Possible admin folder
|   /admin/cp.html: Possible admin folder
|   /admin/index.jsp: Possible admin folder
|   /admin/login.jsp: Possible admin folder
|   /admin/admin.jsp: Possible admin folder
|   /admin/home.jsp: Possible admin folder
|   /admin/controlpanel.jsp: Possible admin folder
|   /admin/admin-login.jsp: Possible admin folder
|   /admin/cp.jsp: Possible admin folder
|   /admin/account.jsp: Possible admin folder
|   /admin/admin_login.jsp: Possible admin folder
|   /admin/adminLogin.jsp: Possible admin folder
|   /manager/html/upload: Apache Tomcat (401 Unauthorized)
|   /manager/html: Apache Tomcat (401 Unauthorized)
|   /admin/view/javascript/fckeditor/editor/filemanager/connectors/test.html: OpenCart/FCKeditor File upload
|   /admin/includes/FCKeditor/editor/filemanager/upload/test.html: ASP Simple Blog / FCKeditor File Upload
|   /admin/jscript/upload.html: Lizard Cart/Remote File upload
|_  /webdav/: Potentially interesting folder
MAC Address: 08:00:27:09:22:81 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Host script results:
|_smb-vuln-ms10-054: false
|_smb-vuln-ms10-061: false
|_smb-vuln-regsvc-dos: ERROR: Script execution failed (use -d to debug)

Nmap done: 1 IP address (1 host up) scanned in 331.60 seconds
                                                                
```


> Nmap will detect vulnerabilities like:
> 1. vsftpd 2.3.4 backdoor
> 2. Samba 3.0.20 RCE
> 3. UnreallRCd backdoor
> 4. Tomcat manager weak credentials
> 5. MySQL no auth

> This Nmap scripts confirm which services are exploitable.

## Step - 6 Vulnerability Mapping
```
searchsploit vsftpd 2.3.4
searchsploit samba 3.0.20
searchsploit unreal ircd
searchsploit tomcat
searchsploit postgres 8.3
```

> Ready for exploitation using:
> 1. Metasploit
> 2. Manual exploits
> 3. Python scripts
> 4. Reverse shells


| Port    | Service    | Version        | OS Impact                 |
| ------- | ---------- | -------------- | ------------------------- |
| 21      | FTP        | vsftpd 2.3.4   | Backdoor shell (RCE)      |
| 22      | SSH        | OpenSSH 4.7p1  | User brute-force possible |
| 23      | Telnet     | (no version)   | Cleartext login           |
| 25      | SMTP       | Postfix smtpd  | VRFY user enumeration     |
| 53      | DNS        | BIND 9.4.2     | Zone transfer/DoS         |
| 80      | HTTP       | Apache 2.2.8   | Web exploits              |
| 111     | rpcbind    | RPC v2         | NFS enumeration           |
| 139/445 | Samba      | smbd 3.0.20    | RCE CVE-2007-2447         |
| 3306    | MySQL      | 5.0.51a        | Weak credentials          |
| 5432    | PostgreSQL | 8.3.0          | Auth bypass               |
| 6667    | IRC        | UnrealIRCd     | Backdoor RCE              |
| 8009    | ajp13      | Apache JServ   | File include              |
| 8180    | Tomcat     | Coyote JSP 1.1 | Manager RCE               |


---

# 5. Summary of the Report (Metasploitable 2 scan)

## Executive summary

The target (Metasploitable 2 — example IP `192.168.56.102`) exposes a large number of intentionally vulnerable services (FTP, Samba, UnrealIRCd, Tomcat, MySQL, etc.). Nmap service/version detection and NSE vulnerability scripts flag multiple high-risk, publicly-exploitable issues (remote code execution backdoors and service misconfigurations) that are trivially exploitable in a lab environment. The results below list the most relevant findings mapped to public exploits (Exploit-DB / Metasploit), with suggested verification commands and remediation guidance.

---

## High-confidence exploitable findings (what you must triage first)

> I list each vuln with a short description, an exploit reference (Exploit-DB / Rapid7/Metasploit), and a quick verification tip.

1. **vsftpd 2.3.4 — backdoor (CVE-2011-2523)**

   * What: a malicious backdoor present in a specific vsftpd 2.3.4 release that spawns a shell (listens on port 6200).
   * Exploit references: Exploit-DB EDB-IDs for vsftpd backdoor (examples).
   * Quick check: `nmap --script ftp-vsftpd-backdoor -p21 192.168.56.102` or use the Metasploit module `unix/ftp/vsftpd_234_backdoor`.
   * Risk: **Critical (RCE / root shell)**
   * Remediation: Replace vsftpd with a patched release; remove vulnerable package; block or monitor FTP.

2. **Samba 3.0.20 — username map script / RPC RCE (CVE-2007-2447)**

   * What: several remote code execution paths in old Samba versions (username map script and related RPC functions).
   * Exploit references: Exploit-DB Samba exploit and Rapid7 Metasploit module.
   * Quick check: `searchsploit samba 3.0.20` or run the Metasploit `multi/samba/usermap_script` module.
   * Risk: **High (RCE / remote exploit)**
   * Remediation: Upgrade Samba to a fixed version; disable risky smb.conf options; apply vendor patches.

3. **UnrealIRCd 3.2.8.1 — backdoor (CVE-2010-2075)**

   * What: a backdoor added to distributed UnrealIRCd 3.2.8.1 that allows remote command execution.
   * Exploit references: Exploit-DB and Rapid7 Metasploit module for UnrealIRCd backdoor.
   * Quick check: use the Metasploit `unix/irc/unreal_ircd_3281_backdoor` module or searchsploit for `unrealircd`.
   * Risk: **Critical (RCE / possible root)**
   * Remediation: Remove or upgrade UnrealIRCd; only install from trusted sources; monitor network for suspicious IRC traffic.

4. **Apache Tomcat (manager/webapps) — manager upload / auth issues (multiple CVEs / weak protections)**

   * What: default or outdated Tomcat managers and webapps can allow authenticated upload or known RCEs via manager or flawed components. Metasploitable includes Tomcat instances vulnerable to manager upload/execution.
   * Exploit references: Exploit-DB tomcat manager deploy / upload modules.
   * Quick check: `nmap -sV --script http-enum -p 8080,8180 192.168.56.102` then attempt authenticated manager actions if credentials known/weak.
   * Risk: **High (RCE if manager accessible / creds weak)**
   * Remediation: Disable unused manager apps; enforce strong creds; apply patches.

5. **MySQL / PostgreSQL — weak/no auth & old versions**

   * What: old DB server versions and default/no passwords allow login and data access; some versions have local privilege-escalation or remote issues.
   * Exploit references: Example exploits on Exploit-DB for MySQL auth issues; various local privesc for older MySQL/Postgres.
   * Quick check: attempt `mysql -u root -p -h 192.168.56.102` (try empty password) and `psql` connections; run `searchsploit mysql 5.0` or `searchsploit postgresql 8.3`.
   * Risk: **High (data access / privilege escalation)**
   * Remediation: Enforce strong DB passwords, bind DB to localhost if not needed remotely, patch DB.

6. **HTTP apps (DVWA / Mutillidae / phpMyAdmin / others) — SQLi / CSRF / insecure cookie flags / file upload**

   * What: web applications present in Metasploitable show multiple web vulnerabilities: SQL Injection, CSRF, file upload endpoints, poor cookie flags. Nmap HTTP scripts discovered many possible injection points.
   * Evidence: long list of possible SQLi/CSRF paths flagged by Nmap NSE.
   * Quick check: run `nikto`, `dirb`, or `burpsuite` against `http://192.168.56.102:80` and test the listed paths.
   * Risk: **Medium–High (data theft, RCE via file upload)**
   * Remediation: patch web apps, remove vulnerable demo apps from production, enforce content security policies and secure cookies.

---

## Full table (concise) — copy into your report

| Port    | Service    | Version                 | Probable exploit (ref)                                                          |
| ------- | ---------- | ----------------------- | ------------------------------------------------------------------------------- |
| 21      | FTP        | vsftpd 2.3.4            | vsftpd backdoor (CVE-2011-2523). Exploit-DB & Metasploit.                       |
| 22      | SSH        | OpenSSH 4.7p1           | Old SSH — brute/weak algos possible (general hardening).                        |
| 23      | Telnet     | —                       | Cleartext auth — trivial credential capture.                                    |
| 25      | SMTP       | Postfix smtpd           | TLS/POODLE/weak DH findings in NSE output (MitM risk).                          |
| 53      | DNS        | BIND 9.4.2              | Zone transfer / DoS (legacy BIND).                                              |
| 80      | HTTP       | Apache 2.2.8 + web apps | DVWA/Mutillidae SQLi/CSRF/file upload — many NSE hits.                          |
| 111     | rpcbind    | RPC v2                  | NFS / RPC enumeration.                                                          |
| 139/445 | Samba      | smbd 3.0.20             | Samba username map / RPC RCE (CVE-2007-2447). Exploit-DB / Metasploit.          |
| 3306    | MySQL      | 5.0.51a                 | Default / weak credentials; DB exploits available.                              |
| 5432    | PostgreSQL | 8.3.0                   | Old Postgres, SSL/TLS issues flagged (CCS injection).                           |
| 6667    | IRC        | UnrealIRCd              | Trojan/backdoor in UnrealIRCd 3.2.8.1 (CVE-2010-2075). Exploit-DB / Metasploit. |
| 8009    | AJP13      | Apache JServ            | AJP-related file include/other issues (check further).                          |
| 8180    | Tomcat     | Coyote JSP 1.1          | Tomcat manager / upload RCE references.                                         |



