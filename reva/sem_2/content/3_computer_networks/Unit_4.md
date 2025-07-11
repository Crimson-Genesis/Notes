# Unit - 4 -> Transport layer and the application layer
Transport service, elements of transport protocl, Simple Transport Protocal, Internet Transport layer protocals: UDP and TCP.
Domain name system, electronic mail, World Wide Web: architectural overview, dynamic web document and http.

Application Layer Protocals: Simple Network Mangement Protocol, File Transfer Protocol, Simple Mail Transfer Protocol.

## Content ->
### **Transport Service (in the Transport Layer)**

---

### **1. Definition**

* A **Transport Service** provides **end-to-end communication** between **processes (applications)** running on different **hosts**.
* It offers **reliable or unreliable** data transfer over the **unreliable network layer**.
* Acts as an interface between the **application layer** and the **network layer**.

---

### **2. Goals of Transport Service**

| Goal                            | Description                                                            |
| ------------------------------- | ---------------------------------------------------------------------- |
| **Process-to-process delivery** | Enables communication between software applications (not just devices) |
| **Reliability**                 | Ensures error-free, ordered, and complete data delivery                |
| **Efficiency**                  | Manages congestion, flow control, and multiplexing                     |
| **Transparency**                | Hides underlying network complexity from applications                  |

---

### **3. Types of Transport Services**

| Service Type            | Description                                                              | Example Protocol |
| ----------------------- | ------------------------------------------------------------------------ | ---------------- |
| **Reliable service**    | Ensures data is delivered **completely, without loss**, and **in order** | TCP              |
| **Unreliable service**  | No delivery guarantees; faster and lightweight                           | UDP              |
| **Connection-oriented** | Establishes a session (handshake) before data transfer                   | TCP              |
| **Connectionless**      | No setup phase; data sent as independent packets                         | UDP              |
| **Full-duplex**         | Allows simultaneous 2-way communication                                  | TCP              |
| **Multiplexed**         | Supports multiple concurrent applications on one host                    | TCP, UDP         |

---

### **4. Key Features Provided by Transport Services**

---

#### **1. Reliable Data Transfer**

* Uses mechanisms like:

  * **Acknowledgments (ACKs)**
  * **Checksums**
  * **Timers and retransmission**
* Ensures data arrives **accurately and in order**.

---

#### **2. Flow Control**

* Prevents the **sender from overwhelming the receiver**.
* Receiver tells sender how much data it can accept.
* Implemented in **TCP (Window-based)**.

---

#### **3. Congestion Control**

* Prevents **network overload** by adjusting transmission rate.
* Based on **feedback from the network** (e.g., packet loss, delay).
* TCP uses:

  * **Slow Start**
  * **Congestion Avoidance**
  * **Fast Retransmit**
  * **Fast Recovery**

---

#### **4. Multiplexing and Demultiplexing**

* **Multiplexing**:

  * Allows multiple application processes to use the transport layer.
  * Adds **port numbers** to identify each session.

* **Demultiplexing**:

  * Delivers incoming segments to the correct application using port numbers.

---

#### **5. Error Detection and Correction**

* Ensures data integrity using:

  * **Checksums**
  * **Automatic Repeat reQuest (ARQ)**

---

#### **6. Sequencing**

* Ensures that **packets are reassembled in the correct order** at the receiver.
* Important for **stream-oriented** communication (e.g., file transfer, HTTP).

---

### **5. Addressing: Ports**

| Concept         | Description                                                                |
| --------------- | -------------------------------------------------------------------------- |
| **Port Number** | Logical address assigned to each application                               |
| **Range**       | 0–65535 (Well-known: 0–1023, Registered: 1024–49151, Dynamic: 49152–65535) |

Example:

* HTTP: port 80
* FTP: port 21
* DNS: port 53
* SMTP: port 25

---

### **6. Relationship with Network Layer**

| Layer               | Function                                                    |
| ------------------- | ----------------------------------------------------------- |
| **Network Layer**   | Delivers packets between hosts (host-to-host)               |
| **Transport Layer** | Delivers segments between applications (process-to-process) |

---

### **7. Summary Table**

| Feature                     | Transport Service Description                   |
| --------------------------- | ----------------------------------------------- |
| Communication Type          | Process-to-process                              |
| Protocols Involved          | TCP, UDP                                        |
| Connection Types            | Connection-oriented (TCP), Connectionless (UDP) |
| Reliability                 | Optional (TCP: reliable, UDP: unreliable)       |
| Flow and Congestion Control | Supported in TCP                                |
| Error Handling              | Checksums, ACKs, Retransmissions                |
| Port-based Multiplexing     | Port numbers identify specific processes        |

---

### **Elements of Transport Protocol**

---

### **1. Definition**

* A **Transport Protocol** defines the **rules and mechanisms** used for **reliable or unreliable delivery** of data **between processes** across networked hosts.
* The **elements of a transport protocol** refer to the **fundamental components** that support **end-to-end communication**.

---

### **2. Major Elements of a Transport Protocol**

---

### **1. Addressing (Port Numbers)**

* Identifies the **specific application process** on a host.
* Transport layer uses:

  * **IP address** (host identification)
  * **Port number** (process identification)
* Enables **multiplexing** (multiple apps sharing network) and **demultiplexing** (routing data to correct app).

| Type             | Range         |
| ---------------- | ------------- |
| Well-known ports | 0 – 1023      |
| Registered ports | 1024 – 49151  |
| Dynamic ports    | 49152 – 65535 |

---

### **2. Connection Establishment and Release**

* **Connection-Oriented Protocols (e.g., TCP)**:

  * Use a **handshake mechanism** before data transfer.
  * **Three-way handshake** in TCP:

    1. SYN → from sender
    2. SYN-ACK → from receiver
    3. ACK → from sender

* **Connection Termination**:

  * Graceful termination using **FIN/ACK** process.
  * Ensures both sides close the connection reliably.

---

### **3. Flow Control**

* Controls **data transmission rate** so that the **receiver is not overwhelmed**.
* Mechanism:

  * **Sliding window protocol**
  * **Receiver window size** advertised to sender
* Used by **TCP**, not by **UDP**.

---

### **4. Error Control**

* Ensures **data integrity** by detecting and correcting errors.
* Involves:

  * **Checksums** to detect bit errors
  * **Acknowledgments (ACKs)** to confirm receipt
  * **Negative Acknowledgments (NAKs)** for requesting retransmission
  * **Timeout and retransmission** if ACK not received

---

### **5. Congestion Control**

* Prevents excessive traffic from **overloading the network**.
* TCP uses:

  * **Slow start**
  * **Congestion avoidance**
  * **Fast retransmit**
  * **Fast recovery**
* Adjusts **window size** and **sending rate** dynamically.

---

### **6. Multiplexing and Demultiplexing**

* **Multiplexing**:

  * Multiple applications share the same network connection.
  * Data from different processes is **tagged with port numbers**.

* **Demultiplexing**:

  * Incoming data is delivered to the correct application based on the port number.

---

### **7. Data Transfer Mechanisms**

| Mechanism            | Description                                      |
| -------------------- | ------------------------------------------------ |
| **Byte stream**      | Continuous flow of data without boundaries (TCP) |
| **Message-oriented** | Data sent in individual messages (UDP)           |

---

### **8. Fragmentation and Reassembly**

* Some transport protocols support **breaking large messages** into smaller segments.
* Each segment is:

  * **Numbered (Sequence Number)**
  * **Reassembled** at the receiver in the correct order

---

### **9. Sequencing**

* Maintains correct **order of packets** during reassembly.
* **Sequence numbers** are used in TCP to order segments.
* Important in case of **out-of-order delivery**.

---

### **10. Acknowledgment Strategy**

| Type of Acknowledgment | Description                                |
| ---------------------- | ------------------------------------------ |
| **Positive ACK**       | Confirms receipt of segment                |
| **Negative ACK (NAK)** | Requests retransmission of missing segment |
| **Cumulative ACK**     | ACKs all segments up to a certain number   |
| **Selective ACK**      | ACKs only specific received segments       |

---

### **11. Timer Management**

* Uses **timers** to:

  * **Detect lost packets**
  * **Trigger retransmissions**
  * **Measure Round Trip Time (RTT)**

* Retransmission timeout (RTO) is based on:

  * Estimated RTT
  * RTT variance

---

### **12. Data Integrity Mechanism**

* **Checksum** is computed on data + header:

  * Sent with each segment
  * Receiver computes and compares with original
  * If mismatch → segment is considered **corrupted**

---

### **13. Urgent Data Handling**

* TCP supports an **"urgent pointer"**:

  * Marks urgent data that should be processed immediately.
  * Used in control scenarios (e.g., breaking a remote shell).

---

### **14. Quality of Service (QoS) Support (Optional)**

* Some protocols (or extensions) support:

  * **Priority marking**
  * **Bandwidth reservation**
  * **Latency control**

---

### **3. Summary Table of Elements**

| Element                     | Function                                                  |
| --------------------------- | --------------------------------------------------------- |
| Addressing                  | Identifies application processes via port numbers         |
| Connection Establishment    | Sets up communication path (e.g., 3-way handshake in TCP) |
| Connection Release          | Graceful shutdown using FIN and ACK                       |
| Flow Control                | Prevents overwhelming the receiver                        |
| Error Control               | Detects/corrects data corruption                          |
| Congestion Control          | Prevents network congestion                               |
| Multiplexing/Demultiplexing | Supports multiple app sessions per host                   |
| Fragmentation/Reassembly    | Handles splitting and rejoining large messages            |
| Sequencing                  | Maintains order of received data                          |
| Acknowledgment Strategy     | Confirms receipt of packets                               |
| Timer Management            | Manages retransmission timing and timeout                 |
| Data Integrity              | Ensures correct data delivery using checksums             |
| Urgent Data                 | Allows delivery of time-critical control data             |
| QoS (optional)              | Supports performance guarantees in advanced protocols     |

---

### **Simple Transport Protocol**

---

### **1. Definition**

* A **Simple Transport Protocol** is a **basic model** of a transport-layer protocol that illustrates the **core functions** without the complexities of full protocols like TCP.
* It is often used for **educational purposes** to understand:

  * **Reliable data delivery**
  * **Flow control**
  * **Acknowledgment mechanisms**
  * **Connection setup and teardown**

---

### **2. Purpose**

* To **demonstrate the fundamental operations** required in transport protocols.
* To build a **conceptual foundation** before studying complex protocols like TCP.

---

### **3. Core Elements in a Simple Transport Protocol**

---

### **1. Message Format (Segment Structure)**

| Field                     | Description                          |
| ------------------------- | ------------------------------------ |
| **Source Port**           | Port of sending process              |
| **Destination Port**      | Port of receiving process            |
| **Sequence Number**       | Byte number of first byte in segment |
| **Acknowledgment Number** | Next expected byte from sender       |
| **Checksum**              | For error detection                  |
| **Flags**                 | Control bits: SYN, ACK, FIN          |
| **Data**                  | Application message                  |

---

### **2. Connection Establishment**

* Simple handshake using **SYN** and **ACK** flags.

