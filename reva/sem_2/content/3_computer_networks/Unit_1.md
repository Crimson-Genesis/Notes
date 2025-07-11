# Unit - 1 -> Introduction and the physical layer
* Introduction: Network applications, network hardware, network software, refernce models: OSI, TCP/IP, Internet.
* The Physical Layer: signals, Transmission impairment.
* Transmission: Serial transmission, guided transmission media, wireless transmission, the public switched telephone networks, mobile telephone system.

## Content ->
### **Introduction to Computer Networks**

---

#### **1. Network Applications**

* **Resource Sharing**: Allows multiple users to share printers, files, storage, etc.
* **Client-Server Communication**: Applications like email, file transfer, and remote login work using this model.
* **E-commerce and E-banking**: Transactions over the internet require reliable network communication.
* **Multimedia Communication**: Includes video conferencing, VoIP, IPTV, etc.
* **Social Networking**: Platforms like Facebook, Instagram, WhatsApp function over networks.
* **Cloud Computing**: On-demand resource access over the internet.

---

#### **2. Network Hardware**

* **Personal Computers (PCs)**: Used as clients or servers.
* **Workstations**: High-end PCs for network tasks.
* **Servers**: Provide services like file storage, web hosting.
* **Routers**: Connect different networks and forward packets based on IP address.
* **Switches**: Forward frames based on MAC addresses within the same network.
* **Bridges**: Connect LAN segments, forwarding frames selectively.
* **Modems**: Convert digital signals to analog and vice versa.
* **Access Points**: Provide wireless access to a wired network.

---

#### **3. Network Software**

* **Protocol**: A set of rules for communication (e.g., TCP, HTTP, FTP).
* **Services**: Defined set of operations offered by one layer to the layer above.
* **Peer-to-Peer Model**: All nodes act as both clients and servers.
* **Client-Server Model**: Dedicated server provides services to multiple clients.
* **Socket Programming**: Enables process-to-process communication using IP address and port number.

---

#### **4. Reference Models**

---

##### **A. OSI Model (Open Systems Interconnection)**

* **Layer 1 - Physical Layer**: Deals with bit transmission over physical medium.
* **Layer 2 - Data Link Layer**: Frames data and handles error detection.
* **Layer 3 - Network Layer**: Handles routing and addressing (IP).
* **Layer 4 - Transport Layer**: Provides reliable data transfer (TCP).
* **Layer 5 - Session Layer**: Manages sessions and dialogues.
* **Layer 6 - Presentation Layer**: Data translation, encryption, compression.
* **Layer 7 - Application Layer**: Interface for user applications (HTTP, FTP).

---

##### **B. TCP/IP Model**

* **Link Layer**: Includes physical and data link functionality.
* **Internet Layer**: Handles IP addressing and routing.
* **Transport Layer**: Provides end-to-end communication (TCP/UDP).
* **Application Layer**: Includes all high-level protocols like HTTP, FTP, SMTP.

---

##### **Comparison of OSI and TCP/IP Models**

| Aspect          | OSI Model                                        | TCP/IP Model                        |
| --------------- | ------------------------------------------------ | ----------------------------------- |
| Layers          | 7                                                | 4                                   |
| Standard        | Generic, protocol independent                    | Protocol-specific (Internet)        |
| Transport Layer | Connection-oriented (TCP) & Connectionless (UDP) | TCP and UDP supported               |
| Model Use       | Conceptual                                       | Practical and used in real networks |

---

#### **5. The Internet**

* **Definition**: A global network of interconnected computers using the TCP/IP protocol suite.
* **Components**:

  * **ISPs (Internet Service Providers)**: Provide access to users.
  * **Backbone Routers**: High-speed routers that form the core.
  * **DNS Servers**: Translate domain names to IP addresses.
  * **Web Servers**: Host websites and provide HTTP services.
* **IP Addressing**: Uniquely identifies devices; IPv4 and IPv6 formats.
* **Domain Name System (DNS)**: Resolves domain names to IP addresses.
* **Protocols Used**: HTTP, FTP, TCP, IP, DNS, SMTP, etc.

---
### **Network Applications**

---

#### **1. File Sharing**

* **Function**: Enables users to store and access files from remote systems.
* **Protocols**: FTP (File Transfer Protocol), SFTP, SMB.
* **Usage**: Shared drives in organizations, distributed file systems like NFS.

---

#### **2. Remote Access**

* **Function**: Access and control a computer remotely.
* **Protocols**: Telnet, SSH (Secure Shell), RDP (Remote Desktop Protocol).
* **Usage**: Server administration, remote troubleshooting.

---

#### **3. Web Services**

* **Function**: Access websites, web applications, and resources over the internet.
* **Protocols**: HTTP, HTTPS.
* **Usage**: Browsing, e-commerce, social media.

---

#### **4. Email Communication**

* **Function**: Sending and receiving electronic mail messages.
* **Protocols**: SMTP (Simple Mail Transfer Protocol), POP3, IMAP.
* **Usage**: Personal and professional communication.

---

#### **5. Voice over IP (VoIP)**

* **Function**: Transmitting voice over the internet.
* **Protocols**: SIP (Session Initiation Protocol), RTP (Real-time Transport Protocol).
* **Usage**: Skype, Zoom, Google Meet, WhatsApp Calls.

---

#### **6. Video Conferencing**

* **Function**: Real-time video communication between users.
* **Protocols**: WebRTC, SIP.
* **Usage**: Online meetings, telemedicine, remote learning.

---

#### **7. Online Gaming**

* **Function**: Interactive games over networks.
* **Protocols**: TCP/UDP depending on game requirements.
* **Usage**: Multiplayer games like PUBG, Fortnite, Call of Duty.

---

#### **8. Cloud Computing**

* **Function**: Provides scalable computing resources and storage via internet.
* **Services**:

  * **IaaS**: Infrastructure as a Service (e.g., AWS EC2).
  * **PaaS**: Platform as a Service (e.g., Google App Engine).
  * **SaaS**: Software as a Service (e.g., Gmail, Office365).
* **Protocols**: HTTPS, REST, SOAP.

---

#### **9. Social Networking**

* **Function**: Platform for user interaction and content sharing.
* **Examples**: Facebook, Twitter, Instagram, LinkedIn.
* **Protocols**: HTTP/HTTPS, APIs for data exchange.

---

#### **10. E-Commerce and Online Banking**

* **Function**: Buying, selling, and financial transactions online.
* **Security Protocols**: HTTPS, SSL/TLS, 2FA (Two-Factor Authentication).
* **Payment Gateways**: Use secure tokens and encrypted connections.

---

#### **11. Internet of Things (IoT)**

* **Function**: Connecting physical devices to collect and exchange data.
* **Examples**: Smart home devices, wearable tech, industrial sensors.
* **Protocols**: MQTT, CoAP, HTTP.

---

#### **12. Network Management**

* **Function**: Monitoring and maintaining network health and performance.
* **Protocols**: SNMP (Simple Network Management Protocol), ICMP (for ping/traceroute).
* **Usage**: Bandwidth monitoring, fault detection, configuration updates.

---

#### **13. Content Delivery Networks (CDN)**

* **Function**: Distribute content closer to users to reduce latency.
* **Examples**: Akamai, Cloudflare, Amazon CloudFront.
* **Usage**: Streaming services, high-traffic websites.

---

#### **14. Email Services**

* **Structure**:

  * **Mail User Agent (MUA)**: User interface (e.g., Thunderbird, Outlook).
  * **Mail Transfer Agent (MTA)**: Transfers emails (e.g., Postfix).
  * **Mail Delivery Agent (MDA)**: Delivers to recipient's mailbox.
* **Protocols**:

  * SMTP for sending.
  * POP3/IMAP for retrieving.

---
### **Network Hardware**

---

#### **1. Network Interface Card (NIC)**

* **Function**: Connects a computer to a network.
* **Types**:

  * **Wired NIC**: Uses Ethernet cable.
  * **Wireless NIC**: Uses Wi-Fi.
* **Features**:

  * Each NIC has a unique MAC (Media Access Control) address.
  * Supports data transmission and reception at hardware level.

---

#### **2. Hubs**

* **Function**: Broadcasts incoming data to all ports.
* **Characteristics**:

  * Operates at **OSI Layer 1 (Physical Layer)**.
  * No filtering or intelligence.
  * Causes network congestion due to broadcast nature.
* **Types**:

  * Passive Hub: No amplification of signal.
  * Active Hub: Amplifies signals before forwarding.

---

#### **3. Switches**

* **Function**: Connects devices within a LAN and forwards data based on MAC addresses.
* **Characteristics**:

  * Operates at **OSI Layer 2 (Data Link Layer)**.
  * Learns and stores MAC addresses in a MAC address table.
  * Provides full-duplex communication and reduces collisions.
  * Supports VLANs and port mirroring.
* **Advanced Types**:

  * Managed Switch: Configurable through software.
  * Unmanaged Switch: Plug-and-play device with no configuration.

---

#### **4. Bridges**

* **Function**: Connects and filters traffic between two network segments.
* **Characteristics**:

  * Operates at **OSI Layer 2**.
  * Uses MAC addresses to forward or filter frames.
  * Helps reduce collisions by dividing collision domains.
* **Types**:

  * Transparent Bridge.
  * Source Routing Bridge.

---

#### **5. Routers**

* **Function**: Connects multiple networks and routes data packets based on IP addresses.
* **Characteristics**:

  * Operates at **OSI Layer 3 (Network Layer)**.
  * Uses routing tables and routing algorithms (e.g., RIP, OSPF).
  * Connects LANs to WANs or the Internet.
* **Features**:

  * Supports NAT (Network Address Translation).
  * Firewall capabilities.
  * DHCP server functionalities.