| Step | Sender                      | Receiver               |
| ---- | --------------------------- | ---------------------- |
| 1    | Sends SYN                   |                        |
| 2    | Receives SYN, sends SYN+ACK |                        |
| 3    | Sends ACK                   | Connection established |

---

### **3. Reliable Data Transfer**

#### **a. Sequencing**

* Assigns a **unique sequence number** to each byte or segment.

#### **b. Acknowledgments**

* Receiver sends an **ACK** for each successfully received segment.

#### **c. Retransmission**

* Sender uses **timers**.
* If **ACK not received** in time, the segment is **retransmitted**.

---

### **4. Flow Control**

* Implemented using a **sliding window**.
* Receiver tells sender how much data it can handle (using **window size**).
* Prevents **buffer overflow** at the receiver.

---

### **5. Error Detection**

* Uses a **checksum** field to verify integrity of the data.
* Corrupted segments are **discarded** or **retransmitted**.

---

### **6. Connection Termination**

| Step | Sender                       | Receiver          |
| ---- | ---------------------------- | ----------------- |
| 1    | Sends **FIN**                |                   |
| 2    | Receives FIN, sends **ACK**  |                   |
| 3    | Sends **FIN** back           |                   |
| 4    | Sender responds with **ACK** | Connection closed |

---

### **7. Pseudocode of Basic Protocol Logic**

#### **Sender Side:**

```
for each segment:
    assign sequence number
    start timer
    send segment
    if (ACK received):
        stop timer
    else if (timeout):
        retransmit segment
```

#### **Receiver Side:**

```
on receiving segment:
    if (checksum is valid and sequence number is expected):
        deliver to application
        send ACK
    else:
        discard segment
```

---

### **8. Key Functions Simulated**

| Function                  | Description                                     |
| ------------------------- | ----------------------------------------------- |
| **Reliable delivery**     | Guaranteed using ACKs and retransmission        |
| **In-order delivery**     | Done using sequence numbers                     |
| **Error control**         | Checksum used to detect corrupted segments      |
| **Flow control**          | Prevents fast sender from overwhelming receiver |
| **Connection management** | Handshake to establish and terminate sessions   |

---

### **9. Comparison with TCP**

| Feature            | Simple Transport Protocol | TCP                            |
| ------------------ | ------------------------- | ------------------------------ |
| Connection Setup   | 2- or 3-step handshake    | 3-way handshake                |
| Flow Control       | Sliding window            | Sliding window                 |
| Congestion Control | Not implemented           | Implemented (slow start, etc.) |
| Reliability        | Basic (ACK + Retransmit)  | Robust                         |
| Security           | Not implemented           | Can use TLS                    |
| Complexity         | Low                       | High                           |

---

### **10. Summary Table**

| Element             | Description                                 |
| ------------------- | ------------------------------------------- |
| Protocol Type       | Conceptual / educational                    |
| Reliability         | Yes (ACK + retransmission)                  |
| Sequencing          | Yes (sequence numbers used)                 |
| Error Detection     | Yes (checksum)                              |
| Flow Control        | Yes (window-based)                          |
| Congestion Control  | No                                          |
| Use Case            | Learning, protocol design foundation        |
| Example Environment | Textbooks, simulations, protocol prototypes |

---

### **Internet Transport Layer Protocols**

---

### **1. Definition**

* **Transport layer protocols** in the Internet provide **end-to-end communication services** between **application processes** running on different hosts.
* The **main Internet transport layer protocols** are:

  * **TCP (Transmission Control Protocol)**
  * **UDP (User Datagram Protocol)**

---

### **2. Overview of Internet Transport Protocols**

| Protocol | Type          | Reliable | Connection-Oriented | Use Case Example             |
| -------- | ------------- | -------- | ------------------- | ---------------------------- |
| **TCP**  | Stream-based  | Yes      | Yes                 | Web, email, file transfer    |
| **UDP**  | Message-based | No       | No                  | Streaming, DNS, VoIP, gaming |

---

### **3. TCP (Transmission Control Protocol)**

---

#### **3.1 Nature and Features**

* **Reliable**, **connection-oriented**, **full-duplex** byte-stream protocol.
* Ensures data is:

  * **Delivered**
  * **Ordered**
  * **Without duplication**
  * **Without errors**

---

#### **3.2 Key Characteristics**

| Feature                 | Description                                           |
| ----------------------- | ----------------------------------------------------- |
| **Connection-oriented** | Requires 3-way handshake to establish connection      |
| **Reliable**            | Uses ACKs, timeouts, retransmissions                  |
| **Ordered delivery**    | Uses sequence numbers                                 |
| **Flow control**        | Sliding window mechanism                              |
| **Congestion control**  | Adjusts send rate using algorithms (slow start, etc.) |
| **Error checking**      | Uses 16-bit checksum in TCP header                    |
| **Full-duplex**         | Simultaneous two-way communication                    |

---

#### **3.3 TCP Header Fields (20 to 60 bytes)**

| Field                   | Description                                     |
| ----------------------- | ----------------------------------------------- |
| Source/Destination Port | Identifies application processes                |
| Sequence Number         | Byte offset of first byte in this segment       |
| Acknowledgment Number   | Next expected byte from peer                    |
| Data Offset             | Header length in 32-bit words                   |
| Flags (e.g., SYN, ACK)  | Control connection setup and teardown           |
| Window Size             | Receiver’s buffer space (for flow control)      |
| Checksum                | Detects errors in header + data                 |
| Urgent Pointer          | Marks urgent data position (if URG flag is set) |
| Options                 | Optional fields like MSS, window scale          |

---

#### **3.4 TCP Services**

* Reliable data transfer
* Flow control
* Congestion control
* Ordered byte stream
* Connection management (SYN, FIN)

---

### **4. UDP (User Datagram Protocol)**

---

#### **4.1 Nature and Features**

* **Unreliable**, **connectionless**, **message-oriented** transport protocol.
* Offers **fast**, **lightweight** communication without guarantees.

---

#### **4.2 Key Characteristics**

| Feature                   | Description                                                      |
| ------------------------- | ---------------------------------------------------------------- |
| **Connectionless**        | No setup or teardown process                                     |
| **Unreliable**            | No retransmission or acknowledgment                              |
| **Message-based**         | Preserves boundaries of application messages                     |
| **No flow control**       | Sender can flood receiver                                        |
| **No congestion control** | UDP does not adjust its rate based on network conditions         |
| **Low overhead**          | Only 8-byte header; fast and suitable for real-time applications |

---

#### **4.3 UDP Header Format (8 bytes)**

| Field            | Description                                          |
| ---------------- | ---------------------------------------------------- |
| Source Port      | Port of sending application                          |
| Destination Port | Port of receiving application                        |
| Length           | Length of UDP header + data                          |
| Checksum         | Error checking (optional in IPv4, mandatory in IPv6) |

---

#### **4.4 Use Cases**

* DNS (Domain Name System)
* VoIP
* Streaming media
* Online gaming
* TFTP (Trivial File Transfer Protocol)

---

### **5. Comparison: TCP vs UDP**

| Feature                | TCP                        | UDP                               |
| ---------------------- | -------------------------- | --------------------------------- |
| **Connection Type**    | Connection-oriented        | Connectionless                    |
| **Reliability**        | Yes (ACKs, retransmission) | No                                |
| **Ordered Delivery**   | Yes                        | No                                |
| **Error Checking**     | Yes (Checksum)             | Yes (Checksum, optional in IPv4)  |
| **Flow Control**       | Yes (Sliding Window)       | No                                |
| **Congestion Control** | Yes                        | No                                |
| **Header Size**        | Minimum 20 bytes           | 8 bytes                           |
| **Speed**              | Slower due to overhead     | Faster                            |
| **Use Case**           | HTTP, FTP, SMTP, Telnet    | DNS, VoIP, games, video streaming |

---

### **6. Summary Table of Internet Transport Protocols**

| Protocol | Connection | Reliability | Ordered | Flow Control | Congestion Control | Use Case                           |
| -------- | ---------- | ----------- | ------- | ------------ | ------------------ | ---------------------------------- |
| TCP      | Yes        | Yes         | Yes     | Yes          | Yes                | HTTP, FTP, Email, SSH              |
| UDP      | No         | No          | No      | No           | No                 | DNS, VoIP, Video Streaming, Gaming |

---

### **7. Additional Protocols (Experimental or Specialized)**

| Protocol | Description                                                                     |
| -------- | ------------------------------------------------------------------------------- |
| **DCCP** | Datagram Congestion Control Protocol; unreliable but with congestion control    |
| **SCTP** | Stream Control Transmission Protocol; supports multi-streaming and multi-homing |
| **QUIC** | Developed by Google; reliable, secure, faster than TCP, used in HTTP/3          |

---

### **8. Conclusion**

* **TCP and UDP** are the **core Internet transport protocols**.
* TCP ensures **reliability and order**, suitable for file transfer and web browsing.
* UDP offers **speed and low overhead**, ideal for real-time or loss-tolerant applications.

---

### **UDP (User Datagram Protocol)**

---

### **1. Definition**

* **UDP** is a **connectionless**, **unreliable**, **transport layer protocol** defined in **RFC 768**.
* It provides **minimal transport-layer services**, focusing on **fast, lightweight** communication.
* Ideal for applications that can tolerate **some data loss** but require **low latency**.

---

### **2. Characteristics of UDP**

| Feature                   | Description                                                     |
| ------------------------- | --------------------------------------------------------------- |
| **Connectionless**        | No connection setup or teardown                                 |
| **Unreliable**            | No guarantees for delivery, ordering, or duplication prevention |
| **Message-Oriented**      | Maintains boundaries between application messages               |
| **No Flow Control**       | Cannot regulate sender’s transmission rate                      |
| **No Congestion Control** | Does not detect or avoid network congestion                     |
| **Fast and Lightweight**  | Minimal header (8 bytes), no state information needed           |
| **Checksum-Based**        | Optional in IPv4, mandatory in IPv6 for error detection         |

---

### **3. UDP Packet Structure (Header)**

| Field                | Size (bits) | Description                                                      |
| -------------------- | ----------- | ---------------------------------------------------------------- |
| **Source Port**      | 16          | Port of sending process                                          |
| **Destination Port** | 16          | Port of receiving process                                        |
| **Length**           | 16          | Length of UDP header + data (in bytes)                           |
| **Checksum**         | 16          | Error-checking field; covers UDP header, data, and pseudo-header |

* **Total header size**: 8 bytes

---

### **4. Operation of UDP**

1. **Sender Side**:

   * Application sends a **message** to UDP layer.
   * UDP attaches header → creates **datagram**.
   * Datagram handed to **IP layer** for delivery.

2. **Receiver Side**:

   * IP layer receives UDP datagram.
   * UDP uses **destination port** to deliver to correct application.

---

### **5. No Reliability Mechanism**

| Feature               | Handled by UDP? | Description                                        |
| --------------------- | --------------- | -------------------------------------------------- |
| **Acknowledgment**    | No              | No feedback on delivery                            |
| **Retransmission**    | No              | Lost packets are not resent                        |
| **Sequencing**        | No              | Packets may arrive out of order                    |
| **Duplication check** | No              | Duplicate packets may be passed to the application |