---

#### **6. Gateways**

* **Function**: Acts as a protocol converter between different network architectures or data formats.
* **Characteristics**:

  * Operates across all **7 OSI layers**, especially Layer 7 (Application Layer).
  * Translates data between networks (e.g., email gateway, VoIP gateway).
* **Examples**:

  * Connecting TCP/IP network to a legacy system using non-IP protocols.

---

#### **7. Modems**

* **Function**: Modulates digital data into analog signals and demodulates analog signals into digital data.
* **Types**:

  * **DSL Modem**: Uses telephone lines.
  * **Cable Modem**: Uses coaxial cables from ISPs.
  * **Fiber Modem (ONT)**: For fiber optic connections.
* **Usage**: Provides Internet connectivity over various physical media.

---

#### **8. Access Points (AP)**

* **Function**: Provides wireless access to a wired network.
* **Characteristics**:

  * Operates at **Layer 2**.
  * Acts as a bridge between wireless and wired segments.
  * Supports multiple wireless clients using Wi-Fi standards (802.11a/b/g/n/ac/ax).
* **Modes**:

  * Root Mode (normal AP).
  * Repeater Mode (extends wireless coverage).

---

#### **9. Repeaters**

* **Function**: Regenerates and amplifies signals to extend the network range.
* **Characteristics**:

  * Operates at **OSI Layer 1**.
  * Used in both wired and wireless networks.
  * No filtering or addressing capability.

---

#### **10. Firewalls (Hardware-Based)**

* **Function**: Filters incoming and outgoing traffic based on predefined security rules.
* **Characteristics**:

  * Can be standalone hardware or integrated into routers.
  * Protects internal networks from external threats.
  * Implements packet filtering, stateful inspection, and proxy services.

---

#### **11. Transmission Media (Physical)**

* **Wired Media**:

  * **Twisted Pair Cable (UTP/STP)**: Used in Ethernet networks.
  * **Coaxial Cable**: Used in cable internet, older LANs.
  * **Fiber Optic Cable**: High-speed, long-distance, uses light signals.
* **Wireless Media**:

  * **Radio Waves**: Wi-Fi, Bluetooth.
  * **Microwaves**: Point-to-point communication.
  * **Infrared**: Short-range communication like TV remotes.

---

#### **12. Network Cables**

* **Ethernet Cables (Cat5, Cat6, Cat7)**:

  * Used in LANs for wired connectivity.
  * Differ in speed, shielding, and maximum transmission distance.
* **Fiber Optic Cables**:

  * Higher bandwidth and longer distances.
  * Immune to electromagnetic interference.

---
### **Network Software**

---

#### **1. Definition**

* Network software refers to the system and application programs that enable communication between devices over a network.
* It manages data transmission, error control, addressing, and protocol implementation.

---

#### **2. Protocols**

* **Definition**: A set of rules that define how data is transmitted and received across a network.
* **Types**:

  * **TCP (Transmission Control Protocol)**: Reliable, connection-oriented.
  * **UDP (User Datagram Protocol)**: Unreliable, connectionless.
  * **IP (Internet Protocol)**: Handles addressing and routing.
  * **HTTP/HTTPS (HyperText Transfer Protocol)**: Used for web communications.
  * **FTP (File Transfer Protocol)**: For file transfers.
  * **SMTP (Simple Mail Transfer Protocol)**: For email sending.
  * **DNS (Domain Name System)**: Resolves domain names to IP addresses.
  * **SNMP (Simple Network Management Protocol)**: Used for network management.

---

#### **3. Network Services**

* **File Sharing Services**: Allows users to access files on remote systems.
* **Email Services**: Manages sending, receiving, and storage of email.
* **Web Services**: Hosts websites and enables HTTP communication.
* **Directory Services**: Organizes and manages network resources (e.g., LDAP).
* **Authentication Services**: Validates user identity (e.g., RADIUS, Kerberos).
* **Remote Access Services**: Provides access to a remote machine (e.g., SSH, VPN).
* **DNS Services**: Resolves hostnames to IP addresses.

---

#### **4. Client-Server Model**

* **Client**:

  * Initiates a request.
  * Examples: Web browsers, email clients.
* **Server**:

  * Provides services to clients.
  * Examples: Web servers (Apache), email servers, database servers.
* **Communication**: Often follows a request-response pattern using standard protocols.

---

#### **5. Peer-to-Peer (P2P) Model**

* **Definition**: All devices (peers) act as both clients and servers.
* **Features**:

  * No central server.
  * Shared resources among all nodes.
* **Examples**: BitTorrent, blockchain nodes.

---

#### **6. Socket Programming**

* **Definition**: A way to enable communication between processes over a network.
* **Components**:

  * **IP Address**: Identifies the host.
  * **Port Number**: Identifies the application/service.
* **Types**:

  * **TCP Socket**: Reliable communication.
  * **UDP Socket**: Faster but unreliable.
* **Usage**: Chat applications, file transfers, HTTP clients.

---

#### **7. APIs for Network Programming**

* **Sockets API**: For low-level communication.
* **HTTP API**: For web-based interactions.
* **FTP Libraries**: To automate file transfers.
* **SNMP APIs**: For network monitoring tools.

---

#### **8. Protocol Stack Implementation**

* **OSI Model Implementation**:

  * Each layer is implemented using software components.
  * Data passes through each layer for encapsulation and processing.
* **TCP/IP Stack Implementation**:

  * Network interface layer interacts with physical hardware.
  * Internet layer manages addressing and routing.
  * Transport layer ensures reliable or fast communication.
  * Application layer implements user services (HTTP, FTP, SMTP).

---

#### **9. Operating System Network Modules**

* **Kernel Modules**: Handle low-level operations (e.g., IP stack, device drivers).
* **User Space Utilities**: Commands and applications (e.g., `ping`, `netstat`, `ssh`).
* **Firewall and Security Tools**: Manage traffic and security (e.g., `iptables`, `ufw`).

---

#### **10. Network Management Software**

* **Monitoring Tools**: Track traffic and performance (e.g., Nagios, Wireshark).
* **Configuration Tools**: Set up and manage devices (e.g., Cisco Packet Tracer).
* **Security Tools**: Detect threats and vulnerabilities (e.g., Snort, Nessus).
* **Traffic Analysis**: Analyze network flow and bandwidth usage.

---

#### **11. Virtual Network Software**

* **Virtual Switches**: Manage virtual network interfaces in hypervisors.
* **VPN Software**: Secure tunneling of traffic over public networks.
* **SDN Controllers**: Software Defined Networking allows centralized control of network devices.

---

#### **12. Middleware**

* **Definition**: Software that acts as a bridge between applications and network services.
* **Examples**:

  * Message brokers.
  * Database connectivity software.
  * RPC (Remote Procedure Call) frameworks.

---
### **Reference Models**

---

## **1. OSI Reference Model (Open Systems Interconnection)**

#### **Overview**

* Developed by **ISO (International Organization for Standardization)**.
* A **conceptual framework** that standardizes the functions of a telecommunication or computing system into **seven abstraction layers**.
* Each layer provides services to the layer above and receives services from the layer below.

---

#### **OSI Model Layers**

---

### **Layer 7 – Application Layer**

* **Function**: Provides interface between application software and network.
* **Examples**: HTTP, FTP, SMTP, DNS, Telnet.

---

### **Layer 6 – Presentation Layer**

* **Function**: Translates data between application and network formats.
* **Tasks**:

  * Data encryption/decryption.
  * Data compression.
  * Data translation (ASCII to EBCDIC).
* **Examples**: SSL/TLS, MIME encoding.

---

### **Layer 5 – Session Layer**

* **Function**: Establishes, manages, and terminates sessions.
* **Tasks**:

  * Session checkpointing and recovery.
  * Dialog control.
* **Examples**: NetBIOS, RPC.

---

### **Layer 4 – Transport Layer**

* **Function**: Provides reliable data transfer and flow control.
* **Tasks**:

  * Segmentation and reassembly.
  * Error detection and correction.
  * Flow control and congestion control.
* **Protocols**: TCP, UDP.

---

### **Layer 3 – Network Layer**

* **Function**: Determines physical path of data; handles logical addressing.
* **Tasks**:

  * Routing.
  * IP addressing.
  * Packet forwarding.
* **Protocols**: IP, ICMP, ARP, RIP, OSPF.

---

### **Layer 2 – Data Link Layer**

* **Function**: Error-free transfer of data frames between nodes.
* **Tasks**:

  * MAC addressing.
  * Error detection and correction.
  * Frame synchronization.
* **Protocols**: Ethernet, PPP, HDLC, Frame Relay.

---

### **Layer 1 – Physical Layer**

* **Function**: Transmission of raw bits over a physical medium.
* **Tasks**:

  * Defines electrical/optical characteristics.
  * Cable types, pin layouts.
  * Signal encoding, bit rate.
* **Examples**: RJ45, Ethernet cable, hubs.

---

#### **Key Characteristics**

| Feature       | OSI Model                                     |
| ------------- | --------------------------------------------- |
| Layers        | 7                                             |
| Development   | ISO                                           |
| Function      | Conceptual standard for network communication |
| Addressing    | MAC (Layer 2), IP (Layer 3), Port (Layer 4)   |
| Communication | Layer-to-layer service and interface          |

---

## **2. TCP/IP Reference Model (Transmission Control Protocol / Internet Protocol)**

#### **Overview**

* Developed by **DARPA** for the **ARPANET**.
* Practical model used in real-world networks including the **Internet**.
* Has **4 layers**, sometimes shown as 5 when split at physical and data link levels.

---

#### **TCP/IP Layers**

---

### **Layer 4 – Application Layer**

* **Function**: High-level protocols for end-user services.
* **Examples**: HTTP, FTP, SMTP, DNS, SNMP, Telnet.

---

### **Layer 3 – Transport Layer**

* **Function**: End-to-end communication and error recovery.
* **Protocols**:

  * TCP: Reliable, connection-oriented.
  * UDP: Unreliable, connectionless.

---

### **Layer 2 – Internet Layer**

* **Function**: Handles logical addressing and routing.
* **Protocols**: IP (IPv4, IPv6), ICMP, IGMP.

---

### **Layer 1 – Link Layer (Network Interface Layer)**

* **Function**: Manages physical transmission over medium.
* **Includes**:

  * Physical standards (Ethernet, Wi-Fi).
  * MAC addresses.
  * ARP for address resolution.

---

#### **Key Characteristics**

| Feature           | TCP/IP Model                               |
| ----------------- | ------------------------------------------ |
| Layers            | 4                                          |
| Development       | DARPA                                      |
| Function          | Practical implementation of networking     |
| Focus             | Inter-network communication and robustness |
| Protocol Standard | Used for Internet communication            |

---

## **3. Comparison: OSI vs TCP/IP**

| Feature               | OSI Model                                                                   | TCP/IP Model                           |
| --------------------- | --------------------------------------------------------------------------- | -------------------------------------- |
| Number of Layers      | 7                                                                           | 4                                      |
| Layer Names           | Physical, Data Link, Network, Transport, Session, Presentation, Application | Link, Internet, Transport, Application |
| Developed By          | ISO                                                                         | DARPA                                  |
| Protocol Independence | Protocol-independent                                                        | Protocol-specific (mainly IP)          |
| Usage                 | Theoretical reference                                                       | Widely used in practice                |
| Transport Layer       | Provides full reliability and flow control                                  | Offers both TCP and UDP                |
| Application Layer     | Split into 3 layers: Application, Presentation, Session                     | Single layer: Application              |

---

## **4. Importance of Reference Models**

* **Standardization**: Provides universal guidelines for developing networking systems.
* **Interoperability**: Ensures different systems and devices can communicate.
* **Modular Engineering**: Simplifies troubleshooting, development, and training.
* **Layer Isolation**: Each layer performs specific functions and communicates with adjacent layers only.

### **OSI (Open Systems Interconnection) Reference Model**

---

#### **1. Definition**

* OSI is a **7-layer conceptual framework** designed by **ISO (International Organization for Standardization)** to standardize network communications.
* It **divides communication tasks** into layers, with each layer performing a **specific role** in data transmission.

---

### **2. OSI Model Layers and Functions (Bottom to Top)**

---

#### **Layer 1: Physical Layer**

* **Purpose**: Transmission and reception of raw binary bits over a physical medium.
* **Functions**:

  * Defines electrical, mechanical, and procedural standards.
  * Converts bits into electrical/optical signals.
  * Manages cable types, voltage levels, and transmission rates.
* **Devices**: Hubs, repeaters, cables, connectors.
* **Protocols/Standards**: RS-232, DSL, USB, Ethernet (physical specs).

---

#### **Layer 2: Data Link Layer**

* **Purpose**: Provides **error-free** frame delivery between adjacent nodes.
* **Sub-layers**:

  * **LLC (Logical Link Control)**: Error checking and flow control.
  * **MAC (Media Access Control)**: Controls device access to physical medium.
* **Functions**:

  * Framing: Encapsulates network-layer packets into frames.
  * Error detection and correction.
  * MAC addressing and access control.
* **Devices**: Switches, bridges.
* **Protocols**: Ethernet, HDLC, PPP, Frame Relay.

---

#### **Layer 3: Network Layer**

* **Purpose**: Manages **routing and addressing** of packets across networks.
* **Functions**:

  * Logical addressing (IP addresses).
  * Routing and forwarding packets.
  * Fragmentation and reassembly of packets.
* **Devices**: Routers.
* **Protocols**: IP, ICMP, IGMP, RIP, OSPF.

---

#### **Layer 4: Transport Layer**

* **Purpose**: Ensures **reliable data transfer** and manages end-to-end communication.
* **Functions**:

  * Segmentation and reassembly.
  * Error detection, correction, and recovery.
  * Flow control and congestion control.
  * Multiplexing: Differentiating data streams by port numbers.
* **Protocols**: TCP (reliable), UDP (unreliable).

---

#### **Layer 5: Session Layer**

* **Purpose**: Establishes, manages, and terminates communication **sessions**.
* **Functions**:

  * Session establishment, maintenance, and termination.
  * Dialog control (half-duplex/full-duplex).
  * Synchronization via checkpoints.
* **Protocols/Examples**: NetBIOS, RPC, PPTP.

---

#### **Layer 6: Presentation Layer**

* **Purpose**: Ensures that data is in a **usable format** for the application layer.
* **Functions**:

  * Data translation (e.g., ASCII to EBCDIC).
  * Data compression.
  * Encryption and decryption for secure transmission.
* **Examples**: SSL/TLS, MIME (used in email).

---

#### **Layer 7: Application Layer**

* **Purpose**: Interface between **network services and user applications**.
* **Functions**:

  * Provides access to network for end-users.
  * Resource sharing and remote file access.
  * Email, file transfer, web browsing, etc.
* **Protocols**: HTTP, FTP, SMTP, POP3, SNMP, DNS.

---

### **3. OSI Layered Communication Process**

1. **Data Encapsulation**:

   * Each layer **adds its own header** to the data before passing it down.
   * Physical layer transmits the final binary signal.

2. **Data Decapsulation**:

   * On the receiving end, each layer **removes its header**, processes the data, and passes it up.

---

### **4. Advantages of OSI Model**

* **Modular design**: Easier to understand and troubleshoot.
* **Standardized interfaces**: Promotes interoperability.
* **Protocol independence**: Any protocol can be implemented at a layer.
* **Flexibility**: Allows for future upgrades at specific layers.

---

### **5. Summary Table**

| Layer | Name         | Data Unit | Functions                                | Devices      | Examples         |
| ----- | ------------ | --------- | ---------------------------------------- | ------------ | ---------------- |
| 7     | Application  | Data      | Network services to applications         | -            | HTTP, FTP, DNS   |
| 6     | Presentation | Data      | Translation, encryption, compression     | -            | SSL, JPEG, ASCII |
| 5     | Session      | Data      | Session setup and synchronization        | -            | RPC, NetBIOS     |
| 4     | Transport    | Segment   | Reliable delivery, error & flow control  | -            | TCP, UDP         |
| 3     | Network      | Packet    | Routing, logical addressing              | Routers      | IP, ICMP, OSPF   |
| 2     | Data Link    | Frame     | Framing, error detection, MAC addressing | Switches     | Ethernet, PPP    |
| 1     | Physical     | Bits      | Transmission of bits                     | Hubs, cables | DSL, USB, RJ45   |

---

### **TCP/IP Reference Model**

---

#### **1. Definition**

* **TCP/IP (Transmission Control Protocol/Internet Protocol)** is the **standard protocol suite** for communication across interconnected networks.
* Developed by **DARPA (Defense Advanced Research Projects Agency)** in the 1970s for **ARPANET**, the precursor to the Internet.
* Composed of **4 layers**, each corresponding to one or more layers of the OSI model.
* Focuses on **interoperability**, **reliability**, and **scalability** of networks.

---

### **2. Layers of the TCP/IP Model (Bottom to Top)**

---

### **Layer 1: Link Layer (Network Interface Layer)**

* **Purpose**: Handles physical transmission and media access control for local delivery.
* **Functions**:

  * Defines hardware addressing (MAC address).
  * Encapsulation of IP packets into frames.
  * Access to physical media (Ethernet, Wi-Fi, etc.).
* **Examples**:

  * Ethernet, Wi-Fi (IEEE 802.11), PPP, ARP (Address Resolution Protocol).

---

### **Layer 2: Internet Layer**

* **Purpose**: Responsible for **logical addressing and routing** of data across multiple networks.
* **Functions**:

  * Assigns logical IP addresses to devices.
  * Routes packets based on IP addresses.
  * Handles fragmentation and reassembly.
* **Key Protocols**:

  * **IP (Internet Protocol)**: Core protocol for packet delivery.

    * IPv4: 32-bit addressing.
    * IPv6: 128-bit addressing.
  * **ICMP (Internet Control Message Protocol)**: Error reporting and diagnostics (used by `ping`).
  * **IGMP (Internet Group Management Protocol)**: Manages multicast group memberships.

---

### **Layer 3: Transport Layer**

* **Purpose**: Provides **end-to-end communication**, flow control, error detection, and reliability.
* **Functions**:

  * Segments data from the application layer.
  * Assigns port numbers to differentiate applications.
  * Ensures reliable or fast data transfer based on protocol type.
* **Protocols**:

  * **TCP (Transmission Control Protocol)**:

    * Reliable, connection-oriented.
    * Three-way handshake, error checking, retransmission, congestion control.
  * **UDP (User Datagram Protocol)**:

    * Unreliable, connectionless.
    * Faster, used for real-time applications (e.g., VoIP, video streaming).

---

### **Layer 4: Application Layer**

* **Purpose**: Provides **services directly to user applications** for network communication.
* **Functions**:

  * Defines application-specific protocols.
  * Encodes and formats data for transmission.
* **Common Protocols**:

  * **HTTP/HTTPS**: Web communication.
  * **FTP**: File transfer.
  * **SMTP**: Sending email.
  * **POP3/IMAP**: Receiving email.
  * **DNS**: Resolves domain names to IP addresses.
  * **Telnet/SSH**: Remote access to systems.
  * **SNMP**: Network monitoring and management.

---

### **3. Summary Table of TCP/IP Layers**