---

### **6. Use Cases**

| Application         | Reason for Using UDP                     |
| ------------------- | ---------------------------------------- |
| **DNS**             | Short query-response, low latency        |
| **VoIP**            | Tolerates loss, needs real-time delivery |
| **Video Streaming** | Accepts quality loss to avoid delay      |
| **Online Gaming**   | High interactivity, low latency required |
| **DHCP**            | For IP address assignment via broadcast  |
| **SNMP**            | Simple monitoring with low overhead      |
| **TFTP**            | Lightweight file transfer                |

---

### **7. Port Numbers**

| Port Type            | Range         |
| -------------------- | ------------- |
| **Well-known ports** | 0 – 1023      |
| **Registered ports** | 1024 – 49151  |
| **Dynamic ports**    | 49152 – 65535 |

* Example:

  * DNS: 53
  * DHCP: 67/68
  * SNMP: 161

---

### **8. Advantages of UDP**

| Advantage                 | Description                                         |
| ------------------------- | --------------------------------------------------- |
| **Speed**                 | No handshaking or retransmissions                   |
| **Low Overhead**          | 8-byte header vs 20-byte TCP header                 |
| **No Connection Setup**   | Saves resources and time                            |
| **Real-Time Suitability** | Ideal for time-sensitive applications               |
| **Stateless**             | Server doesn't track clients, reducing memory usage |

---

### **9. Disadvantages of UDP**

| Limitation                | Description                                             |
| ------------------------- | ------------------------------------------------------- |
| **No Reliability**        | Packets may be lost, duplicated, or arrive out of order |
| **No Congestion Control** | Can cause or worsen network congestion                  |
| **No Flow Control**       | Fast sender may overwhelm slow receiver                 |
| **No Packet Management**  | Receiver must handle errors, order, and loss manually   |

---

### **10. UDP vs TCP**

| Feature                  | UDP            | TCP                 |
| ------------------------ | -------------- | ------------------- |
| **Connection Type**      | Connectionless | Connection-oriented |
| **Reliability**          | Unreliable     | Reliable            |
| **Ordering**             | Not guaranteed | Guaranteed          |
| **Header Size**          | 8 bytes        | 20–60 bytes         |
| **Flow/Congestion Ctrl** | No             | Yes                 |
| **Latency**              | Low            | Higher              |
| **Use Cases**            | Real-time data | Reliable transfer   |

---

### **11. Summary Table**

| Field                | UDP Description                          |
| -------------------- | ---------------------------------------- |
| **Layer**            | Transport Layer                          |
| **Protocol Type**    | Connectionless, unreliable               |
| **Header Size**      | 8 bytes                                  |
| **Reliability**      | No                                       |
| **Flow Control**     | No                                       |
| **Error Detection**  | Optional in IPv4, mandatory in IPv6      |
| **Use Case**         | VoIP, DNS, video streaming, online games |
| **Application Type** | Tolerates some loss, demands speed       |

---

### **TCP (Transmission Control Protocol)**

---

### **1. Definition**

* **TCP** is a **connection-oriented**, **reliable**, **byte-stream**, **full-duplex** transport layer protocol defined in **RFC 793**.
* It provides **end-to-end communication** with **guaranteed delivery**, **ordered data**, and **error correction** between applications on different hosts in the Internet.

---

### **2. Characteristics of TCP**

| Feature                  | Description                                                                    |
| ------------------------ | ------------------------------------------------------------------------------ |
| **Connection-oriented**  | Requires a handshake before data transmission                                  |
| **Reliable delivery**    | Uses acknowledgments, retransmission, and sequencing to guarantee delivery     |
| **Byte-oriented stream** | Transmits data as a continuous stream of bytes, not discrete packets           |
| **Full-duplex**          | Supports simultaneous two-way communication                                    |
| **Error checking**       | Uses a checksum to detect errors in header and data                            |
| **Flow control**         | Prevents sender from overwhelming the receiver (via window size)               |
| **Congestion control**   | Avoids network overload using algorithms like slow start, congestion avoidance |
| **Ordered delivery**     | Data is delivered in the exact order it was sent                               |

---

### **3. TCP Segment Format (Header)**

| Field Name                | Size (bits) | Description                                           |
| ------------------------- | ----------- | ----------------------------------------------------- |
| **Source Port**           | 16          | Port of sending process                               |
| **Destination Port**      | 16          | Port of receiving process                             |
| **Sequence Number**       | 32          | Byte offset of the first byte in this segment         |
| **Acknowledgment Number** | 32          | Next byte expected from the sender                    |
| **Data Offset**           | 4           | Length of TCP header in 32-bit words                  |
| **Flags (Control bits)**  | 6           | URG, ACK, PSH, RST, SYN, FIN                          |
| **Window Size**           | 16          | Receiver buffer size (for flow control)               |
| **Checksum**              | 16          | Error detection for header and data                   |
| **Urgent Pointer**        | 16          | Position of urgent data (used when URG flag is set)   |
| **Options (variable)**    | -           | Used for features like MSS, window scaling, timestamp |

---

### **4. TCP Services**

| Service                   | Description                                                     |
| ------------------------- | --------------------------------------------------------------- |
| **Reliable Transfer**     | Ensures data is not lost, duplicated, or corrupted              |
| **In-order Delivery**     | Delivers data in the exact sequence it was sent                 |
| **Error Control**         | Uses checksum and retransmission for corrupted or lost segments |
| **Flow Control**          | Uses sliding window to manage rate of data flow                 |
| **Congestion Control**    | Adjusts sending rate based on network congestion                |
| **Multiplexing**          | Uses port numbers to support multiple applications              |
| **Connection Management** | Establishes and tears down connection gracefully                |

---

### **5. TCP Connection Establishment (Three-Way Handshake)**

| Step | Client                        | Server                     |
| ---- | ----------------------------- | -------------------------- |
| 1    | Sends SYN (synchronize)       | →                          |
| 2    | Receives SYN, sends SYN + ACK | ←                          |
| 3    | Sends ACK                     | →                          |
|      | **Connection established**    | **Connection established** |

---

### **6. TCP Connection Termination (Four-Step)**

| Step | Action           |
| ---- | ---------------- |
| 1    | Host A sends FIN |
| 2    | Host B sends ACK |
| 3    | Host B sends FIN |
| 4    | Host A sends ACK |

* Ensures both sides close the connection cleanly.

---

### **7. Flow Control (Sliding Window Protocol)**

* Sender maintains a **window** of bytes that it can send before waiting for an ACK.
* Receiver advertises its **available buffer size** (window size).
* **Sliding window** dynamically adjusts based on ACKs received.

---

### **8. Error Control Mechanism**

| Method               | Description                                                     |
| -------------------- | --------------------------------------------------------------- |
| **Checksum**         | Detects corrupted data                                          |
| **ACK/NAK**          | Confirms or requests retransmission                             |
| **Timeout**          | Retransmits segments not acknowledged within a set time         |
| **Sequence Numbers** | Ensures segments are delivered in order and without duplication |

---

### **9. Congestion Control Algorithms in TCP**

| Algorithm                | Description                                                            |
| ------------------------ | ---------------------------------------------------------------------- |
| **Slow Start**           | Increases congestion window (cwnd) exponentially at the beginning      |
| **Congestion Avoidance** | Increases cwnd linearly after threshold                                |
| **Fast Retransmit**      | Retransmits a packet if 3 duplicate ACKs are received                  |
| **Fast Recovery**        | Skips slow start after fast retransmit and enters congestion avoidance |

---

### **10. TCP Flags (Control Bits)**

| Flag | Name           | Function                          |
| ---- | -------------- | --------------------------------- |
| URG  | Urgent         | Urgent pointer field is valid     |
| ACK  | Acknowledgment | ACK number is valid               |
| PSH  | Push           | Push buffered data to application |
| RST  | Reset          | Reset the connection              |
| SYN  | Synchronize    | Initiate a connection             |
| FIN  | Finish         | Gracefully terminate a connection |

---

### **11. Advantages of TCP**

| Feature                       | Description                                  |
| ----------------------------- | -------------------------------------------- |
| **Reliable Delivery**         | No data loss or duplication                  |
| **Flow & Congestion Control** | Manages receiver capacity and network load   |
| **Ordered Data**              | Maintains sequence of transmitted data       |
| **Wide Compatibility**        | Supported by most applications and platforms |

---

### **12. Disadvantages of TCP**

| Limitation             | Description                                          |
| ---------------------- | ---------------------------------------------------- |
| **Higher Overhead**    | Large header size (min. 20 bytes)                    |
| **Complexity**         | More state and logic required                        |
| **Slower Performance** | Compared to UDP for real-time or lightweight traffic |

---

### **13. Use Cases of TCP**

| Application        | Reason for TCP Use                   |
| ------------------ | ------------------------------------ |
| **HTTP/HTTPS**     | Reliable web browsing                |
| **FTP**            | Accurate file transfers              |
| **SMTP/IMAP/POP3** | Reliable email delivery              |
| **SSH**            | Secure remote login                  |
| **Telnet**         | Command-line access with reliability |

---

### **14. Summary Table**

| Feature            | TCP Description                             |
| ------------------ | ------------------------------------------- |
| Protocol Type      | Connection-oriented, reliable, stream-based |
| Header Size        | 20–60 bytes                                 |
| Reliability        | Yes (ACK, retransmit, error detection)      |
| Ordering           | Guaranteed                                  |
| Flow Control       | Sliding window                              |
| Congestion Control | Yes (slow start, avoidance, fast recovery)  |
| Use Cases          | Web, email, file transfer, secure shell     |

---

### **Domain Name System (DNS)**

---

### **1. Definition**

* The **Domain Name System (DNS)** is a **distributed hierarchical database system** that **translates human-readable domain names** (e.g., `www.google.com`) into **IP addresses** (e.g., `142.250.64.132`) required for locating and identifying computer services and devices on the Internet.
* Defined in **RFC 1034** and **RFC 1035**.

---

### **2. Purpose**

* To make the **Internet user-friendly** by allowing users to access websites using **domain names** instead of numerical IP addresses.
* Provides **name-to-address** and **address-to-name** mappings.

---

### **3. Components of DNS**

---

#### **1. Domain Names**

* Structured hierarchically:

  * **Root domain**: Represented as a dot `.`
  * **Top-Level Domain (TLD)**: `.com`, `.org`, `.edu`, `.in`, etc.
  * **Second-Level Domain**: `google` in `google.com`
  * **Subdomains**: `mail.google.com`, `maps.google.com`

---

#### **2. DNS Name Space**

* A **tree-structured** namespace, where:

  * Each node represents a domain.
  * Leaf nodes represent **hostnames**.
  * Each node has a **label**, separated by dots.

---

#### **3. DNS Zones**

* A **zone** is a portion of the domain name space managed by a specific DNS server.
* Each zone stores:

  * **Resource Records (RRs)**
  * **Start of Authority (SOA) record**
  * **Name server (NS) records**

---

### **4. DNS Resource Records (RR)**