| Layer       | OSI Equivalent                     | Functions                                      | Protocols/Examples        |
| ----------- | ---------------------------------- | ---------------------------------------------- | ------------------------- |
| Application | Application, Presentation, Session | End-user network services                      | HTTP, FTP, DNS, SMTP, SSH |
| Transport   | Transport                          | Reliable/fast data transfer, port addressing   | TCP, UDP                  |
| Internet    | Network                            | Routing, IP addressing, fragmentation          | IP, ICMP, IGMP, ARP       |
| Link        | Data Link, Physical                | Framing, MAC addressing, physical transmission | Ethernet, Wi-Fi, PPP      |

---

### **4. Key Characteristics of TCP/IP Model**

* **Protocol Suite**: Contains a complete set of communication protocols.
* **Inter-networking Capability**: Designed to connect different types of networks.
* **End-to-End Communication**: Ensures delivery from one device to another.
* **Hierarchical Addressing**: Uses IP addressing for logical location identification.
* **Port Numbers**: Used at transport layer to identify specific processes/services.

---

### **5. Differences: TCP/IP vs OSI Model**

| Feature                 | OSI Model                                   | TCP/IP Model                         |
| ----------------------- | ------------------------------------------- | ------------------------------------ |
| Number of Layers        | 7                                           | 4                                    |
| Development             | ISO (theoretical)                           | DARPA (practical)                    |
| Protocol Dependency     | Protocol-independent                        | Protocol-specific (e.g., TCP, IP)    |
| Application Layer Scope | Separate Session, Presentation, Application | All combined into one layer          |
| Usage                   | Educational, conceptual                     | Real-world implementation (Internet) |

---

### **6. Advantages of TCP/IP Model**

* Open and widely accepted standard.
* Highly scalable and robust.
* Supports connectionless and connection-oriented communication.
* Enables heterogeneous network interconnection.
* Protocols are simple and efficient for real-time data transmission.

---

### **Internet**

---

#### **1. Definition**

* The **Internet** is a **global network of interconnected computer networks** using the **TCP/IP protocol suite**.
* It enables **data exchange**, **communication**, and **resource sharing** among billions of devices worldwide.

---

#### **2. Components of the Internet**

* **Hosts (End Systems)**:

  * Devices like computers, smartphones, servers that use Internet services.
  * Identified by unique **IP addresses**.

* **Routers**:

  * Specialized hardware that forwards data between networks.
  * Operates at **Network Layer** of the TCP/IP model.

* **Transmission Media**:

  * Physical pathways like **fiber optics, copper cables**, or **wireless links** for data transmission.

* **ISPs (Internet Service Providers)**:

  * Organizations that provide Internet connectivity to end users and other networks.
  * Operate at various levels:

    * **Tier 1 ISP**: Global Internet backbone.
    * **Tier 2 ISP**: Regional.
    * **Tier 3 ISP**: Local, end-user access.

---

#### **3. Internet Protocols**

* **IP (Internet Protocol)**:

  * Logical addressing and routing.
  * Two versions: **IPv4 (32-bit)** and **IPv6 (128-bit)**.

* **TCP (Transmission Control Protocol)**:

  * Provides reliable, ordered, and error-checked delivery of data.

* **UDP (User Datagram Protocol)**:

  * Unreliable but faster; used in real-time applications like video calls.

* **DNS (Domain Name System)**:

  * Resolves human-readable domain names into IP addresses.

* **HTTP/HTTPS (HyperText Transfer Protocol)**:

  * Used for accessing and transmitting web content.

* **SMTP, POP3, IMAP**:

  * Email communication protocols.

---

#### **4. Addressing in the Internet**

* **IP Address**:

  * A unique identifier for every device on the Internet.
  * Format:

    * IPv4: `192.168.1.1` (4 bytes).
    * IPv6: `2001:0db8:85a3::8a2e:0370:7334` (16 bytes).

* **MAC Address**:

  * Hardware address of a network interface; used in LANs.

* **Port Numbers**:

  * Identify specific applications/services on a host.
  * Range:

    * 0–1023: Well-known ports (HTTP - 80, FTP - 21).
    * 1024–49151: Registered ports.
    * 49152–65535: Dynamic/private ports.

---

#### **5. Services Offered by the Internet**

* **Web Browsing**:

  * Accessing websites using protocols like HTTP/HTTPS.

* **Email**:

  * Sending/receiving messages using SMTP, POP3, IMAP.

* **File Transfer**:

  * Uploading/downloading files via FTP, SFTP, SCP.

* **VoIP and Video Conferencing**:

  * Real-time communication using RTP, SIP, WebRTC.

* **Remote Login**:

  * Accessing remote systems via SSH, Telnet.

* **Cloud Computing**:

  * On-demand computing resources accessed through the Internet.

* **Streaming Services**:

  * Delivering multimedia content using CDN and RTP.

---

#### **6. Domain Name System (DNS)**

* **Purpose**: Translates domain names to IP addresses.
* **Hierarchy**:

  * Root servers.
  * Top-Level Domains (TLDs): `.com`, `.org`, `.net`, etc.
  * Second-Level Domains: `google.com`, `example.org`.
* **Records**:

  * A Record: Maps domain to IPv4.
  * AAAA Record: Maps domain to IPv6.
  * MX Record: Mail exchange.

---

#### **7. Internet Architecture**

* **Client-Server Model**:

  * Clients request services (e.g., browsers), servers respond (e.g., web servers).

* **Peer-to-Peer Model**:

  * All nodes are equal, share resources (e.g., BitTorrent).

* **Backbone Network**:

  * High-capacity, long-distance lines connecting large networks.

---

#### **8. Accessing the Internet**

* **Dial-up**: Uses telephone lines, very slow.
* **DSL**: Digital signals over standard phone lines.
* **Cable**: Coaxial cable; faster than DSL.
* **Fiber**: High-speed internet via optical fiber.
* **Satellite**: Internet access in remote areas using satellites.
* **Mobile Data (3G/4G/5G)**: Wireless internet via cellular networks.
* **Wi-Fi**: Wireless local network for device access.

---

#### **9. Internet Governance**

* **ICANN**: Manages IP address allocation and domain name system.
* **IANA**: Allocates IP addresses and manages root zone.
* **IETF**: Develops Internet standards and protocols.
* **W3C**: Sets standards for the World Wide Web.

---

#### **10. Security Mechanisms on the Internet**

* **SSL/TLS**: Secures data transmission with encryption.
* **Firewalls**: Block unauthorized access to/from a network.
* **VPN (Virtual Private Network)**: Encrypts traffic between device and server.
* **Antivirus & Anti-malware**: Protects against malicious software.

---

#### **11. Applications of the Internet**

* E-commerce and online banking.
* Education and e-learning.
* Government services (e-governance).
* Social networking and communication.
* Online gaming and entertainment.

---
### **The Physical Layer (OSI Layer 1)**

---

#### **1. Definition**

* The **Physical Layer** is the **lowest layer** in the OSI model.
* Responsible for the **transmission and reception of raw binary bits** (0s and 1s) over a **physical transmission medium**.
* Concerned with **hardware-level** specifications, not logical addressing or error correction.

---

#### **2. Main Functions**

1. **Bit Transmission**

   * Converts digital data into electrical, optical, or radio signals.
   * Transmits raw bits without inspecting meaning or structure.

2. **Physical Topology**

   * Defines the physical arrangement of devices and cables.
   * Examples: Star, Bus, Ring, Mesh.

3. **Line Configuration**

   * Determines how devices are connected:

     * **Point-to-Point**: Single transmitter-receiver pair.
     * **Multipoint**: Multiple devices share a single medium.

4. **Data Rate (Transmission Rate)**

   * Specifies how many bits can be transmitted per second (bps).
   * Measured in bps, Kbps, Mbps, Gbps.

5. **Bit Synchronization**

   * Ensures sender and receiver are synchronized to correctly identify bit boundaries.

6. **Physical Characteristics of Interface**

   * Defines electrical/optical characteristics of interfaces (voltage, resistance, etc.).
   * Examples: RS-232, RJ45, USB.

7. **Transmission Mode**

   * **Simplex**: One direction only (e.g., keyboard to computer).
   * **Half-Duplex**: Both directions, but one at a time (e.g., walkie-talkie).
   * **Full-Duplex**: Simultaneous transmission (e.g., telephone).

8. **Encoding and Signaling**

   * Converts binary data into signals suitable for the medium.
   * Types:

     * **NRZ (Non-Return to Zero)**.
     * **Manchester Encoding**.
     * **4B/5B**, **8B/10B**.
   * Signal types:

     * Electrical (wired).
     * Optical (fiber optics).
     * Radio (wireless).

9. **Multiplexing**

   * Technique to share the medium among multiple signals.
   * Types:

     * **FDM** (Frequency Division Multiplexing).
     * **TDM** (Time Division Multiplexing).
     * **WDM** (Wavelength Division Multiplexing for optical fiber).

---

#### **3. Devices Operating at Physical Layer**

* **Hubs**: Regenerate and broadcast electrical signals.
* **Repeaters**: Amplify and retransmit signals to extend network range.
* **Cables and Connectors**: Physical media for transmission (e.g., RJ45 connectors, fiber-optic cables).
* **Network Interface Cards (NIC)**: Connect devices to network and convert digital signals.
* **Modems**: Convert digital signals to analog (modulation) and vice versa (demodulation).

---

#### **4. Transmission Media Types**

##### **A. Guided Media (Wired)**

1. **Twisted Pair Cable**

   * Consists of pairs of insulated copper wires twisted together.
   * Categories: Cat5, Cat6, Cat7 (differ in speed and shielding).
   * Common in LANs.

2. **Coaxial Cable**

   * Central copper conductor, surrounded by insulation, metallic shield, and outer cover.
   * Used for broadband internet and cable TV.

3. **Fiber Optic Cable**

   * Transmits light signals.
   * Immune to electromagnetic interference.
   * High bandwidth, long-distance transmission.

##### **B. Unguided Media (Wireless)**

1. **Radio Waves**

   * Used for Wi-Fi, FM radio, Bluetooth.
   * Can penetrate walls.

2. **Microwaves**

   * Line-of-sight communication.
   * Used in satellite and cellular communication.

3. **Infrared**

   * Short-range, line-of-sight communication (e.g., TV remotes).

---

#### **5. Important Physical Layer Concepts**

1. **Bandwidth**

   * Range of frequencies available for transmission.
   * Higher bandwidth allows faster data rates.

2. **Attenuation**

   * Loss of signal strength over distance.
   * Measured in decibels (dB).

3. **Noise**

   * Undesirable electrical signals interfering with transmission.
   * Types: Thermal, Crosstalk, Impulse.

4. **Latency**

   * Time taken for a signal to travel from source to destination.

5. **Propagation Delay**

   * Time taken for signal to physically propagate through medium.

6. **Jitter**

   * Variation in packet arrival times due to network congestion or poor synchronization.

---

#### **6. Summary Table**

| Feature               | Description                                                    |
| --------------------- | -------------------------------------------------------------- |
| Layer Number          | OSI Layer 1                                                    |
| Data Type Transmitted | Bits (0s and 1s)                                               |
| Devices               | Hub, Repeater, NIC, Modem                                      |
| Media Types           | Twisted Pair, Coaxial, Fiber, Radio, Microwave                 |
| Concerns              | Voltage levels, bit timing, signal type, connectors, bandwidth |
| Topologies Supported  | Bus, Ring, Star, Mesh                                          |
| Standards Examples    | IEEE 802.3 (Ethernet physical layer), RS-232, ITU V-series     |

---

### **Signals (in the Physical Layer)**

---

#### **1. Definition**

* A **signal** is an **electrical, optical, or electromagnetic wave** used to carry data from one device to another over a transmission medium.
* Signals are used in the **physical layer** to represent bits (0s and 1s) during transmission.

---

### **2. Types of Signals**

---

#### **A. Analog Signals**

* **Definition**: Continuous wave that varies in amplitude, frequency, or phase over time.

* **Characteristics**:

  * Infinite number of possible values.
  * Represented by **sine waves**.

* **Used In**:

  * Traditional telephone systems.
  * Radio and TV transmission.

* **Key Parameters**:

  * **Amplitude**: Height of the wave (signal strength).
  * **Frequency (f)**: Number of cycles per second (Hz).
  * **Phase (Φ)**: Position of wave relative to time zero.

---

#### **B. Digital Signals**

* **Definition**: Discrete waveforms that represent binary data (0 and 1).
* **Characteristics**:

  * Has only **two levels**: high (1) and low (0).
  * Represented by **square waves**.
* **Used In**:

  * Modern computer and data networks (Ethernet, USB).

---

### **3. Signal Representation**

| Bit | Digital Signal |
| --- | -------------- |
| 0   | Low voltage    |
| 1   | High voltage   |

| Signal Type | Representation |
| ----------- | -------------- |
| Analog      | Sine wave      |
| Digital     | Square wave    |

---

### **4. Periodic vs Aperiodic Signals**

* **Periodic Signal**:

  * Repeats pattern over time.
  * Example: Sine wave.
* **Aperiodic Signal**:

  * Does not repeat.
  * Example: Spoken voice or digital file transfer signal.

---

### **5. Characteristics of Analog Signal**

| Parameter  | Description                                      |
| ---------- | ------------------------------------------------ |
| Amplitude  | Maximum height of wave (voltage level)           |
| Frequency  | Number of cycles per second (Hz)                 |
| Phase      | Shift from the starting point in degrees/radians |
| Wavelength | Distance the signal travels during one cycle     |
| Bandwidth  | Range of frequencies the signal occupies         |

---

### **6. Characteristics of Digital Signal**

| Parameter      | Description                                    |
| -------------- | ---------------------------------------------- |
| Bit Rate       | Number of bits transmitted per second (bps)    |
| Bit Interval   | Time required to send one bit (1 / Bit rate)   |
| Voltage Levels | Defines binary values (e.g., 0 V = 0, 5 V = 1) |

---

### **7. Signal Impairments**

1. **Attenuation**

   * Loss of signal strength over distance.
   * Measured in decibels (dB).

2. **Noise**

   * Unwanted signal that distorts data transmission.
   * Types:

     * Thermal noise.
     * Crosstalk.
     * Impulse noise.

3. **Distortion**

   * Signal shape changes due to different propagation speeds of frequencies.

4. **Delay**

   * Time taken for a signal to propagate through medium.

---

### **8. Modulation Techniques**

**Used for converting digital/analog signals into transmittable waveforms:**

#### A. For Analog Signals (Carrier-based):

* **Amplitude Modulation (AM)**: Varies amplitude.
* **Frequency Modulation (FM)**: Varies frequency.
* **Phase Modulation (PM)**: Varies phase.

#### B. For Digital Signals:

* **ASK (Amplitude Shift Keying)**: 0 = low amplitude, 1 = high amplitude.
* **FSK (Frequency Shift Keying)**: 0 and 1 represented by different frequencies.
* **PSK (Phase Shift Keying)**: 0 and 1 represented by different phase angles.

---

### **9. Transmission of Signals**

1. **Baseband Transmission**

   * Digital signal sent directly over the medium.
   * Used in Ethernet (e.g., 100BASE-T).

2. **Broadband Transmission**

   * Analog signal modulated onto a carrier frequency.
   * Used in cable TV and DSL.

---

### **10. Encoding Techniques (Digital Data to Digital Signal)**

* **NRZ (Non-Return to Zero)**
* **Manchester Encoding**
* **4B/5B Encoding**
* **8B/10B Encoding**

These techniques ensure synchronization and signal integrity.

---

### **11. Summary Table**

| Property           | Analog Signal         | Digital Signal       |
| ------------------ | --------------------- | -------------------- |
| Value Range        | Continuous            | Discrete (0, 1)      |
| Representation     | Sine wave             | Square wave          |
| Transmission Media | Coaxial, Fiber, Radio | UTP, Fiber, Wireless |
| Used in            | Audio, video, TV      | Computer networks    |
| Susceptibility     | More to noise         | Less to noise        |

---

### **Transmission Impairment**

---

#### **1. Definition**

* **Transmission Impairment** refers to any **undesirable alteration of a signal** as it travels over a transmission medium.
* It results in **loss, distortion, or corruption** of data during communication.

---

### **2. Main Types of Transmission Impairments**

---

#### **A. Attenuation**

* **Definition**: Reduction in **signal strength** as it travels over distance.

* **Cause**: Energy loss due to resistance, absorption, scattering, etc.

* **Unit of Measurement**: **Decibels (dB)**

  $$
  \text{Attenuation (dB)} = 10 \times \log_{10} \left( \frac{P_{\text{in}}}{P_{\text{out}}} \right)
  $$

* **Example**:

  * If a signal starts at 100 mW and reaches the receiver at 10 mW:

    $$
    \text{Attenuation} = 10 \log_{10}(100/10) = 10 \log_{10}(10) = 10 \text{ dB}
    $$

* **Solution**: Use **amplifiers** or **repeaters** to boost signal strength.

---

#### **B. Distortion**

* **Definition**: Signal **changes its shape or form** during transmission.

* **Cause**: Different signal components (frequencies) **travel at different speeds**.

* **Occurs In**:

  * Guided media (copper cables, fiber).
  * Multi-frequency signals.

* **Effects**:

  * Misinterpretation of the received data.
  * Errors in decoding analog/digital waveforms.

* **Solution**: Use **equalization** and **bandwidth management**.

---

#### **C. Noise**

* **Definition**: **Unwanted electrical or electromagnetic energy** that interferes with signal transmission.
* **Cause**: External electromagnetic fields, hardware, other transmissions.

---

##### **Types of Noise**

1. **Thermal Noise (Johnson-Nyquist Noise)**

   * Caused by random motion of electrons in conductors.
   * Exists even in the absence of any external signal.
   * Formula:

     $$
     N = k \cdot T \cdot B
     $$

     Where:
     $k$ = Boltzmann's constant (1.38 × 10⁻²³ J/K)
     $T$ = Temperature (Kelvin)
     $B$ = Bandwidth (Hz)

2. **Induced Noise**

   * Caused by motors, fluorescent lights, transformers.
   * Inductive or capacitive coupling with the transmission line.

3. **Crosstalk**

   * Signal from one line interferes with another line.
   * Common in twisted pair cables.

4. **Impulse Noise**

   * Sudden, irregular spikes due to power line faults, lightning, switching.
   * Causes burst errors in digital systems.

---

### **3. Effects of Transmission Impairments**

| Impairment  | Effect on Signal                | Result              |
| ----------- | ------------------------------- | ------------------- |
| Attenuation | Weakened signal                 | Inability to detect |
| Distortion  | Misaligned frequency components | Bit errors, jitter  |
| Noise       | Signal alteration or corruption | Data corruption     |

---

### **4. Techniques to Reduce Transmission Impairments**

| Impairment  | Mitigation Techniques                        |
| ----------- | -------------------------------------------- |
| Attenuation | Amplifiers, repeaters, short cables          |
| Distortion  | Equalizers, distortion-correcting filters    |
| Noise       | Shielded cables, error correction, filtering |

---

### **5. Summary Table**