| Record Type | Description                                     | Example                       |
| ----------- | ----------------------------------------------- | ----------------------------- |
| **A**       | Maps domain name to IPv4 address                | `example.com → 93.184.216.34` |
| **AAAA**    | Maps domain name to IPv6 address                | `example.com → 2606:2800...`  |
| **CNAME**   | Canonical name (alias)                          | `www → example.com`           |
| **MX**      | Mail exchange server                            | Used for email delivery       |
| **NS**      | Name server responsible for the zone            | `ns1.example.com`             |
| **PTR**     | Pointer (reverse lookup: IP → name)             | `34.216.184.93.in-addr.arpa`  |
| **SOA**     | Start of authority (zone info, serial, refresh) | Primary server data           |
| **TXT**     | Human-readable text or verification info        | SPF records, site verif.      |

---

### **5. Types of DNS Servers**

| Server Type            | Role                                                      |
| ---------------------- | --------------------------------------------------------- |
| **Root DNS Server**    | Knows location of all TLD name servers                    |
| **TLD DNS Server**     | Manages domains under `.com`, `.org`, `.in`, etc.         |
| **Authoritative DNS**  | Provides final IP address for a domain                    |
| **Recursive Resolver** | Receives DNS queries from clients and resolves them fully |

---

### **6. DNS Query Process (Name Resolution)**

1. User enters `www.example.com`.
2. Request goes to **recursive resolver**.
3. Resolver asks **root server** → gets address of TLD server.
4. Resolver asks **TLD server** (e.g., `.com`) → gets address of authoritative server.
5. Resolver asks **authoritative server** → gets IP address for `www.example.com`.
6. Resolver returns IP to client → browser connects to the IP.

---

### **7. Types of DNS Queries**

| Query Type          | Description                                                             |
| ------------------- | ----------------------------------------------------------------------- |
| **Recursive Query** | Resolver takes full responsibility to find the answer                   |
| **Iterative Query** | Resolver asks each server in the hierarchy; continues querying manually |
| **Inverse Query**   | Looks up domain name from an IP address using **PTR records**           |

---

### **8. Caching in DNS**

* To reduce load and improve speed, DNS responses are **cached** at various levels:

  * Browser cache
  * Operating system cache
  * Resolver (ISP) cache
* **TTL (Time-To-Live)** in resource records controls cache duration.

---

### **9. DNS Protocol Details**

| Attribute              | Value                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| **Transport Protocol** | UDP (usually port 53), TCP for large transfers or zone transfers |
| **Message Format**     | Header + Question + Answer + Authority + Additional sections     |
| **Standard Port**      | Port 53                                                          |

---

### **10. DNS Message Structure**

| Section        | Content                                                           |
| -------------- | ----------------------------------------------------------------- |
| **Header**     | Transaction ID, flags (query/response), number of records         |
| **Question**   | Domain name, query type (A, AAAA, MX, etc.)                       |
| **Answer**     | Actual response records (e.g., IP address)                        |
| **Authority**  | Info about authoritative name servers                             |
| **Additional** | Extra information (e.g., IP of name servers in authority section) |

---

### **11. Security in DNS**

| Technique                | Purpose                                            |
| ------------------------ | -------------------------------------------------- |
| **DNSSEC**               | Digital signature-based authentication of DNS data |
| **DNS over HTTPS (DoH)** | Encrypts DNS queries to prevent eavesdropping      |
| **DNS over TLS (DoT)**   | Secures DNS communication using TLS                |

---

### **12. Common DNS Tools**

| Tool       | Use                         |
| ---------- | --------------------------- |
| `nslookup` | Query DNS records           |
| `dig`      | Detailed DNS query analysis |
| `host`     | Simple DNS lookups          |

---

### **13. Advantages of DNS**

| Advantage                  | Description                                     |
| -------------------------- | ----------------------------------------------- |
| **User-friendly**          | Easy to remember names instead of IPs           |
| **Scalable**               | Hierarchical and distributed architecture       |
| **Redundant and Reliable** | Multiple servers ensure continuous availability |
| **Flexible**               | Easy domain management and delegation           |

---

### **14. Summary Table**

| Element                | DNS Description                           |
| ---------------------- | ----------------------------------------- |
| **Function**           | Maps domain names to IP addresses         |
| **Structure**          | Hierarchical, distributed                 |
| **Transport Protocol** | UDP (port 53); TCP used for special cases |
| **Record Types**       | A, AAAA, MX, CNAME, NS, PTR, SOA, TXT     |
| **Query Types**        | Recursive, iterative, inverse             |
| **Main Servers**       | Root, TLD, Authoritative, Resolver        |
| **Security Add-ons**   | DNSSEC, DNS-over-HTTPS, DNS-over-TLS      |

---

### **Electronic Mail (E-Mail)**

---

### **1. Definition**

* **Electronic Mail (E-Mail)** is a **store-and-forward** communication system that enables users to send, receive, and store textual and multimedia messages over a computer network.
* It consists of **user agents**, **message transfer agents**, and **mail delivery systems**, operating under protocols like **SMTP**, **POP3**, and **IMAP**.

---

### **2. Architecture of E-Mail System**

#### **1. Components**

| Component                        | Description                                           |
| -------------------------------- | ----------------------------------------------------- |
| **User Agent (UA)**              | Interface for composing, reading, and managing emails |
| **Message Transfer Agent (MTA)** | Transfers messages between mail servers               |
| **Message Delivery Agent (MDA)** | Delivers message to recipient's mailbox               |
| **Mail Server**                  | Stores mailboxes, handles message transfer            |

---

#### **2. Basic Flow of E-Mail**

1. **Sender** composes email using **User Agent (UA)**.
2. UA sends message to **MTA (e.g., SMTP)** on sender’s mail server.
3. MTA forwards email to recipient's mail server (also via SMTP).
4. Recipient retrieves email using **MUA** via **POP3** or **IMAP**.

---

### **3. Phases of Email Transmission**

| Phase          | Description                                                       |
| -------------- | ----------------------------------------------------------------- |
| **Submission** | Sender uses UA to compose and submit message to SMTP server       |
| **Transfer**   | MTA relays message across networks to the recipient's mail server |
| **Delivery**   | MDA stores message in recipient’s mailbox                         |
| **Access**     | Recipient uses MUA to retrieve message using POP3 or IMAP         |

---

### **4. E-Mail Protocols**

---

#### **1. SMTP (Simple Mail Transfer Protocol)**

* Used to **send** emails from client to server or between servers.
* **Push protocol**, uses **TCP port 25**.

| Feature         | Description                       |
| --------------- | --------------------------------- |
| Type            | Push                              |
| Transport Layer | TCP (port 25, 587 for submission) |
| Role            | Sends mail to mail servers        |

---

#### **2. POP3 (Post Office Protocol version 3)**

* Used by client to **download** email from server to local machine.
* **Pull protocol**, uses **TCP port 110**.
* Does **not keep a copy** on the server by default.

| Feature  | Description         |
| -------- | ------------------- |
| Type     | Pull                |
| Behavior | Download and delete |
| Port     | TCP 110             |

---

#### **3. IMAP (Internet Message Access Protocol)**

* Used by client to **view and manage** email **on the server**.
* **Synchronizes** emails across devices.
* Uses **TCP port 143** (port 993 for secure).

| Feature  | Description           |
| -------- | --------------------- |
| Type     | Pull (with sync)      |
| Behavior | Leaves mail on server |
| Port     | TCP 143               |

---

### **5. Message Format (RFC 5322)**

---

#### **1. Header Section**

| Header Field   | Description                        |
| -------------- | ---------------------------------- |
| `From:`        | Sender’s email address             |
| `To:`          | Recipient’s email address          |
| `Subject:`     | Subject line                       |
| `Date:`        | Timestamp of when message was sent |
| `CC:` / `BCC:` | Carbon Copy / Blind Carbon Copy    |
| `Reply-To:`    | Address for replies                |

---

#### **2. Body Section**

* Contains **actual content** of the email.
* Can be:

  * **Plain text**
  * **HTML formatted**
  * **Multipart (attachments, images)**

---

### **6. MIME (Multipurpose Internet Mail Extensions)**

* Extends email format to support:

  * **Attachments**
  * **Multimedia content (images, audio, video)**
  * **Multiple content types**

| MIME Header                 | Purpose                            |
| --------------------------- | ---------------------------------- |
| `Content-Type`              | Specifies type (text, image, etc.) |
| `Content-Transfer-Encoding` | Specifies encoding method          |

---

### **7. Advantages of Email**

| Advantage              | Description                            |
| ---------------------- | -------------------------------------- |
| **Speed**              | Instant communication                  |
| **Cost-effective**     | Free or low-cost for most users        |
| **Attachment support** | Send files, images, documents, etc.    |
| **Accessibility**      | Accessible from anywhere with internet |
| **Record Keeping**     | Messages can be stored indefinitely    |

---

### **8. Disadvantages of Email**

| Disadvantage        | Description                                    |
| ------------------- | ---------------------------------------------- |
| **Spam**            | Unwanted or malicious messages                 |
| **Viruses**         | Attachments may contain malware                |
| **Phishing**        | Fraudulent messages aimed to steal information |
| **Delivery Issues** | Possible delays or bounce-backs                |

---

### **9. Security Concerns and Measures**

| Concern             | Protection Method                              |
| ------------------- | ---------------------------------------------- |
| **Confidentiality** | Use **S/MIME**, **PGP**, or **TLS encryption** |
| **Authentication**  | Use **SPF**, **DKIM**, **DMARC**               |
| **Integrity**       | Message hashing and digital signatures         |

---

### **10. Summary Table**

| Feature               | Email Description                     |
| --------------------- | ------------------------------------- |
| **Architecture**      | Client-Server, Store-and-Forward      |
| **Protocols**         | SMTP, POP3, IMAP                      |
| **Ports**             | 25 (SMTP), 110 (POP3), 143 (IMAP)     |
| **Content Format**    | Header + Body (MIME for rich content) |
| **Message Access**    | Pull via POP3/IMAP                    |
| **Security Features** | TLS, S/MIME, SPF, DKIM, DMARC         |
| **Common Tools**      | Gmail, Outlook, Thunderbird           |

---

### **World Wide Web (WWW)**

---

### **1. Definition**

* The **World Wide Web (WWW)** is a **system of interlinked hypertext documents** and multimedia content accessed via the Internet using **web browsers**.
* It is built upon **Internet protocols** such as **HTTP/HTTPS**, and uses **URLs** to locate resources.
* Created by **Tim Berners-Lee** in 1989 at **CERN**.

---

### **2. Architecture of the World Wide Web**

---

#### **1. Components**

| Component                          | Description                                                    |
| ---------------------------------- | -------------------------------------------------------------- |
| **Web Browser**                    | Client software used to request, receive, and render web pages |
| **Web Server**                     | Hosts and serves web resources via HTTP                        |
| **Web Page**                       | A document formatted in HTML, linked via hyperlinks            |
| **URL (Uniform Resource Locator)** | Identifies web resources' address                              |
| **HTTP/HTTPS**                     | Protocols used to transfer web data between client and server  |

---

#### **2. Client-Server Model**

* WWW is based on a **client-server architecture**:

  * **Client (browser)** sends a **request** using HTTP.
  * **Server** processes the request and returns the **HTML document** or resource.

---

### **3. Working of WWW**

1. User enters a **URL** into the browser.
2. Browser resolves domain using **DNS** to get IP address.
3. Browser establishes a connection (usually **TCP**) with the **web server**.
4. Sends **HTTP request** (e.g., GET).
5. Server sends back an **HTTP response** with content (HTML, CSS, JS, etc.).
6. Browser **renders** the page for the user.

---

### **4. Key Technologies**

---

#### **1. HTML (HyperText Markup Language)**

* Used to **structure** content on web pages.
* Elements include headings, paragraphs, images, tables, and hyperlinks.

---

#### **2. CSS (Cascading Style Sheets)**

* Used to **style** HTML documents: layout, colors, fonts, spacing, etc.

---

#### **3. JavaScript**

* Used for **client-side scripting** to enable dynamic content and interactivity.

---

#### **4. Web Protocols**

| Protocol  | Description                                            |
| --------- | ------------------------------------------------------ |
| **HTTP**  | HyperText Transfer Protocol; basic protocol of the web |
| **HTTPS** | Secure version of HTTP using TLS/SSL                   |
| **FTP**   | Used for transferring files                            |

---

### **5. Uniform Resource Locator (URL)**

| Component       | Description                             | Example                              |
| --------------- | --------------------------------------- | ------------------------------------ |
| **Protocol**    | Access method (e.g., HTTP, HTTPS, FTP)  | `https`                              |
| **Host/Domain** | Server address or domain name           | `www.example.com`                    |
| **Path**        | Specific file or resource on the server | `/index.html`                        |
| **Full URL**    | Complete address of a web resource      | `https://www.example.com/index.html` |

---

### **6. Hypertext and Hypermedia**

| Type           | Description                                                 |
| -------------- | ----------------------------------------------------------- |
| **Hypertext**  | Text that links to other text via hyperlinks                |
| **Hypermedia** | Extension of hypertext with multimedia (audio, video, etc.) |

---

### **7. Features of the WWW**

| Feature                  | Description                                           |
| ------------------------ | ----------------------------------------------------- |
| **Interlinked content**  | Web pages connected through hyperlinks                |
| **Multimedia support**   | Handles images, videos, audio                         |
| **Platform-independent** | Accessible from various operating systems and devices |
| **Global reach**         | Content is available worldwide                        |
| **Interactive**          | Supports dynamic websites via JavaScript, forms, etc. |

---

### **8. Types of Web Pages**

| Type             | Description                                                |
| ---------------- | ---------------------------------------------------------- |
| **Static Page**  | Fixed content, coded in HTML, sent as-is from the server   |
| **Dynamic Page** | Content is generated at request time via server-side logic |

---

### **9. Web Servers and Browsers**

#### **1. Popular Web Servers**

| Server            | Description                         |
| ----------------- | ----------------------------------- |
| **Apache**        | Open-source, widely used web server |
| **Nginx**         | High-performance HTTP server        |
| **Microsoft IIS** | Internet Information Services       |

#### **2. Popular Web Browsers**

| Browser             | Vendor    |
| ------------------- | --------- |
| **Google Chrome**   | Google    |
| **Mozilla Firefox** | Mozilla   |
| **Safari**          | Apple     |
| **Edge**            | Microsoft |

---

### **10. WWW vs Internet**

| Aspect     | WWW                    | Internet                                  |
| ---------- | ---------------------- | ----------------------------------------- |
| Definition | System of web pages    | Global network infrastructure             |
| Protocol   | HTTP/HTTPS             | TCP/IP                                    |
| Scope      | Subset of the Internet | Superset containing WWW, email, FTP, etc. |
| Access     | Through web browsers   | Through browsers, apps, etc.              |

---

### **11. Limitations of WWW**

| Limitation               | Description                                    |
| ------------------------ | ---------------------------------------------- |
| **Security threats**     | Phishing, malware, man-in-the-middle attacks   |
| **Information overload** | Difficult to filter quality content            |
| **Accessibility issues** | Some sites not optimized for all users/devices |

---

### **12. Summary Table**

| Element             | Description                                          |
| ------------------- | ---------------------------------------------------- |
| **Purpose**         | Provide access to interlinked multimedia information |
| **Technology**      | HTTP, HTML, CSS, JavaScript                          |
| **Structure**       | Client-server with DNS and TCP/IP                    |
| **Tools**           | Web browser (client), web server (host)              |
| **Resource Access** | Using URLs                                           |
| **Protocols Used**  | HTTP, HTTPS, DNS, TCP/IP                             |
| **Page Types**      | Static and dynamic                                   |
| **Inventor**        | Tim Berners-Lee (1989, CERN)                         |

---

### **Architectural Overview of the World Wide Web (WWW)**

---

### **1. Architecture Type**

* The **World Wide Web** uses a **client-server architecture** built on top of the **Internet**.
* Clients (web browsers) request services/resources.
* Servers (web servers) provide services/resources.

---

### **2. Core Components**

| Component                          | Description                                                                   |
| ---------------------------------- | ----------------------------------------------------------------------------- |
| **Client (User Agent)**            | Web browser that sends requests and renders responses (e.g., Chrome, Firefox) |
| **Web Server**                     | Hosts web pages/resources and handles HTTP requests (e.g., Apache, Nginx)     |
| **Web Pages**                      | Documents formatted in HTML, linked by hyperlinks                             |
| **Protocols**                      | Enable communication and resource access (HTTP, HTTPS, DNS, TCP/IP)           |
| **Uniform Resource Locator (URL)** | Identifies location of resources on the Web                                   |

---

### **3. Flow of Web Request**

1. **User enters a URL** in browser.
2. **DNS resolves** domain to an IP address.
3. **TCP connection** established between browser and server.
4. **Browser sends HTTP request** to the server.
5. **Server sends HTTP response** containing HTML document.
6. **Browser renders** the content using HTML, CSS, JavaScript.

---

### **4. Logical Layers of WWW**

| Layer                  | Description                                                                     |
| ---------------------- | ------------------------------------------------------------------------------- |
| **Application Layer**  | User interacts with the browser and web application                             |
| **Presentation Layer** | Rendering of HTML, CSS, multimedia content                                      |
| **Session Layer**      | Maintains communication sessions (HTTP is stateless but uses cookies, sessions) |
| **Transport Layer**    | Reliable delivery using **TCP**                                                 |
| **Network Layer**      | Routing data using **IP addresses**                                             |
| **Data Link Layer**    | Handles MAC addresses, frames (e.g., Ethernet, Wi-Fi)                           |
| **Physical Layer**     | Physical transmission of bits (cables, radio, etc.)                             |

---

### **5. Protocol Stack Used**

| Layer (OSI) | Protocols Used               |
| ----------- | ---------------------------- |
| Application | HTTP, HTTPS, FTP, DNS        |
| Transport   | TCP (usually), sometimes UDP |
| Network     | IP (IPv4/IPv6)               |
| Link        | Ethernet, Wi-Fi, PPP         |

---

### **6. Key Technologies in the Architecture**

| Technology                  | Role in Architecture                                                |
| --------------------------- | ------------------------------------------------------------------- |
| **HTML**                    | Defines the structure of web pages                                  |
| **CSS**                     | Controls visual presentation                                        |
| **JavaScript**              | Adds interactivity and dynamic behavior                             |
| **HTTP/HTTPS**              | Protocols for request/response communication                        |
| **Web Servers**             | Serve HTML and resources (e.g., Apache, Nginx)                      |
| **Web Clients**             | Render and interact with web content (e.g., browsers)               |
| **Web Application Servers** | Process dynamic requests using server-side languages (PHP, Node.js) |

---

### **7. Web Page Retrieval Process**

| Step | Action                                                 |
| ---- | ------------------------------------------------------ |
| 1    | Client sends HTTP GET request using URL                |
| 2    | Server locates the requested resource                  |
| 3    | Server sends HTTP response with content                |
| 4    | Client renders the content (HTML → visible page)       |
| 5    | Additional requests for CSS, images, JS made as needed |

---

### **8. Dynamic vs Static Content Handling**

| Type        | Description                                  |
| ----------- | -------------------------------------------- |
| **Static**  | Served as-is, e.g., plain HTML, images       |
| **Dynamic** | Generated on-demand, e.g., PHP, JSP, Node.js |

---

### **9. Distributed Nature**

* The WWW is **decentralized** and **distributed**:

  * Content is stored across **millions of servers** globally.
  * Clients retrieve content using **standard protocols**.

---

### **10. Security Aspects in Architecture**

| Mechanism            | Purpose                       |
| -------------------- | ----------------------------- |
| **HTTPS (TLS)**      | Encrypts communication        |
| **Cookies/Sessions** | Maintain stateful sessions    |
| **Authentication**   | Login systems to verify users |
| **Authorization**    | Role-based access control     |

---

### **11. Content Delivery Optimization**

| Feature                            | Description                                          |
| ---------------------------------- | ---------------------------------------------------- |
| **Caching**                        | Saves web content for faster access                  |
| **CDN (Content Delivery Network)** | Distributes content to geographically closer servers |
| **Load Balancers**                 | Distribute traffic across multiple servers           |

---

### **12. Summary Table**

| Element                | Description                                          |
| ---------------------- | ---------------------------------------------------- |
| **Architecture Model** | Client-Server                                        |
| **Key Protocols**      | HTTP, HTTPS, DNS, TCP/IP                             |
| **Data Format**        | HTML, CSS, JavaScript, multimedia                    |
| **Core Components**    | Web browser, web server, DNS, URL                    |
| **Communication Flow** | Request → Response → Rendering                       |
| **Layering**           | Based on OSI/Internet stack (Application → Physical) |
| **Content Type**       | Static and Dynamic                                   |

---

### **Dynamic Web Document**

---

### **1. Definition**

* A **dynamic web document** is a web page whose **content is generated at runtime** based on user interaction, time, session data, or database queries.
* Unlike static documents (fixed HTML files), **dynamic pages change with context or data** and often involve **server-side** or **client-side scripting**.

---

### **2. Characteristics**

| Feature                   | Description                                                     |
| ------------------------- | --------------------------------------------------------------- |
| **Content is not fixed**  | Generated or updated based on variables, user input, or data    |
| **Interaction-driven**    | Responds to user actions (e.g., forms, searches)                |
| **Uses scripting**        | Server-side (e.g., PHP) or client-side (e.g., JavaScript)       |
| **Often database-backed** | Retrieves, updates, or displays data from databases             |
| **Customizable per user** | Can generate personalized content (e.g., greetings, dashboards) |

---

### **3. Generation Methods**

---

#### **1. Server-Side Scripting**

* Content generated **on the server** before being sent to the browser.
* Scripting languages like:

  * **PHP**
  * **Python (Django, Flask)**
  * **Node.js**
  * **Java (JSP, Servlets)**
  * **Ruby on Rails**
* Example: `index.php`, `home.jsp`

---

#### **2. Client-Side Scripting**