| Type        | Cause                                     | Effect                       | Solution                           |
| ----------- | ----------------------------------------- | ---------------------------- | ---------------------------------- |
| Attenuation | Signal energy loss over distance          | Weak signal, data loss       | Repeaters, amplifiers              |
| Distortion  | Unequal propagation speeds of frequencies | Altered waveform, bit errors | Equalization, bandwidth control    |
| Noise       | Electromagnetic interference, hardware    | Corrupted or lost bits       | Shielding, ECC, twisted pair cable |

---

### **Transmission**

---

#### **1. Definition**

* **Transmission** refers to the **process of sending data (bits)** from one device to another over a communication medium.
* It involves **encoding**, **modulating**, and **physically transferring** signals (analog or digital).

---

### **2. Types of Data Transmission**

---

#### **A. Serial Transmission**

* **Definition**: Bits are sent **one after another** over a single channel.
* **Advantages**:

  * Fewer wires.
  * Cheaper and simpler.
  * Less chance of interference.
* **Types**:

  * **Asynchronous**:

    * Data sent in small units with start/stop bits.
    * Used in keyboards, RS-232.
  * **Synchronous**:

    * Large blocks transmitted with timing synchronization.
    * Used in high-speed data transfers (e.g., USB, Ethernet).

---

#### **B. Parallel Transmission**

* **Definition**: **Multiple bits sent simultaneously** using multiple wires (1 wire per bit).
* **Advantages**:

  * Faster for short distances.
* **Disadvantages**:

  * Expensive due to more cables.
  * Signal skew and interference in long distances.

---

| Feature             | Serial Transmission | Parallel Transmission      |
| ------------------- | ------------------- | -------------------------- |
| Wires               | 1                   | Multiple                   |
| Speed (short range) | Slower              | Faster                     |
| Cost                | Low                 | High                       |
| Long Distance       | Efficient           | Not suitable (signal skew) |

---

### **3. Transmission Direction Modes**

---

#### **A. Simplex**

* **One-way communication** only.
* Example: Keyboard to CPU, monitor output.

#### **B. Half-Duplex**

* **Two-way communication**, but **one direction at a time**.
* Example: Walkie-talkies.

#### **C. Full-Duplex**

* **Two-way communication simultaneously**.
* Example: Telephones, modern computer networks.

---

| Mode        | Direction              | Example       |
| ----------- | ---------------------- | ------------- |
| Simplex     | One-way only           | TV Broadcast  |
| Half-Duplex | Two-way, one-at-a-time | Walkie-talkie |
| Full-Duplex | Two-way, simultaneous  | Telephone     |

---

### **4. Transmission Media Types**

---

#### **A. Guided Media (Wired)**

1. **Twisted Pair Cable**

   * Pairs of copper wires twisted to reduce interference.
   * Types:

     * **UTP (Unshielded Twisted Pair)**.
     * **STP (Shielded Twisted Pair)**.
   * Used in LANs, telephony.

2. **Coaxial Cable**

   * Single copper conductor with insulation and shielding.
   * Used in cable TV, Internet.

3. **Fiber Optic Cable**

   * Transmits data using light pulses.
   * High bandwidth and long distance.
   * Immune to EMI.

---

#### **B. Unguided Media (Wireless)**

1. **Radio Waves**

   * Omni-directional.
   * Used in Wi-Fi, FM radio.

2. **Microwaves**

   * Line-of-sight communication.
   * Used in satellites, mobile networks.

3. **Infrared**

   * Short-range, line-of-sight.
   * Used in remotes, some wireless peripherals.

---

| Media Type   | Examples            | Features                           |
| ------------ | ------------------- | ---------------------------------- |
| Twisted Pair | Ethernet cable      | Low cost, easy to install          |
| Coaxial      | Cable Internet/TV   | Better shielding, medium speed     |
| Fiber Optic  | Long-haul backbones | Very high speed, expensive         |
| Radio        | Wi-Fi, FM           | Wide coverage, lower security      |
| Microwave    | Cellular, satellite | Requires alignment, high bandwidth |
| Infrared     | TV remote           | Short range, line-of-sight         |

---

### **5. Baseband vs Broadband Transmission**

---

#### **Baseband Transmission**

* Sends **digital signals directly** over the medium.
* One signal at a time.
* Uses the entire bandwidth.
* Example: Ethernet.

#### **Broadband Transmission**

* Uses **modulation to transmit analog signals** over different frequency channels.
* Multiple signals simultaneously.
* Example: Cable TV.

---

| Type      | Signal Type | Number of Channels | Example  |
| --------- | ----------- | ------------------ | -------- |
| Baseband  | Digital     | Single             | Ethernet |
| Broadband | Analog      | Multiple           | Cable TV |

---

### **6. Transmission Rate**

* **Bit Rate**: Number of bits transmitted per second (bps).
* **Baud Rate**: Number of signal units transmitted per second.
* **Bandwidth**: Frequency range used to transmit the signal (measured in Hz).
* **Throughput**: Actual data rate achieved (depends on network conditions).
* **Latency**: Time delay from source to destination.

---

### **7. Summary Table**

| Aspect             | Serial         | Parallel         | Simplex           | Duplex (Half/Full)            |
| ------------------ | -------------- | ---------------- | ----------------- | ----------------------------- |
| Transmission Lines | 1              | Multiple         | One-way           | Two-way (one/both directions) |
| Speed              | Slower (short) | Faster (short)   | Limited           | Efficient communication       |
| Cost               | Low            | High             | Simple            | Complex                       |
| Applications       | USB, Ethernet  | Printers (older) | Keyboard, Monitor | Telephone, Walkie-Talkie      |

---

### **Serial Transmission**

---

#### **1. Definition**

* **Serial transmission** is a method of transmitting data where **bits are sent one after another** **sequentially over a single communication channel or wire**.
* It is the most commonly used form of data transmission in digital communication systems.

---

#### **2. Key Characteristics**

| Feature      | Description                                 |
| ------------ | ------------------------------------------- |
| Bit Transfer | 1 bit at a time                             |
| Wires Needed | Only one wire/channel for data              |
| Direction    | Can be simplex, half-duplex, or full-duplex |
| Speed        | Slower than parallel over short distances   |
| Cost         | Cheaper (fewer wires, less complexity)      |
| Range        | Suitable for long-distance communication    |

---

#### **3. Types of Serial Transmission**

---

##### **A. Asynchronous Serial Transmission**

* **Definition**: Data is sent **character-by-character** (usually 8 bits) with **start and stop bits** to indicate beginning and end.

* **Features**:

  * No common clock between sender and receiver.
  * Idle time between data units.
  * Start bit = 1 bit (usually 0).
  * Stop bit = 1 or 2 bits (usually 1).

* **Example**:

  * Data: `01000001` (ASCII 'A')
  * Transmitted as: `0 01000001 1` (start, data, stop)

* **Applications**:

  * Keyboards, serial ports (RS-232), modems.

---

##### **B. Synchronous Serial Transmission**

* **Definition**: Data is sent **as a continuous stream** of bits, synchronized using **a shared clock**.

* **Features**:

  * Higher speed than asynchronous.
  * Transmits blocks or frames of data.
  * Requires **clock synchronization** between sender and receiver.
  * Uses synchronization characters or signals to align data.

* **Applications**:

  * High-speed communication: Ethernet, USB, HDLC.

---

#### **4. Advantages of Serial Transmission**

1. **Cost-effective**:

   * Uses fewer wires, reducing cabling and cost.
2. **Simplified hardware**:

   * Easier to design and manage.
3. **Long-distance support**:

   * Less signal degradation over longer distances.
4. **Reduced crosstalk and EMI**:

   * Only one signal line, so less interference.

---

#### **5. Disadvantages of Serial Transmission**

1. **Slower than parallel (short range)**:

   * Since bits are sent one at a time.
2. **More complex protocols for timing**:

   * Especially in synchronous mode.

---

#### **6. Examples of Serial Transmission Standards**

| Standard | Description                                 | Type         |
| -------- | ------------------------------------------- | ------------ |
| RS-232   | Serial communication port standard          | Asynchronous |
| USB      | Universal Serial Bus                        | Synchronous  |
| I²C      | Inter-Integrated Circuit                    | Synchronous  |
| SPI      | Serial Peripheral Interface                 | Synchronous  |
| SATA     | Serial ATA (disk interface)                 | Synchronous  |
| UART     | Universal Asynchronous Receiver/Transmitter | Asynchronous |

---

#### **7. Serial vs Parallel Transmission**

| Aspect              | Serial Transmission    | Parallel Transmission          |
| ------------------- | ---------------------- | ------------------------------ |
| Data Sent           | One bit at a time      | Multiple bits at the same time |
| Number of Wires     | One                    | One per bit (e.g., 8 or 16)    |
| Cost                | Low                    | High                           |
| Distance            | Good for long distance | Short distance only            |
| Speed (short range) | Slower                 | Faster                         |
| Synchronization     | Easier                 | Complex                        |

---

#### **8. Applications of Serial Transmission**

* Communication between:

  * Microcontrollers and sensors.
  * Computers and peripherals (mouse, keyboard, printer).
  * Networking equipment (switches, routers).
* Data communication over:

  * USB, RS-232, SPI, I²C.
* Long-distance data links using fiber optics or satellite.

---

#### **9. Diagram: Asynchronous vs Synchronous Serial Transmission**

```
Asynchronous (with start and stop bits):
| Start | D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | Stop |
|   0   | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 1  |  1   |

Synchronous (no start/stop bits, uses clock sync):
| Sync Pattern | D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | ... |
```

---

#### **10. Summary Table**

| Parameter           | Serial Transmission       |
| ------------------- | ------------------------- |
| Bits sent at a time | 1                         |
| Cost                | Low                       |
| Speed (short range) | Lower than parallel       |
| Distance            | Better for long distances |
| Types               | Asynchronous, Synchronous |
| Applications        | USB, UART, I²C, Ethernet  |