* Content modified or generated **in the browser** after the page loads.
* Language used: **JavaScript**
* Uses DOM manipulation and AJAX for dynamic behavior.
* Example: Content updated without reloading the entire page.

---

#### **3. Hybrid (Server + Client Side)**

* Initial page rendered by server-side logic.
* Additional content or interactivity provided by client-side JavaScript.
* Common in modern **Single Page Applications (SPA)**.

---

### **4. Examples of Dynamic Web Documents**

| Example                           | Description                                       |
| --------------------------------- | ------------------------------------------------- |
| **User dashboards**               | Personalized content fetched after login          |
| **Search results pages**          | Dynamically fetched from server/database          |
| **Social media feeds**            | Updates with latest posts, likes, and comments    |
| **E-commerce product pages**      | Prices, stock levels, reviews fetched dynamically |
| **Interactive forms and surveys** | Adapt based on user input                         |

---

### **5. Technologies Used**

| Layer           | Tools/Technologies                         |
| --------------- | ------------------------------------------ |
| **Server-side** | PHP, Python (Flask/Django), Node.js, JSP   |
| **Client-side** | HTML, CSS, JavaScript, AJAX                |
| **Databases**   | MySQL, PostgreSQL, MongoDB, etc.           |
| **Web Servers** | Apache, Nginx, Express.js                  |
| **Frameworks**  | React, Angular, Vue (for client-side apps) |

---

### **6. Advantages**

| Advantage                   | Description                                              |
| --------------------------- | -------------------------------------------------------- |
| **Interactive**             | Responds to user actions, improves user experience       |
| **Personalized**            | Customizes content per session/user                      |
| **Real-time updates**       | Supports asynchronous content loading (e.g., live chats) |
| **Efficient data handling** | Integrates with databases for data retrieval and display |

---

### **7. Disadvantages**

| Disadvantage                  | Description                                               |
| ----------------------------- | --------------------------------------------------------- |
| **Slower load times**         | Server processing time required                           |
| **Requires server resources** | More computation than static pages                        |
| **Complex to develop**        | Needs integration of scripts, databases, security         |
| **Security risks**            | Prone to SQL injection, XSS, CSRF if not properly secured |

---

### **8. Dynamic vs Static Web Document**

| Feature             | Static Web Document | Dynamic Web Document                     |
| ------------------- | ------------------- | ---------------------------------------- |
| **Content**         | Fixed               | Generated on-the-fly                     |
| **Scripting**       | No scripting        | Uses server-side/client-side scripting   |
| **Personalization** | Not possible        | Possible                                 |
| **Interaction**     | Limited             | Highly interactive                       |
| **Data Handling**   | No real-time data   | Supports databases and real-time content |

---

### **9. Example Workflow**

1. User visits `products.php`.
2. Server executes script:

   * Connects to database.
   * Retrieves product info.
   * Embeds data into HTML.
3. Server sends the final HTML page to the browser.
4. Browser displays it.
5. JavaScript may enhance the page with AJAX (e.g., load more products on scroll).

---

### **10. Summary Table**

| Attribute              | Description                                             |
| ---------------------- | ------------------------------------------------------- |
| **Purpose**            | To provide dynamic, responsive, personalized content    |
| **Execution location** | Server-side and/or client-side                          |
| **Languages used**     | PHP, JavaScript, Python, etc.                           |
| **Depends on data**    | Yes, often from databases                               |
| **Common uses**        | Search, forms, shopping carts, social media, dashboards |

---

### **HTTP (HyperText Transfer Protocol)**

---

### **1. Definition**

* **HTTP (Hypertext Transfer Protocol)** is an **application-layer protocol** used for **transferring hypermedia documents** (like HTML) between web browsers (clients) and web servers.
* It is a **request-response protocol** following the **client-server model**.
* Standardized by **IETF** in **RFC 2616** (HTTP/1.1) and later updated in **RFC 7230–7235** and **RFC 7540** (HTTP/2).

---

### **2. Key Characteristics**

| Feature               | Description                                                     |
| --------------------- | --------------------------------------------------------------- |
| **Protocol Type**     | Application Layer (uses TCP)                                    |
| **Port Number**       | Default: **80** (HTTP), **443** (HTTPS)                         |
| **Stateless**         | Each request is **independent**; no memory of previous requests |
| **Media Independent** | Can transfer any type of data (text, images, audio, video)      |
| **Extensible**        | Supports additional features via headers (cookies, caching)     |

---

### **3. Versions of HTTP**

| Version      | Description                                                           |
| ------------ | --------------------------------------------------------------------- |
| **HTTP/0.9** | Simple, GET-only support, no headers                                  |
| **HTTP/1.0** | Added headers, POST, status codes                                     |
| **HTTP/1.1** | Persistent connections, chunked transfer, pipelining                  |
| **HTTP/2**   | Multiplexing, header compression, binary framing                      |
| **HTTP/3**   | Based on **QUIC** (UDP), faster performance and connection management |

---

### **4. HTTP Request Structure**

| Section          | Description                                                              |
| ---------------- | ------------------------------------------------------------------------ |
| **Request Line** | Method (e.g., GET), URL, HTTP version (e.g., `GET /index.html HTTP/1.1`) |
| **Headers**      | Metadata (e.g., Host, User-Agent, Accept, Content-Type)                  |
| **Blank Line**   | Indicates end of headers                                                 |
| **Body**         | Optional (for POST/PUT) – contains form data or payload                  |

---

#### **Example Request**

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

---

### **5. HTTP Response Structure**

| Section         | Description                                                        |
| --------------- | ------------------------------------------------------------------ |
| **Status Line** | HTTP version, status code, reason phrase (e.g., `HTTP/1.1 200 OK`) |
| **Headers**     | Metadata (Content-Type, Content-Length, etc.)                      |
| **Blank Line**  | End of headers                                                     |
| **Body**        | The content (HTML, JSON, etc.)                                     |

---

#### **Example Response**

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1024

<html>
  <body>Hello, World!</body>
</html>
```

---

### **6. HTTP Methods (Verbs)**

| Method      | Purpose                            |
| ----------- | ---------------------------------- |
| **GET**     | Retrieve data (no body in request) |
| **POST**    | Submit data to be processed        |
| **PUT**     | Update existing data               |
| **DELETE**  | Remove a resource                  |
| **HEAD**    | Like GET, but returns headers only |
| **OPTIONS** | Describe communication options     |
| **PATCH**   | Partial resource update            |

---

### **7. HTTP Status Codes**

| Class   | Range   | Description                              |
| ------- | ------- | ---------------------------------------- |
| **1xx** | 100–199 | Informational responses                  |
| **2xx** | 200–299 | Success (e.g., 200 OK, 201 Created)      |
| **3xx** | 300–399 | Redirection (e.g., 301 Moved, 302 Found) |
| **4xx** | 400–499 | Client error (e.g., 404 Not Found)       |
| **5xx** | 500–599 | Server error (e.g., 500 Internal Error)  |

---

### **8. Common HTTP Headers**

| Header            | Description                                    |
| ----------------- | ---------------------------------------------- |
| **Host**          | Specifies the domain name                      |
| **User-Agent**    | Identifies the client software                 |
| **Content-Type**  | Specifies media type of body (e.g., text/html) |
| **Accept**        | Client’s preferred response formats            |
| **Set-Cookie**    | Instructs browser to store a cookie            |
| **Cache-Control** | Controls caching behavior                      |

---

### **9. Persistent Connections (Keep-Alive)**

* **HTTP/1.1** introduced **persistent connections**:

  * A single TCP connection is used for multiple requests/responses.
  * Reduces overhead of establishing new connections.

---

### **10. Pipelining (HTTP/1.1)**

* Multiple HTTP requests can be sent without waiting for responses.
* Reduces latency but not widely used due to **head-of-line blocking**.

---

### **11. Multiplexing (HTTP/2)**

* **Parallel requests** on a single connection.
* **Binary framing** protocol.
* Reduces latency and improves performance over HTTP/1.1.

---

### **12. HTTPS (HTTP Secure)**

* HTTP over **TLS/SSL** (port 443).
* Provides:

  * **Confidentiality** (encryption)
  * **Integrity** (data not altered)
  * **Authentication** (server identity)

---

### **13. HTTP Caching**

| Header            | Function                                  |
| ----------------- | ----------------------------------------- |
| **ETag**          | Entity tag for validating cached response |
| **Last-Modified** | Timestamp of last modification            |
| **Cache-Control** | Directs caching behavior                  |
| **Expires**       | Date/time after which response is stale   |

---

### **14. Cookies in HTTP**

* Stored as **name-value** pairs.
* Used for:

  * **Session tracking**
  * **User preferences**
  * **Authentication**

---

### **15. Summary Table**

| Attribute         | HTTP Details                               |
| ----------------- | ------------------------------------------ |
| **Protocol Type** | Application Layer                          |
| **Default Port**  | 80 (HTTP), 443 (HTTPS)                     |
| **Methods**       | GET, POST, PUT, DELETE, etc.               |
| **Status Codes**  | 200 OK, 404 Not Found, 500 Internal Server |
| **Connection**    | Stateless; persistent with HTTP/1.1+       |
| **Security**      | Added by HTTPS using TLS                   |
| **Versions**      | HTTP/0.9, 1.0, 1.1, 2, 3                   |
| **Used By**       | Web browsers and APIs                      |

---

### **Application Layer Protocols**

---

### **1. Definition**

* **Application layer protocols** are protocols that operate at the **top layer** (Layer 7) of the **OSI model** and directly support **end-user services and applications**.
* These protocols define how software applications **communicate over the network** and **exchange data**.

---

### **2. Functions of Application Layer Protocols**

| Function                       | Description                                                     |
| ------------------------------ | --------------------------------------------------------------- |
| **Network Virtual Terminal**   | Provides standard interface for remote communication            |
| **Data Encoding**              | Translates data between application and network formats         |
| **Dialog Control**             | Manages communication sessions (e.g., half-duplex, full-duplex) |
| **Access Control**             | Determines user authorization                                   |
| **Error Detection/Correction** | Ensures message accuracy during transmission                    |

---

### **3. Key Application Layer Protocols**

---

### **1. Simple Network Management Protocol (SNMP)**

| Feature        | Description                                                    |
| -------------- | -------------------------------------------------------------- |
| **Purpose**    | Monitors and manages network devices (e.g., routers, switches) |
| **Port**       | UDP **161 (Agent)**, **162 (Manager)**                         |
| **Model**      | Manager-Agent                                                  |
| **Components** | SNMP Manager, SNMP Agent, MIB (Management Information Base)    |
| **Operations** | GET, SET, GETNEXT, TRAP                                        |

---

### **2. File Transfer Protocol (FTP)**

| Feature            | Description                               |
| ------------------ | ----------------------------------------- |
| **Purpose**        | Transfers files between client and server |
| **Port**           | TCP **20 (Data)**, **21 (Control)**       |
| **Connection**     | Requires two separate TCP connections     |
| **Authentication** | Supports username/password login          |
| **Modes**          | Active and Passive FTP                    |

---

### **3. Simple Mail Transfer Protocol (SMTP)**

| Feature         | Description                                           |
| --------------- | ----------------------------------------------------- |
| **Purpose**     | Sends emails from client to server or between servers |
| **Port**        | TCP **25** (also 587 for client submission)           |
| **Type**        | Push protocol                                         |
| **Use with**    | Used with POP3/IMAP for retrieval                     |
| **Limitations** | Cannot retrieve or store emails                       |

---

### **4. Hypertext Transfer Protocol (HTTP)**

| Feature            | Description                         |
| ------------------ | ----------------------------------- |
| **Purpose**        | Transfers web pages (HTML, CSS, JS) |
| **Port**           | TCP **80** (HTTP), **443** (HTTPS)  |
| **Type**           | Stateless, request-response model   |
| **Methods**        | GET, POST, PUT, DELETE, etc.        |
| **Secure Version** | HTTPS (uses SSL/TLS)                |

---

### **5. Domain Name System (DNS)**

| Feature          | Description                            |
| ---------------- | -------------------------------------- |
| **Purpose**      | Resolves domain names to IP addresses  |
| **Port**         | UDP/TCP **53**                         |
| **Record Types** | A, AAAA, CNAME, MX, NS, PTR, TXT       |
| **Hierarchy**    | Root → TLD → Authoritative nameservers |

---

### **6. Post Office Protocol version 3 (POP3)**

| Feature      | Description                                       |
| ------------ | ------------------------------------------------- |
| **Purpose**  | Retrieves emails from mail server                 |
| **Port**     | TCP **110** (995 for POP3S)                       |
| **Behavior** | Downloads and deletes mail from server by default |
| **Use Case** | Suitable for single-device access                 |

---

### **7. Internet Message Access Protocol (IMAP)**

| Feature      | Description                                     |
| ------------ | ----------------------------------------------- |
| **Purpose**  | Retrieves and manages email on the server       |
| **Port**     | TCP **143** (993 for IMAPS)                     |
| **Behavior** | Syncs mail across devices, keeps copy on server |
| **Use Case** | Multi-device access                             |

---

### **8. Dynamic Host Configuration Protocol (DHCP)**

| Feature        | Description                                   |
| -------------- | --------------------------------------------- |
| **Purpose**    | Automatically assigns IP addresses to clients |
| **Port**       | UDP **67 (Server)**, **68 (Client)**          |
| **Process**    | DORA (Discover, Offer, Request, Acknowledge)  |
| **Lease Time** | IP address assigned for a fixed duration      |

---

### **9. Telnet**

| Feature         | Description                              |
| --------------- | ---------------------------------------- |
| **Purpose**     | Remote login to command-line interface   |
| **Port**        | TCP **23**                               |
| **Security**    | Not secure, transmits data in plain text |
| **Replaced by** | SSH (Secure Shell)                       |

---

### **10. Secure Shell (SSH)**

| Feature        | Description                                 |
| -------------- | ------------------------------------------- |
| **Purpose**    | Secure remote login and file transfer       |
| **Port**       | TCP **22**                                  |
| **Encryption** | Yes, provides confidentiality and integrity |

---

### **11. BOOTP (Bootstrap Protocol)**

| Feature        | Description                                         |
| -------------- | --------------------------------------------------- |
| **Purpose**    | Predecessor to DHCP, assigns IP to diskless devices |
| **Port**       | UDP **67/68**                                       |
| **Limitation** | Manual configuration required for new clients       |

---

### **12. Trivial File Transfer Protocol (TFTP)**

| Feature            | Description                                      |
| ------------------ | ------------------------------------------------ |
| **Purpose**        | Simplified version of FTP for file transfer      |
| **Port**           | UDP **69**                                       |
| **Authentication** | No authentication or directory support           |
| **Use Case**       | Used in booting and routers/switch configuration |

---

### **13. Gopher (Historical)**

| Feature     | Description                                    |
| ----------- | ---------------------------------------------- |
| **Purpose** | Early alternative to WWW, menu-based interface |
| **Status**  | Largely obsolete                               |

---

### **14. Summary Table**

| Protocol | Purpose                           | Port(s)       | Transport | Functionality                 |
| -------- | --------------------------------- | ------------- | --------- | ----------------------------- |
| SNMP     | Network management                | 161, 162      | UDP       | Monitor and control devices   |
| FTP      | File transfer                     | 20 (data), 21 | TCP       | Upload/download files         |
| SMTP     | Email sending                     | 25, 587       | TCP       | Send email                    |
| HTTP     | Web content                       | 80            | TCP       | Load websites                 |
| HTTPS    | Secure web content                | 443           | TCP       | Secure HTTP                   |
| DNS      | Domain name resolution            | 53            | UDP/TCP   | Converts domain names to IPs  |
| POP3     | Email retrieval                   | 110           | TCP       | Download and delete email     |
| IMAP     | Email synchronization             | 143           | TCP       | View/manage email on server   |
| DHCP     | IP address assignment             | 67, 68        | UDP       | Dynamic IP configuration      |
| Telnet   | Remote terminal access (insecure) | 23            | TCP       | Command-line access           |
| SSH      | Secure remote terminal access     | 22            | TCP       | Secure login, file transfer   |
| TFTP     | Lightweight file transfer         | 69            | UDP       | Simple file sending/receiving |

---

### **Simple Network Management Protocol (SNMP)**

---

### **1. Definition**

* **SNMP (Simple Network Management Protocol)** is an **application layer protocol** used for **monitoring and managing network devices** like routers, switches, firewalls, printers, and servers.
* It allows **centralized management** of network performance, detection of faults, and configuration of remote devices.

---

### **2. Purpose**

* **Monitor** network performance (e.g., bandwidth usage, CPU load).
* **Detect** and **resolve faults** (e.g., link failures, device errors).
* **Configure** devices remotely (e.g., change interface status).
* **Collect statistics** from devices.

---

### **3. SNMP Model**

| Component                             | Description                                                                         |
| ------------------------------------- | ----------------------------------------------------------------------------------- |
| **SNMP Manager**                      | Central system (e.g., network monitoring software) that controls SNMP communication |
| **SNMP Agent**                        | Program running on managed devices; responds to manager's queries                   |
| **MIB (Management Information Base)** | Hierarchical database of all manageable resources on the device                     |
| **Managed Device**                    | Network device being monitored/managed (e.g., router, switch)                       |

---

### **4. Architecture**

* SNMP follows a **Manager-Agent architecture**:

  * The **Manager** sends **requests** to the **Agent**.
  * The **Agent** responds with **data** or **status**.
  * The Agent can also send **Traps** to notify the Manager of critical events.

---

### **5. SNMP Operations**

| Operation   | Description                                                       |
| ----------- | ----------------------------------------------------------------- |
| **GET**     | Requests the value of a variable from an agent                    |
| **GETNEXT** | Requests the next variable in the MIB tree                        |
| **SET**     | Changes the value of a variable on the agent                      |
| **TRAP**    | Agent-initiated alert sent to the manager                         |
| **INFORM**  | Like TRAP but expects acknowledgment from the manager             |
| **GETBULK** | Retrieves large blocks of data efficiently (introduced in SNMPv2) |

---

### **6. Management Information Base (MIB)**

* A **virtual database** used by SNMP to **describe and store device parameters**.
* Organized as a **tree structure** with **Object Identifiers (OIDs)**.
* Each OID represents a **specific parameter** (e.g., system uptime, interface status).

**Example MIB Entry:**

* OID: `1.3.6.1.2.1.1.3.0` → System uptime
* OID: `1.3.6.1.2.1.2.2.1.10.1` → Incoming bytes on interface 1

---

### **7. SNMP Versions**

| Version     | Features                                                           |
| ----------- | ------------------------------------------------------------------ |
| **SNMPv1**  | Basic features, uses community strings (e.g., "public", "private") |
| **SNMPv2c** | Adds GETBULK and INFORM; still uses community strings              |
| **SNMPv3**  | Adds **security**: authentication, encryption, and access control  |

---

### **8. SNMP Message Format**

| Field                 | Description                            |
| --------------------- | -------------------------------------- |
| **Version**           | SNMP version (1, 2c, 3)                |
| **Community String**  | Like a password to control access      |
| **PDU Type**          | Request/Response type (GET, SET, etc.) |
| **Variable Bindings** | List of OIDs and their values          |

---

### **9. Community Strings (v1 and v2c)**

| String    | Access Type       |
| --------- | ----------------- |
| `public`  | Read-only access  |
| `private` | Read-write access |

---

### **10. SNMP Security in v3**

| Security Feature   | Description                               |
| ------------------ | ----------------------------------------- |
| **Authentication** | Verifies sender identity (e.g., MD5, SHA) |
| **Encryption**     | Protects data in transit (e.g., DES, AES) |
| **Access Control** | Limits access to specific MIB objects     |

---

### **11. SNMP Ports**

| Port Number | Protocol | Description                          |
| ----------- | -------- | ------------------------------------ |
| **161**     | UDP      | Used by agents for receiving queries |
| **162**     | UDP      | Used by managers to receive traps    |

---

### **12. SNMP Agent Behavior**

1. **Waits** for queries from the manager on UDP port 161.
2. **Responds** with current values from its MIB.
3. **Sends TRAPs** on port 162 when specific events occur (e.g., device reboot).

---

### **13. SNMP Use Cases**

| Use Case                           | Description                                       |
| ---------------------------------- | ------------------------------------------------- |
| **Network Performance Monitoring** | Track bandwidth, latency, and uptime              |
| **Fault Detection**                | Alert when device fails or link goes down         |
| **Configuration Management**       | Enable/disable interfaces, set IP addresses       |
| **Inventory Management**           | Track types and numbers of devices in the network |

---

### **14. Advantages**

| Advantage                | Description                                    |
| ------------------------ | ---------------------------------------------- |
| **Lightweight**          | Uses simple UDP-based messages                 |
| **Scalable**             | Can monitor thousands of devices               |
| **Real-time alerts**     | TRAPs notify manager immediately of issues     |
| **Platform-independent** | Supported by almost all network device vendors |

---

### **15. Limitations**

| Limitation              | Description                                          |
| ----------------------- | ---------------------------------------------------- |
| **Security (v1, v2c)**  | Community strings sent in plain text                 |
| **Limited Data Format** | Only simple data types (integers, strings, counters) |
| **Lacks Reliability**   | UDP messages may be lost                             |

---

### **16. Summary Table**

| Attribute           | SNMP Details                                       |
| ------------------- | -------------------------------------------------- |
| **Layer**           | Application Layer                                  |
| **Architecture**    | Manager-Agent                                      |
| **Main Components** | SNMP Manager, SNMP Agent, MIB                      |
| **Operations**      | GET, SET, GETNEXT, GETBULK, TRAP, INFORM           |
| **Versions**        | SNMPv1, SNMPv2c, SNMPv3                            |
| **Security**        | Present only in SNMPv3                             |
| **Ports**           | 161 (agent), 162 (trap)                            |
| **Protocol Used**   | UDP                                                |
| **Use Cases**       | Network monitoring, configuration, fault detection |

---

### **File Transfer Protocol (FTP)**

---

### **1. Definition**

* **FTP (File Transfer Protocol)** is a **standard network protocol** used to **transfer files** between a **client** and a **server** on a **TCP/IP network**.
* Defined by **RFC 959**, FTP is an **application layer protocol** that uses **TCP** for reliable data transmission.

---

### **2. Purpose**

* **Upload** files from client to server.
* **Download** files from server to client.
* **Manage files remotely** (rename, delete, list, etc.).

---

### **3. FTP Architecture**

| Component              | Description                                        |
| ---------------------- | -------------------------------------------------- |
| **FTP Client**         | Initiates connection and requests files            |
| **FTP Server**         | Responds to client requests and provides files     |
| **Control Connection** | Used to send commands and responses (Port 21)      |
| **Data Connection**    | Used to transfer actual files (Port 20 or dynamic) |

---

### **4. FTP Ports**

| Port   | Usage                                    |
| ------ | ---------------------------------------- |
| **21** | Control connection (commands, responses) |
| **20** | Data connection (for Active Mode only)   |

---

### **5. FTP Modes**

#### **1. Active Mode**

* Client opens a random port and sends it to server via control connection.
* Server initiates data connection from its port 20 to the client's random port.

#### **2. Passive Mode**

* Server opens a random port for data connection.
* Client initiates the data connection to that port.
* Used when client is behind firewall/NAT.

---

### **6. FTP Connection Process**

1. Client connects to server on port 21.
2. Server responds with welcome message.
3. Client sends **login credentials** (username and password).
4. Server authenticates user.
5. Control connection established.
6. Data connection initiated as per mode (active/passive).
7. File transfer operations are executed.

---

### **7. FTP Commands**

| Command | Description                  |
| ------- | ---------------------------- |
| `USER`  | Sends username               |
| `PASS`  | Sends password               |
| `LIST`  | Lists files and directories  |
| `RETR`  | Retrieves a file from server |
| `STOR`  | Uploads a file to server     |
| `DELE`  | Deletes a file               |
| `CWD`   | Changes working directory    |
| `PWD`   | Prints current directory     |
| `QUIT`  | Ends the session             |

---

### **8. FTP Response Codes**

| Code Class | Range   | Description                                  |
| ---------- | ------- | -------------------------------------------- |
| **1xx**    | 100–199 | Positive Preliminary reply                   |
| **2xx**    | 200–299 | Positive Completion reply                    |
| **3xx**    | 300–399 | Positive Intermediate reply (need more info) |
| **4xx**    | 400–499 | Transient Negative Completion reply          |
| **5xx**    | 500–599 | Permanent Negative Completion reply          |

**Examples:**

* `220`: Service ready for new user
* `331`: Username okay, need password
* `226`: Closing data connection (file transfer successful)

---

### **9. FTP Authentication**

* **Anonymous FTP**: User logs in using "anonymous" as the username.
* **Authenticated FTP**: Requires valid username and password.

---

### **10. Security Concerns**

| Issue                       | Description                                   |
| --------------------------- | --------------------------------------------- |
| **Plaintext login**         | Credentials sent without encryption           |
| **Unencrypted data**        | All data, including files, sent in plain text |
| **Susceptible to sniffing** | Can be intercepted by attackers               |

---

### **11. Secure FTP Alternatives**

| Protocol  | Description                                        |
| --------- | -------------------------------------------------- |
| **FTPS**  | FTP over **SSL/TLS** (adds encryption)             |
| **SFTP**  | **SSH File Transfer Protocol**, not related to FTP |
| **HTTPS** | Uses HTTP over TLS for file uploads/downloads      |

---

### **12. Use Cases**

| Use Case                   | Description                                        |
| -------------------------- | -------------------------------------------------- |
| **Website deployment**     | Uploading web pages to hosting server              |
| **Backup and restoration** | Transferring data between local and remote systems |
| **Large file exchange**    | Sharing media or archives                          |
| **Remote file management** | Listing, moving, renaming files remotely           |

---

### **13. FTP Client Software**

| Type              | Examples                              |
| ----------------- | ------------------------------------- |
| **GUI-based**     | FileZilla, WinSCP, Cyberduck          |
| **Command-line**  | `ftp`, `lftp`, `ncftp`                |
| **Browser-based** | `ftp://` links in some older browsers |