---

### **Guided Transmission Media**

---

#### **1. Definition**

* **Guided Transmission Media** refers to **physical communication channels** through which signals are **guided or confined within a solid medium** such as cables or fibers.
* Also called **bounded media** because the signals travel along a specific path.

---

#### **2. Types of Guided Media**

---

### **A. Twisted Pair Cable**

---

##### **1. Structure**

* Consists of two insulated copper wires twisted together to reduce electromagnetic interference.

##### **2. Categories**

| Type   | Max Data Rate | Max Distance | Use Case            |
| ------ | ------------- | ------------ | ------------------- |
| Cat-3  | 10 Mbps       | 100 meters   | Telephone networks  |
| Cat-5  | 100 Mbps      | 100 meters   | Fast Ethernet       |
| Cat-5e | 1 Gbps        | 100 meters   | Gigabit Ethernet    |
| Cat-6  | 10 Gbps       | 55 meters    | High-speed Ethernet |

##### **3. Types**

* **Unshielded Twisted Pair (UTP)**:

  * No additional shielding.
  * Cheaper, commonly used in LANs.
* **Shielded Twisted Pair (STP)**:

  * Shielded with metallic foil to reduce noise.
  * Better noise resistance, more expensive.

##### **4. Advantages**

* Inexpensive.
* Easy to install and maintain.
* Suitable for short and medium distances.

##### **5. Disadvantages**

* Susceptible to electromagnetic interference (EMI).
* Limited bandwidth and distance compared to other media.

---

### **B. Coaxial Cable**

---

##### **1. Structure**

* A single central copper conductor, surrounded by:

  * Insulating layer.
  * Metallic shield (to prevent interference).
  * Outer insulating jacket.

##### **2. Types**

* **Baseband Coaxial**: Used for digital transmission.
* **Broadband Coaxial**: Used for analog transmission.

##### **3. Applications**

* Cable TV.
* Internet broadband.
* CCTV systems.

##### **4. Advantages**

* Better shielding than twisted pair.
* Higher bandwidth and transmission distance.

##### **5. Disadvantages**

* Thicker and less flexible.
* More expensive than twisted pair.

---

### **C. Fiber Optic Cable**

---

##### **1. Structure**

* Consists of:

  * **Core**: Thin strand of glass that carries light.
  * **Cladding**: Reflects light back into the core.
  * **Buffer coating and outer jacket**: Protection layers.

##### **2. Types**

* **Single-Mode Fiber (SMF)**:

  * Narrow core (\~9 µm).
  * Supports long-distance, high-speed communication.
  * Used in WAN, backbone links.
* **Multi-Mode Fiber (MMF)**:

  * Wide core (\~50–62.5 µm).
  * Used for shorter distances (e.g., within buildings).

##### **3. Transmission**

* Uses light signals (infrared or laser).
* Operates at high frequencies (100s of THz).

##### **4. Advantages**

* **Very high bandwidth**.
* **Low attenuation** and **resistance to EMI**.
* **Secure** (difficult to tap).

##### **5. Disadvantages**

* Expensive and delicate.
* Requires special equipment for installation and repair.

---

#### **3. Comparison Table**

| Feature          | Twisted Pair            | Coaxial Cable         | Fiber Optic Cable      |
| ---------------- | ----------------------- | --------------------- | ---------------------- |
| Medium           | Copper wires            | Copper with shielding | Glass or plastic fiber |
| Bandwidth        | Low to Medium           | Medium                | Very High              |
| Cost             | Low                     | Medium                | High                   |
| Distance         | Short                   | Medium                | Very Long              |
| Noise Resistance | Low (UTP), Medium (STP) | High                  | Very High              |
| Data Rate        | Up to 10 Gbps (Cat-6)   | Up to 100 Mbps+       | 1 Tbps+                |
| Installation     | Easy                    | Moderate              | Difficult (fragile)    |
| EMI Immunity     | Low (UTP)               | High                  | Very High              |

---

#### **4. Applications of Guided Media**

| Media Type        | Applications                                         |
| ----------------- | ---------------------------------------------------- |
| Twisted Pair      | LANs, telephones, DSL connections                    |
| Coaxial Cable     | Cable TV, Internet access, video surveillance (CCTV) |
| Fiber Optic Cable | Long-distance communication, Internet backbone, ISPs |

---

#### **5. Summary**

* Guided media provide a **controlled environment** for signal transmission.
* **Twisted pair** is ideal for LANs and short-distance setups.
* **Coaxial cable** supports better shielding and is common in broadcasting.
* **Fiber optics** offer **maximum speed, bandwidth, and distance**, but at **higher cost** and complexity.

---

### **Wireless Transmission**

---

#### **1. Definition**

* **Wireless transmission** refers to the **transfer of data or signals over a distance without using physical conductors** (like cables or wires).
* It uses **electromagnetic waves** (radio, microwave, infrared) to transmit signals through the **air or vacuum**.

---

### **2. Key Characteristics**

| Feature            | Description                                |
| ------------------ | ------------------------------------------ |
| Medium             | Unguided (air, space)                      |
| Signal Types       | Electromagnetic waves                      |
| Directionality     | Omni-directional or uni-directional        |
| Common Frequencies | 3 kHz to 300 GHz                           |
| Use Cases          | Mobile phones, Wi-Fi, satellite, Bluetooth |

---

### **3. Types of Wireless Transmission**

---

#### **A. Radio Waves**

* **Frequency Range**: 3 kHz – 1 GHz
* **Wavelength**: Longest among all wireless types.
* **Properties**:

  * Omni-directional.
  * Can penetrate walls.
  * Suitable for long-distance transmission.
* **Applications**:

  * AM/FM radio.
  * Television broadcasts.
  * Wi-Fi (2.4 GHz band).
  * Cordless phones.

---

#### **B. Microwaves**

* **Frequency Range**: 1 GHz – 300 GHz
* **Wavelength**: Shorter than radio waves.
* **Properties**:

  * Requires **line-of-sight** communication.
  * Cannot penetrate solid obstacles.
  * Used for **point-to-point links**.
* **Applications**:

  * Satellite communication.
  * Cellular networks (4G/5G).
  * Microwave ovens.
  * Wi-Fi (5 GHz band).

---

#### **C. Infrared (IR)**

* **Frequency Range**: 300 GHz – 400 THz
* **Wavelength**: Short-range.
* **Properties**:

  * Requires **line-of-sight**.
  * Cannot penetrate walls.
  * Safe, low power, and used for **device-to-device** transmission.
* **Applications**:

  * Remote controls (TV, AC).
  * Wireless mouse/keyboards.
  * Short-range file transfer between phones (older systems).

---

#### **D. Light Transmission (Visible/Lasers)**

* **Medium**: Uses focused light beams.
* **Properties**:

  * Requires **clear, unobstructed path** (line-of-sight).
  * Highly directional.
* **Applications**:

  * Laser communication.
  * Optical wireless communication (free-space optics, FSO).

---

### **4. Wireless Transmission Techniques**

| Technique                  | Description                                       |
| -------------------------- | ------------------------------------------------- |
| **Broadcast**              | Signal sent in all directions (e.g., radio, TV)   |
| **Point-to-Point**         | Direct communication between two antennas/devices |
| **Satellite Transmission** | Uses geostationary or low-earth orbit satellites  |

---

### **5. Wireless Transmission Frequencies**

| Band             | Frequency Range | Usage Example                   |
| ---------------- | --------------- | ------------------------------- |
| VLF/LF/MF        | < 3 MHz         | AM radio                        |
| HF/VHF/UHF       | 3 – 300 MHz     | FM radio, TV, land-mobile radio |
| SHF (Microwave)  | 3 – 30 GHz      | Wi-Fi, radar, satellite         |
| EHF (Millimeter) | 30 – 300 GHz    | 5G, short-range high-speed data |

---

### **6. Advantages of Wireless Transmission**

1. **Mobility**:

   * Devices can move freely within coverage area.
2. **Flexibility**:

   * Easy to install and expand (no cables).
3. **Cost-Effective for Long Distances**:

   * Especially in difficult terrains (mountains, oceans).
4. **Support for Broadcasting**:

   * Useful for one-to-many communication like radio/TV.

---

### **7. Disadvantages of Wireless Transmission**

1. **Interference**:

   * Signals may overlap or interfere with other devices.
2. **Limited Bandwidth**:

   * Shared frequency spectrum among many users.
3. **Security Risks**:

   * Easier to intercept compared to guided media.
4. **Signal Attenuation**:

   * Absorption, reflection, or scattering reduce signal strength.
5. **Line-of-Sight Requirement** (microwave/infrared):

   * Obstruction degrades or blocks signal.

---

### **8. Wireless Transmission Technologies**

| Technology       | Description                                  | Used In                              |
| ---------------- | -------------------------------------------- | ------------------------------------ |
| Wi-Fi            | Wireless LAN standard (IEEE 802.11)          | Home/Office networking               |
| Bluetooth        | Short-range communication (IEEE 802.15.1)    | Headphones, input devices            |
| Zigbee           | Low-power mesh communication (IEEE 802.15.4) | IoT and smart home devices           |
| NFC              | Very short range, high frequency             | Contactless payments, device pairing |
| Cellular (2G-5G) | Mobile network generations                   | Voice, SMS, mobile internet          |
| Satellite        | Uses geostationary satellites                | TV, GPS, global internet coverage    |

---

### **9. Summary Table**