---

### **14. FTP vs HTTP (Comparison)**

| Feature            | FTP                       | HTTP                         |
| ------------------ | ------------------------- | ---------------------------- |
| **Purpose**        | File transfer             | Web content delivery         |
| **Authentication** | Yes                       | Optional (basic, token)      |
| **Data Type**      | Files                     | Hypermedia (HTML, CSS, JS)   |
| **Connections**    | Separate control and data | Single persistent connection |
| **Security**       | None by default           | Encrypted via HTTPS          |

---

### **15. Summary Table**

| Attribute           | Description                                           |
| ------------------- | ----------------------------------------------------- |
| **Protocol Type**   | Application Layer                                     |
| **Defined In**      | RFC 959                                               |
| **Transport Layer** | Uses **TCP**                                          |
| **Ports**           | 21 (control), 20 (data - active mode)                 |
| **Modes**           | Active and Passive                                    |
| **Operations**      | Upload, Download, Rename, Delete                      |
| **Security**        | No encryption by default (use FTPS/SFTP for security) |
| **Use Cases**       | File sharing, backups, web hosting                    |

---

### **Simple Mail Transfer Protocol (SMTP)**

---

### **1. Definition**

* **SMTP (Simple Mail Transfer Protocol)** is an **application layer protocol** used for **sending and routing emails** between **email clients and servers** or between **mail servers**.
* Defined in **RFC 5321** (replacing the older RFC 821).
* SMTP is a **push protocol**, meaning it **initiates** the transfer of emails.

---

### **2. Purpose**

| Function                   | Description                                            |
| -------------------------- | ------------------------------------------------------ |
| **Send Emails**            | From user agent to mail server or between mail servers |
| **Relay Messages**         | Between mail servers across domains                    |
| **Delivery Notifications** | Returns errors or delivery reports to the sender       |

---

### **3. SMTP Architecture**

| Component                     | Description                                                                |
| ----------------------------- | -------------------------------------------------------------------------- |
| **User Agent (UA)**           | Application used to compose/send (e.g., Outlook, Thunderbird)              |
| **Mail Transfer Agent (MTA)** | Responsible for forwarding and delivering emails (e.g., Sendmail, Postfix) |
| **Mail Delivery Agent (MDA)** | Receives emails from MTA and stores them (e.g., Procmail, Dovecot)         |

---

### **4. SMTP Ports**

| Port    | Description                                                                  |
| ------- | ---------------------------------------------------------------------------- |
| **25**  | Default port for server-to-server communication                              |
| **587** | Submission port for sending mail from client to server (with authentication) |
| **465** | Deprecated port (was used for SMTP over SSL)                                 |

---

### **5. SMTP Commands**

| Command     | Description                                            |
| ----------- | ------------------------------------------------------ |
| `HELO`      | Identify the client to the server                      |
| `EHLO`      | Extended version of HELO (SMTP extensions)             |
| `MAIL FROM` | Specifies the sender's email address                   |
| `RCPT TO`   | Specifies the recipient’s email address                |
| `DATA`      | Indicates the start of the message body                |
| `RSET`      | Resets the current session                             |
| `VRFY`      | Verifies the existence of an address (may be disabled) |
| `QUIT`      | Terminates the SMTP session                            |

---

### **6. SMTP Communication Process**

1. Client connects to server on port 25 or 587.
2. Server responds with a 220 (Service ready) code.
3. Client sends `HELO` or `EHLO`.
4. Server acknowledges.
5. Client sends `MAIL FROM:<sender>`.
6. Client sends `RCPT TO:<receiver>`.
7. Client sends `DATA`, followed by message body and a line with just `.` to end.
8. Server responds with 250 (OK).
9. Client sends `QUIT`.

---

### **7. SMTP Response Codes**

| Code | Description                                      |
| ---- | ------------------------------------------------ |
| 220  | Service ready                                    |
| 250  | Requested action completed                       |
| 354  | Start mail input; end with `.` on a line         |
| 421  | Service not available                            |
| 450  | Requested action not taken                       |
| 550  | Requested action not taken – mailbox unavailable |
| 500  | Syntax error                                     |

---

### **8. SMTP Message Format**

| Section    | Description                            |
| ---------- | -------------------------------------- |
| **Header** | To, From, Subject, Date, MIME headers  |
| **Body**   | Actual message content (plain or HTML) |

---

### **9. SMTP Features**

| Feature                 | Description                                           |
| ----------------------- | ----------------------------------------------------- |
| **Text-based protocol** | Commands and responses are plain text                 |
| **Reliable delivery**   | Uses TCP, ensures ordered delivery                    |
| **Queueing**            | Temporarily stores undeliverable mail for retry       |
| **Extensions (ESMTP)**  | Adds features like authentication, 8BITMIME, STARTTLS |

---

### **10. SMTP Authentication**

* Used to prevent spam and unauthorized mail sending.
* Typically used on port 587 (with STARTTLS).
* Requires valid **username and password**.
* Authentication mechanisms include:

  * PLAIN
  * LOGIN
  * CRAM-MD5
  * DIGEST-MD5

---

### **11. SMTP Security**

| Security Mechanism | Description                                       |
| ------------------ | ------------------------------------------------- |
| **STARTTLS**       | Upgrades plain connection to encrypted            |
| **SSL/TLS**        | Encrypts communication (port 465 used previously) |
| **SPF/DKIM/DMARC** | Protects against spoofing and spam                |

---

### **12. SMTP vs Other Email Protocols**

| Feature          | SMTP           | POP3                           | IMAP                        |
| ---------------- | -------------- | ------------------------------ | --------------------------- |
| **Used for**     | Sending emails | Receiving emails               | Receiving + managing emails |
| **Direction**    | Outgoing       | Incoming                       | Incoming                    |
| **Port**         | 25, 587, 465   | 110, 995                       | 143, 993                    |
| **Stores mail?** | No             | Downloads + deletes by default | Keeps mail on server        |

---

### **13. Use Cases**

| Use Case                      | Description                                |
| ----------------------------- | ------------------------------------------ |
| **Sending email from app**    | Applications like contact forms use SMTP   |
| **Mail server communication** | Transfers email from one domain to another |
| **Automated email alerts**    | Sends notifications, newsletters, OTPs     |

---

### **14. Summary Table**

| Attribute              | SMTP Details                                        |
| ---------------------- | --------------------------------------------------- |
| **Full Form**          | Simple Mail Transfer Protocol                       |
| **Layer**              | Application Layer                                   |
| **Protocol Type**      | Push protocol (sending only)                        |
| **Transport Protocol** | TCP                                                 |
| **Ports**              | 25, 587 (modern), 465 (deprecated for SMTPS)        |
| **Authentication**     | Optional (required on port 587)                     |
| **Security**           | STARTTLS, SSL/TLS, SPF/DKIM/DMARC                   |
| **Status Codes**       | 220 (ready), 250 (OK), 354 (start data), 550 (fail) |
| **Used With**          | POP3/IMAP for retrieving emails                     |

---