| Medium      | Frequency         | Range       | Directionality     | Used In                       |
| ----------- | ----------------- | ----------- | ------------------ | ----------------------------- |
| Radio Waves | 3 kHz – 1 GHz     | Long        | Omni-directional   | FM/AM radio, Wi-Fi (2.4 GHz)  |
| Microwaves  | 1 – 300 GHz       | Medium/Long | Uni-directional    | Cellular, satellite, 5G       |
| Infrared    | 300 GHz – 400 THz | Short       | Line-of-sight      | Remotes, wireless peripherals |
| Light/Laser | Visible/Infrared  | Short       | Highly directional | Optical wireless, laser comms |

---

### **The Public Switched Telephone Network (PSTN)**

---

#### **1. Definition**

* The **Public Switched Telephone Network (PSTN)** is the **worldwide circuit-switched telephone system** used for **traditional voice communication**.
* Also known as **Plain Old Telephone Service (POTS)**.
* It is a **global system** of interconnected **telecommunication networks** operated by governments and private companies.

---

### **2. Key Features**

| Feature         | Description                                                 |
| --------------- | ----------------------------------------------------------- |
| Type            | Circuit-switched network                                    |
| Primary Use     | Voice communication                                         |
| Medium          | Copper wires, fiber optics, microwave, satellite            |
| Signaling       | Uses analog and digital signals                             |
| Switching       | Manual (older), electromechanical, and electronic switching |
| Standardization | ITU-T (International Telecommunication Union - Telephony)   |

---

### **3. Structure and Components**

---

#### **A. Local Loop**

* The **physical connection** between the subscriber (user's phone) and the local telephone exchange.
* Typically **twisted pair copper wire**.
* Carries analog voice signals.

---

#### **B. Central Office (CO) / Local Exchange**

* A switching facility that connects calls from local users.
* Routes local calls and forwards non-local calls to higher-level switches.

---

#### **C. Tandem Switch / Toll Office**

* Intermediary exchange between central offices.
* Handles **long-distance** call routing within the same region or country.

---

#### **D. International Gateway**

* Facilitates international call routing via satellite, undersea cables, or fiber optics.
* Connects national networks to the **international telephone network**.

---

#### **E. Transmission Media**

1. **Twisted Pair Cable** – for local loops.
2. **Coaxial Cable** – for trunk lines (older networks).
3. **Fiber Optics** – modern high-speed core backbone.
4. **Microwave Links/Satellite** – for remote and long-distance connections.

---

### **4. PSTN Signaling System**

---

#### **A. In-Band Signaling**

* Control signals (dial tones, call setup) share the same channel as voice.
* Used in analog systems.

#### **B. Out-of-Band Signaling**

* Control signals transmitted over a **separate** channel (e.g., SS7 protocol).
* More secure and reliable.

---

### **5. Call Setup and Process**

1. **User dials** a number via telephone.
2. Local exchange receives digits and **determines routing**.
3. If the destination is:

   * **Local** → Connects directly.
   * **Non-local** → Routes to tandem or toll office.
4. Circuit is established **end-to-end** (circuit switching).
5. **Voice communication begins** over the dedicated path.
6. **Call teardown** occurs after termination to release the circuit.

---

### **6. Circuit Switching in PSTN**

* PSTN uses **circuit switching**, which means:

  * A **dedicated physical path** is established between caller and receiver.
  * The entire bandwidth is reserved for the **duration of the call**.
  * Offers **constant delay and quality** but **inefficient** use of resources during silence.

---

### **7. Evolution of PSTN**

| Phase               | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| Analog PSTN         | Initially analog lines and manual switching.                 |
| Digital PSTN (ISDN) | Introduction of Integrated Services Digital Network.         |
| VoIP Integration    | PSTN-to-IP telephony gateways.                               |
| Transition to NGN   | Modern migration toward all-IP **Next Generation Networks**. |

---

### **8. Advantages of PSTN**

1. **Wide Coverage**: Global infrastructure.
2. **Reliable Voice Quality**: Due to dedicated circuit paths.
3. **Power through line**: Old phones receive power from the network.
4. **Proven Technology**: Used and trusted for over a century.

---

### **9. Disadvantages of PSTN**

1. **Inefficient Resource Use**: Circuit switching occupies full path during the call.
2. **Poor Support for Data**: Limited bandwidth for modern internet use.
3. **High Cost for Long-Distance Calls**.
4. **Limited Scalability and Flexibility**.

---

### **10. PSTN vs VoIP (Modern Alternative)**

| Feature        | PSTN                             | VoIP                   |
| -------------- | -------------------------------- | ---------------------- |
| Technology     | Circuit-switched                 | Packet-switched (IP)   |
| Transmission   | Analog/Digital over copper/fiber | Digital over internet  |
| Cost           | High (especially long distance)  | Low                    |
| Infrastructure | Legacy and dedicated             | Uses existing internet |
| Scalability    | Difficult                        | Easy                   |

---

### **11. Summary Table**

| Component             | Function                                    |
| --------------------- | ------------------------------------------- |
| Local Loop            | Connects subscriber to local exchange       |
| Central Office        | Local call switching                        |
| Tandem Switch         | Regional long-distance routing              |
| International Gateway | Connects national PSTNs globally            |
| Transmission Media    | Carries signals (twisted pair, fiber, etc.) |

---

### **Mobile Telephone System**

---

#### **1. Definition**

* A **Mobile Telephone System** is a **wireless communication system** that allows users to make **voice calls, send messages**, and **access data services** over a **cellular network** while moving between locations.
* It uses **radio waves** and **cellular architecture** to provide continuous and reliable mobile communication.

---

### **2. Key Characteristics**

| Feature               | Description                                            |
| --------------------- | ------------------------------------------------------ |
| Mobility              | Supports user movement without interrupting connection |
| Wireless Transmission | Uses radio frequency (RF) spectrum                     |
| Network Architecture  | Divided into small regions called **cells**            |
| Switching             | Uses circuit and packet switching                      |
| Frequency Reuse       | Allows same frequency in non-adjacent cells            |

---

### **3. Cellular System Architecture**

---

#### **A. Cell**

* A geographical area covered by a single base station.
* Cells are **hexagonally shaped** for theoretical modeling.
* Each cell uses **a set of frequencies** distinct from adjacent cells.

---

#### **B. Base Transceiver Station (BTS)**

* Located in every cell.
* Handles radio communication between **mobile users and the network**.
* Consists of antennas, transceivers, and control units.

---

#### **C. Base Station Controller (BSC)**

* Manages multiple BTSs.
* Handles **handover**, **frequency assignment**, and **power control**.

---

#### **D. Mobile Switching Center (MSC)**

* Central component for **call routing and switching**.
* Connects mobile network to **PSTN** and **other mobile networks**.
* Maintains databases like HLR (Home Location Register) and VLR (Visitor Location Register).

---

#### **E. Mobile Station (MS)**

* The **mobile device** (phone or tablet) used by the end-user.
* Contains:

  * **Transceiver**: Communicates with BTS.
  * **SIM card**: Stores user and network info.

---

### **4. Frequency Reuse**

* **Cells use different frequency sets** to avoid interference.
* The same frequency can be reused in **non-adjacent cells**.
* Increases spectrum efficiency.

---

### **5. Handover (Handoff)**

* **Process of transferring** an active call or data session from one BTS to another as the user moves.
* Two types:

  * **Hard Handoff**: Old connection is broken before new one is made.
  * **Soft Handoff**: New connection is made before breaking the old one (used in CDMA).

---

### **6. Generations of Mobile Communication**

---

| Generation | Name           | Features                                        |
| ---------- | -------------- | ----------------------------------------------- |
| 1G         | Analog         | Voice only, poor quality, insecure              |
| 2G         | GSM/CDMA       | Digital voice, SMS, limited data (GPRS, EDGE)   |
| 3G         | UMTS/WCDMA     | Higher data rates, mobile internet, video calls |
| 4G         | LTE            | High-speed data, VoIP, HD video streaming       |
| 5G         | NR (New Radio) | Ultra-high speed, low latency, IoT support      |

---

### **7. Components of Mobile Telephony**

| Component                             | Function                                               |
| ------------------------------------- | ------------------------------------------------------ |
| **SIM Card**                          | Stores subscriber identity (IMSI), authentication info |
| **IMEI**                              | Unique ID for the mobile device                        |
| **HLR (Home Location Register)**      | Stores user information permanently                    |
| **VLR (Visitor Location Register)**   | Temporarily stores info of roaming users               |
| **AuC (Authentication Center)**       | Provides authentication and encryption                 |
| **EIR (Equipment Identity Register)** | Stores IMEI of allowed/blocked devices                 |

---

### **8. Services Provided**

* **Voice calls**
* **SMS (Short Message Service)**
* **MMS (Multimedia Messaging)**
* **Mobile Internet**
* **VoLTE (Voice over LTE)**
* **Emergency and location-based services**

---

### **9. Advantages of Mobile Telephone System**

1. **Mobility**: Enables communication on the move.
2. **Wide Coverage**: Global roaming and access.
3. **Multiple Services**: Data, voice, video, messaging.
4. **Ease of Use**: Portable and user-friendly.
5. **Scalability**: Easy to add users or extend coverage.

---

### **10. Disadvantages**

1. **Signal Interference**: From physical obstacles or frequency overlap.
2. **Limited Bandwidth**: Especially in dense urban areas.
3. **Battery Dependency**: Constant power required.
4. **Security Risks**: Susceptible to eavesdropping and tracking.
5. **Radiation Exposure**: Long-term health concerns (still debated).

---

### **11. Summary Table**

| Component           | Role                                       |
| ------------------- | ------------------------------------------ |
| MS (Mobile Station) | User device                                |
| BTS                 | Wireless communication with mobile devices |
| BSC                 | Manages BTS, handovers                     |
| MSC                 | Routing, switching, connects to PSTN       |
| HLR/VLR             | User location and subscription information |
| SIM                 | Stores IMSI and authentication keys        |

---


