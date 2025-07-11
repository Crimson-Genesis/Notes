# Unit - 2 -> The data link layer
* The Data Link Layer: Design issues, error detection and correction, elementary data link protocals, sliding window protocals, example data link protocals - HDLC, the data link layer in the internet.
* The Medium Access SubLayer: Channel allocations problem, multiple access protocols, Ethernet, Data Link Layer switching, Wireless LAN, Broadband Wireless, Blurtooth.

## Content ->
### **The Data Link Layer**

---

#### **1. Definition**

* The **Data Link Layer** is **Layer 2** of the **OSI (Open Systems Interconnection)** model.
* It is responsible for **node-to-node delivery** of data across a physical link in a network.
* Converts raw transmission data (from the physical layer) into a reliable link by **framing, error detection, and flow control**.

---

### **2. Major Responsibilities**

---

#### **A. Framing**

* Divides the data stream into manageable **frames**.
* Adds headers and trailers to identify frame boundaries.

#### **B. Addressing**

* Adds **MAC (Media Access Control)** addresses to each frame.
* Ensures data is delivered to the correct physical device on a LAN.

#### **C. Error Detection and Correction**

* Detects errors caused during transmission (using checksums, CRC, etc.).
* In some protocols, also corrects these errors (e.g., Hamming code, ARQ).

#### **D. Flow Control**

* Prevents a fast sender from overwhelming a slow receiver.
* Common mechanisms: **Stop-and-Wait**, **Sliding Window**.

#### **E. Access Control**

* Determines which device has the right to use the physical medium when multiple devices are connected.
* Important in **shared media** (like Ethernet or Wi-Fi).

---

### **3. Sub-Layers of the Data Link Layer**

---

#### **A. Logical Link Control (LLC) Sub-layer**

* Manages communication between the **network layer and the MAC sub-layer**.
* Provides:

  * Flow control
  * Error checking
  * Frame synchronization

#### **B. Media Access Control (MAC) Sub-layer**

* Controls how devices **access the physical medium**.
* Defines:

  * MAC addressing
  * Frame format
  * Channel access methods

---

### **4. Functions of the Data Link Layer**

| Function              | Description                                       |
| --------------------- | ------------------------------------------------- |
| Framing               | Divide bit stream into frames                     |
| Physical Addressing   | Adds MAC address to identify sender/receiver      |
| Error Control         | Uses checksums or CRC to detect/correct errors    |
| Flow Control          | Controls data rate between sender and receiver    |
| Access Control        | Manages access to shared media                    |
| Frame Synchronization | Ensures frames are correctly aligned and detected |

---

### **5. Communication Types at Data Link Layer**

| Type      | Description                           |
| --------- | ------------------------------------- |
| Unicast   | One-to-one communication              |
| Broadcast | One-to-all (e.g., ARP request in LAN) |
| Multicast | One-to-many selected group of devices |

---

### **6. Data Unit**

| Layer           | Data Unit Name |
| --------------- | -------------- |
| Data Link Layer | **Frame**      |

Each frame consists of:

* **Header**: Contains source/destination MAC, control info
* **Payload**: Actual data from network layer
* **Trailer**: Error checking (e.g., CRC)

---

### **7. Devices Operating at Data Link Layer**

| Device                       | Function                                  |
| ---------------------------- | ----------------------------------------- |
| Switch                       | Forwards frames based on MAC address      |
| Bridge                       | Connects and filters LAN segments         |
| Network Interface Card (NIC) | Provides MAC address and access to medium |

---

### **8. Relationship with Other Layers**

| Layer           | Interaction                                                    |
| --------------- | -------------------------------------------------------------- |
| Physical Layer  | Sends/receives actual bits                                     |
| Network Layer   | Sends/receives packets (IP layer)                              |
| Data Link Layer | Converts packets into frames and ensures reliable transmission |

---

### **9. Protocols at Data Link Layer**

| Protocol            | Description                                 |
| ------------------- | ------------------------------------------- |
| HDLC                | High-Level Data Link Control (bit-oriented) |
| PPP                 | Point-to-Point Protocol for direct links    |
| Ethernet            | Popular LAN protocol using MAC addresses    |
| Wi-Fi (IEEE 802.11) | Wireless LAN MAC layer protocol             |

---

### **10. Summary Table**

| Feature           | Description                                            |
| ----------------- | ------------------------------------------------------ |
| Layer             | 2nd layer in OSI model                                 |
| Data Unit         | Frame                                                  |
| Address Used      | MAC address                                            |
| Key Functions     | Framing, Error Detection, Flow Control, MAC Access     |
| Sub-layers        | LLC (Logical Link Control), MAC (Media Access Control) |
| Devices           | Switch, Bridge, NIC                                    |
| Protocol Examples | Ethernet, HDLC, PPP, Wi-Fi                             |

---

### **Design Issues in the Data Link Layer**

---

The design of the Data Link Layer must address several critical issues to ensure **reliable, efficient, and accurate communication** between directly connected devices. These issues define how the layer manages **framing, error handling, synchronization, addressing, flow control**, and **medium access**.

---

### **1. Framing**

#### ❖ Problem:

* The receiver must identify **where a frame starts and ends** within a continuous stream of bits.

#### ❖ Solutions:

* **Character Count**: Frame starts with a byte that specifies the number of characters.

  * Problem: If count field gets corrupted, sync is lost.
* **Byte Stuffing**:

  * Uses special delimiter (e.g., `FLAG`) and escapes it if found in data.
  * Example: HDLC uses `01111110` as a flag.
* **Bit Stuffing**:

  * Insert a `0` after every five consecutive `1`s in the data to prevent false flag detection.
* **Physical Layer Coding Violations**:

  * Special patterns not used in normal data are used to indicate frame boundaries.

---

### **2. Error Control**

#### ❖ Problem:

* During transmission, bits may flip due to noise or interference.

#### ❖ Requirements:

* **Detect** errors.
* **Correct** errors (optional depending on protocol).

#### ❖ Solutions:

* **Parity Bit**: Adds 1 bit to make the number of 1’s even or odd.
* **Checksums**: Sum of all data bytes sent; the receiver checks the total.
* **Cyclic Redundancy Check (CRC)**: Polynomial-based error detection (very reliable).
* **Error-Correcting Codes**:

  * **Hamming Code**: Detects and corrects single-bit errors.
  * **Automatic Repeat Request (ARQ)**: Uses acknowledgments (ACK/NACK) and retransmissions.

---

### **3. Flow Control**

#### ❖ Problem:

* A fast sender can overwhelm a slow receiver, causing buffer overflows and data loss.

#### ❖ Solutions:

* **Stop-and-Wait Protocol**:

  * Sender transmits one frame and waits for acknowledgment.
* **Sliding Window Protocol**:

  * Allows multiple frames in transit before acknowledgment.
  * Increases efficiency in high-latency links.

---

### **4. Error Detection vs Error Correction**

| Task             | Purpose                  | Methods               |
| ---------------- | ------------------------ | --------------------- |
| Error Detection  | Detect errors in frames  | CRC, Checksum, Parity |
| Error Correction | Fix errors automatically | Hamming Code, FEC     |

---

### **5. Acknowledgment and Retransmission**

#### ❖ Purpose:

* Ensures that frames are received correctly.

#### ❖ Types:

* **ACK**: Positive acknowledgment.
* **NACK**: Negative acknowledgment.
* **Timeouts**: Retransmit if no ACK is received in time.

---

### **6. Medium Access Control**

#### ❖ Problem:

* When multiple devices share a common medium, how to avoid collisions?

#### ❖ Techniques:

* **CSMA/CD** (Carrier Sense Multiple Access with Collision Detection): Ethernet.
* **CSMA/CA** (Carrier Sense Multiple Access with Collision Avoidance): Wi-Fi.
* **Token Passing**: Token-ring networks.
* **Polling**: Central controller grants permission.

---

### **7. Addressing**

#### ❖ Requirement:

* Identify the source and destination within a local network.

#### ❖ Solution:

* Use **MAC (Media Access Control) addresses** which are unique 48-bit identifiers assigned to each NIC.

---

### **8. Frame Sequencing and Numbering**

#### ❖ Problem:

* Frames may arrive **out of order** or be duplicated.

#### ❖ Solution:

* Use **sequence numbers** to identify frames.
* Helps detect lost or duplicate frames.

---

### **9. Frame Synchronization**

#### ❖ Problem:

* The receiver must know **where each frame begins and ends**.

#### ❖ Solution:

* Use **special bit patterns** or **synchronization characters** to mark frame boundaries.

---

### **10. Duplex Communication**

#### ❖ Modes:

* **Simplex**: One-way only.
* **Half-Duplex**: Two-way but one at a time.
* **Full-Duplex**: Two-way simultaneously.

#### ❖ Impact:

* Determines how acknowledgment and frame control must be managed.

---

### **Summary Table**

| Design Issue          | Description                               | Solution Examples                          |
| --------------------- | ----------------------------------------- | ------------------------------------------ |
| Framing               | Recognizing frame boundaries              | Bit stuffing, byte stuffing, special flags |
| Error Control         | Detecting/correcting transmission errors  | CRC, Hamming code, ARQ                     |
| Flow Control          | Matching sender/receiver speeds           | Stop-and-wait, sliding window              |
| Medium Access         | Preventing collisions in shared media     | CSMA/CD, token passing                     |
| Addressing            | Identifying sender and receiver           | MAC address                                |
| Frame Synchronization | Aligning start/end of frames              | Flag patterns, coding violations           |
| Acknowledgments       | Ensuring delivery of frames               | ACK, NACK, timeout                         |
| Sequencing            | Handling out-of-order or duplicate frames | Sequence numbers                           |

---

### **Error Detection in the Data Link Layer**

---

#### **1. Definition**

* **Error detection** is the process of identifying whether errors have occurred during the transmission of data across a communication channel.
* It ensures the **integrity** of data by checking if the received data matches the original.

---

### **2. Causes of Errors**

* **Thermal noise**
* **Signal attenuation**
* **Electromagnetic interference**
* **Crosstalk**
* **Hardware failures**

---

### **3. Types of Errors**

| Error Type           | Description                                  |
| -------------------- | -------------------------------------------- |
| **Single-bit Error** | Only one bit is altered during transmission. |
| **Burst Error**      | Two or more consecutive bits are altered.    |

---

### **4. Requirements for Error Detection**

* Sender computes a **redundant code** (error detection code) and appends it to the data.
* Receiver recalculates the code and **compares** it with the received code.
* If mismatch occurs → error detected.

---

### **5. Common Error Detection Techniques**

---

### **A. Parity Bit**

#### ❖ Method:

* Adds a **single bit** to the data to make the number of 1’s **even or odd**.

#### ❖ Types:

* **Even parity**: Ensures even number of 1s.
* **Odd parity**: Ensures odd number of 1s.

#### ❖ Example:

* Data: `1001101` (4 ones)

  * Even parity → Parity bit = 0 → `10011010`
  * Odd parity → Parity bit = 1 → `10011011`

#### ❖ Limitations:

* Can only detect **single-bit errors**, not burst errors.

---

### **B. Checksum**

#### ❖ Method:

* Data is divided into equal segments (e.g., 16 bits).
* All segments are **added** using binary addition.
* The **1’s complement** of the result is sent as the checksum.

#### ❖ At Receiver:

* Adds received segments including checksum.
* Takes 1’s complement of the sum.
* If result is **all 0s**, no error is detected.

#### ❖ Limitations:

* Weaker than CRC, may fail to detect some errors.

---

### **C. Cyclic Redundancy Check (CRC)**

#### ❖ Most powerful and widely used error detection method.

#### ❖ Method:

1. **Sender**:

   * Treats data as a binary polynomial `M(x)`.
   * Divides it by a predefined **generator polynomial** `G(x)`.
   * Appends **remainder** (CRC bits) to the data.
2. **Receiver**:

   * Divides the received data (data + CRC).
   * If **remainder = 0**, data is accepted.
   * Else, error is detected.

#### ❖ Example:

* Generator polynomial: `x³ + x + 1 → 1011`
* Data: `110100`
* Perform binary division (modulo-2), append remainder.

#### ❖ Advantages:

* Detects:

  * All single-bit errors.
  * All double-bit errors.
  * All odd number of bit errors.
  * Burst errors (length < generator length).

---

### **D. Longitudinal Redundancy Check (LRC)**

#### ❖ Method:

* Data is organized in a block of rows.
* Computes **parity for each column** and appends them as a final row.
* Used for **block error detection**.

#### ❖ Limitations:

* Can detect but not correct errors.

---

### **6. Comparison Table of Error Detection Methods**

| Method     | Extra Bits | Detects           | Strength    | Correction Ability |
| ---------- | ---------- | ----------------- | ----------- | ------------------ |
| Parity Bit | 1          | Single-bit errors | Weak        | No                 |
| Checksum   | 8/16 bits  | Many errors       | Medium      | No                 |
| CRC        | 8–32 bits  | Burst, multi-bit  | Very Strong | No                 |
| LRC        | Row bits   | Burst errors      | Strong      | No                 |

---

### **7. Error Detection vs. Error Correction**

| Feature    | Error Detection            | Error Correction           |
| ---------- | -------------------------- | -------------------------- |
| Purpose    | Identify presence of error | Detect and correct errors  |
| Complexity | Lower                      | Higher                     |
| Examples   | Parity, CRC, Checksum      | Hamming Code, Reed-Solomon |

---

### **8. Summary Table**

| Technique  | Bits Added | Error Type Detected    | Complexity | Efficiency |
| ---------- | ---------- | ---------------------- | ---------- | ---------- |
| Parity Bit | 1          | Single-bit             | Very Low   | Low        |
| Checksum   | Variable   | Many types             | Low        | Medium     |
| CRC        | Variable   | Burst and multi-bit    | Medium     | High       |
| LRC        | Variable   | Block and burst errors | Medium     | Medium     |

---

### **Error Correction in the Data Link Layer**

---

#### **1. Definition**

* **Error correction** is the process of identifying and **correcting errors** in transmitted data **without requiring retransmission**.
* Unlike error detection (which only identifies errors), error correction also **restores the original data**.

---

### **2. Purpose**

* Ensures **data integrity** in unreliable or noisy communication channels.
* Particularly useful in **wireless, satellite, or long-distance transmissions**, where retransmission is costly or impossible.

---

### **3. Methods of Error Correction**

---

### **A. Forward Error Correction (FEC)**

#### ❖ Principle:

* The sender **encodes** data with redundant bits before transmission.
* The receiver uses the redundancy to **detect and correct** errors.

#### ❖ Features:

* No retransmission required.
* Suitable for **real-time applications** (e.g., audio/video streaming, deep-space communication).

---

### **B. Automatic Repeat Request (ARQ)**

#### ❖ Principle:

* Combines error detection with **feedback-based retransmission**.
* If an error is detected, the receiver requests **retransmission**.

#### ❖ Variants:

1. **Stop-and-Wait ARQ**:

   * Sender sends one frame at a time and waits for ACK.
   * Retransmits if no ACK is received.

2. **Go-Back-N ARQ**:

   * Sender sends multiple frames (windowed), but must **retransmit from the errored frame** if one fails.

3. **Selective Repeat ARQ**:

   * Only **retransmits the specific errored frame**, not the entire window.

---

### **4. Error-Correcting Codes (ECC)**

---

### **A. Hamming Code**

#### ❖ Purpose:

* Detects and **corrects single-bit errors**.
* Can also **detect two-bit errors**.

#### ❖ Principle:

* Adds **parity bits at positions that are powers of 2**.
* Each parity bit covers a subset of data bits.
* The **syndrome** (binary index) tells the **position of the error**.

#### ❖ Example (7,4 Hamming Code):

* 4 data bits, 3 parity bits → total 7-bit code word.
* Positions: 1 (P1), 2 (P2), 3 (D1), 4 (P4), 5 (D2), 6 (D3), 7 (D4)

| Bit Pos | 1  | 2  | 3  | 4  | 5  | 6  | 7  |
| ------- | -- | -- | -- | -- | -- | -- | -- |
| Type    | P1 | P2 | D1 | P4 | D2 | D3 | D4 |

---

### **B. Reed–Solomon Code**

#### ❖ Features:

* Used in **block-based digital systems** like DVDs, QR codes, satellite links.
* Can **correct multiple burst errors** within a block.

#### ❖ Characteristics:

* Operates over **symbols** (not individual bits).
* Suitable for **high error environments**.

---

### **C. Convolutional Codes**

#### ❖ Used in:

* Real-time systems, wireless communication.
* Combines current and previous input bits to generate output.

#### ❖ Decoding:

* Uses **Viterbi Algorithm** for optimal decoding.

---

### **5. Comparison: Error Detection vs Correction**

| Feature         | Error Detection               | Error Correction                     |
| --------------- | ----------------------------- | ------------------------------------ |
| Action          | Identifies presence of errors | Identifies and fixes errors          |
| Techniques      | CRC, Parity, Checksum         | Hamming, Reed–Solomon, ARQ           |
| Feedback Needed | Yes (in ARQ)                  | No (in FEC)                          |
| Resource Use    | Lower                         | Higher (computationally expensive)   |
| Application     | LANs, Ethernet                | Wireless, satellite, media streaming |

---

### **6. Summary Table**

| Technique              | Correction Type | Suitable For                     | Correction Capability          |
| ---------------------- | --------------- | -------------------------------- | ------------------------------ |
| Hamming Code           | FEC             | RAM, digital communication       | 1-bit error correction         |
| Reed–Solomon Code      | FEC             | DVDs, QR codes, digital TV       | Multiple symbol errors         |
| Convolutional Code     | FEC             | Wireless, real-time transmission | Continuous data correction     |
| ARQ (Stop-and-Wait)    | Retransmission  | Simple data links                | Any error (via retransmission) |
| ARQ (Go-Back-N)        | Retransmission  | LAN/WAN protocols                | Any error (retransmits window) |
| ARQ (Selective Repeat) | Retransmission  | High-speed, reliable links       | Efficient retransmission       |

---

### **7. Conclusion**

* **Error correction** ensures that communication remains accurate and reliable.
* **FEC** is preferred in **high-latency/no-feedback systems**.
* **ARQ** is common in **computer networks**, especially TCP/IP-based systems.
* The choice of technique depends on **error rate**, **latency**, **bandwidth**, and **application requirements**.

---

### **Error Detection and Correction in the Data Link Layer**

---

### **1. Introduction**

* In data communication, **errors** can occur due to noise, interference, and signal attenuation.
* The **data link layer** ensures **reliable transmission** by implementing both **error detection** (identify if an error occurred) and **error correction** (fix the error, if possible).
* These are essential for maintaining **data integrity**.

---

### **2. Types of Errors**

| Error Type           | Description                                  |
| -------------------- | -------------------------------------------- |
| **Single-bit Error** | Only one bit is altered during transmission. |
| **Burst Error**      | Two or more consecutive bits are altered.    |

---

### **3. Techniques for Error Detection**

#### **A. Parity Bit**

* Adds 1 bit to make the total number of 1s **even (even parity)** or **odd (odd parity)**.
* **Detects single-bit errors** only.

#### **B. Checksum**

* Divides data into fixed-size blocks (e.g., 16 bits), adds them, and sends the **1's complement** of the sum as checksum.
* Receiver adds blocks + checksum; if result is all 1s → no error.

#### **C. Cyclic Redundancy Check (CRC)**

* Treats data as a binary polynomial and divides it by a **generator polynomial**.
* Appends **remainder** (CRC bits) to the frame.
* Receiver divides received bits by same polynomial: **if remainder = 0**, data is correct.

#### **D. Longitudinal Redundancy Check (LRC)**

* Organizes data into rows, computes **column-wise parity**, and appends them as a new row.

---

### **4. Techniques for Error Correction**

#### **A. Forward Error Correction (FEC)**

* Sender adds redundant bits to enable receiver to **detect and correct** errors.
* No need for retransmission.

##### i. **Hamming Code**

* Adds multiple parity bits to detect and correct **single-bit errors**.
* Example: 7-bit code for 4 data bits and 3 parity bits.

##### ii. **Reed–Solomon Code**

* Works on **symbols**, corrects **burst errors**.
* Used in DVDs, QR codes, satellite links.

##### iii. **Convolutional Codes**

* Generates output based on current and previous bits.
* Decoded using **Viterbi algorithm**.

#### **B. Automatic Repeat Request (ARQ)**

* Combines error detection with **retransmission**.

##### i. **Stop-and-Wait ARQ**

* Sends one frame and waits for ACK before sending next.
* Retransmits on timeout.

##### ii. **Go-Back-N ARQ**

* Sends multiple frames using a **window**.
* If one frame is lost, all subsequent frames are retransmitted.

##### iii. **Selective Repeat ARQ**

* Only **retransmits errored frames**, not the whole window.

---

### **5. Comparison Table**

| Feature    | Error Detection             | Error Correction                      |
| ---------- | --------------------------- | ------------------------------------- |
| Purpose    | Detect if an error occurred | Detect and correct errors             |
| Response   | Request retransmission      | Correct errors without retransmission |
| Examples   | CRC, Parity, Checksum       | Hamming Code, Reed–Solomon, ARQ       |
| Complexity | Lower                       | Higher                                |
| Use Case   | Reliable channels, LANs     | Noisy channels, satellite, streaming  |

---

### **6. Error Control Strategies in Data Link Layer**

| Strategy                 | Description                                       |
| ------------------------ | ------------------------------------------------- |
| **Error Detection**      | Detect corrupted frames using CRC, checksum, etc. |
| **Acknowledgment (ACK)** | Confirms successful receipt.                      |
| **Negative ACK (NACK)**  | Indicates error, requests retransmission.         |
| **Timeout**              | Retransmits if no ACK is received in time.        |
| **Sequence Numbers**     | Helps detect lost/duplicate frames.               |

---

### **7. Summary Table of Techniques**

| Technique    | Type       | Detects         | Corrects         | Best For                       |
| ------------ | ---------- | --------------- | ---------------- | ------------------------------ |
| Parity Bit   | Detection  | Single-bit      | No               | Simple, low-error environments |
| Checksum     | Detection  | Most errors     | No               | IP, TCP, UDP                   |
| CRC          | Detection  | Burst errors    | No               | Ethernet, Wi-Fi, USB           |
| Hamming Code | Correction | Single-bit      | Yes              | RAM, simple hardware systems   |
| Reed–Solomon | Correction | Burst/multi-bit | Yes              | DVDs, satellite, barcodes      |
| ARQ          | Correction | All errors      | Yes (via resend) | Computer networks (TCP/IP)     |

---

### **Elementary Data Link Protocols**

---

#### **1. Definition**

* **Elementary data link protocols** are the **basic set of rules and mechanisms** for the transmission of frames between two directly connected nodes over a communication link.
* These protocols provide **error detection, flow control**, and **acknowledgment handling** in simple, foundational scenarios (no complex networks).

---

### **2. Assumptions in Elementary Protocols**

* Communication is between **only two nodes** (point-to-point).
* **No channel access control** is needed (no shared medium).
* Each frame is transmitted **in order**.
* **Reliable** or **unreliable** channels may be considered depending on the protocol.

---

### **3. Categories of Elementary Protocols**

---

#### **A. Unrestricted Simplex Protocol**

##### ❖ Features:

* Data flows **in one direction only** (simplex).
* No flow or error control.
* Assumes **error-free** and **reliable** channel.

##### ❖ Operation:

* Sender sends frames continuously without waiting for any acknowledgment.
* Receiver only receives and delivers data to the network layer.

##### ❖ Limitation:

* Can lead to **buffer overflow** at the receiver.

---

#### **B. Simplex Stop-and-Wait Protocol**

##### ❖ Features:

* **Flow control** is added.
* Still one-directional.
* Sender waits for acknowledgment before sending the next frame.
* Assumes **error-free channel**.

##### ❖ Operation:

1. Sender sends one frame.
2. Waits for an **ACK** (acknowledgment).
3. Sends next frame after ACK is received.

##### ❖ Limitation:

* **Inefficient** use of bandwidth (idle wait time).

---

#### **C. Simplex Protocol with Error Detection (Stop-and-Wait ARQ)**

##### ❖ Features:

* Adds **error detection** using CRC or checksums.
* Includes **acknowledgment (ACK)** and **negative acknowledgment (NAK)**.
* Handles **lost or damaged frames**.
* Stop-and-wait approach is used.

##### ❖ Operation:

1. Sender transmits a frame and waits for ACK.
2. If frame is received correctly:

   * Receiver sends **ACK**.
3. If frame is corrupted or not received:

   * Receiver sends **NAK**, or sender times out and retransmits.

##### ❖ Problem Handled:

* Frame loss or corruption.

---

#### **D. Protocol with Flow and Error Control (Stop-and-Wait with Sequence Numbers)**

##### ❖ Features:

* Adds **sequence numbers** (usually 0 and 1 alternately) to detect **duplicate frames** due to retransmission.
* Handles both **flow control** and **error control**.

##### ❖ Operation:

1. Sender sends frame with sequence number `0`.
2. Receiver checks it and sends ACK `0`.
3. Sender then sends frame `1`, and so on.
4. If ACK is lost, sender **resends frame**.
5. Receiver checks sequence number to detect **duplicate** and discards it.

---

### **4. Summary Table of Elementary Protocols**

| Protocol                            | Direction | Flow Control | Error Control | Sequence Numbers | Use Case                      |
| ----------------------------------- | --------- | ------------ | ------------- | ---------------- | ----------------------------- |
| Unrestricted Simplex                | Simplex   | No           | No            | No               | Ideal, error-free link        |
| Simplex Stop-and-Wait               | Simplex   | Yes          | No            | No               | Prevent buffer overflows      |
| Simplex with Error Detection (ARQ)  | Simplex   | Yes          | Yes           | No               | Handles lost/corrupt frames   |
| Stop-and-Wait with Sequence Numbers | Simplex   | Yes          | Yes           | Yes              | Handles all elementary errors |

---

### **5. General Structure of a Frame in These Protocols**

| Field   | Purpose                                       |
| ------- | --------------------------------------------- |
| Header  | Contains control info (e.g., sequence number) |
| Payload | Actual data                                   |
| Trailer | Error detection bits (CRC/checksum)           |

---

### **6. Advantages of Elementary Protocols**

* Easy to understand and implement.
* Provide the foundation for more advanced data link protocols.
* Efficient in low-speed or low-error environments.

---

### **7. Limitations**

* Not suitable for high-speed or long-distance communication.
* Low utilization of bandwidth (especially in Stop-and-Wait).
* Inefficient in noisy environments or for large volumes of data.

---

### **8. Importance**

* Elementary protocols are used to **introduce fundamental concepts** like:

  * Framing
  * Acknowledgment
  * Timeout
  * Sequence numbers
  * Flow and error control
* These are the **building blocks** for complex protocols like **Sliding Window, HDLC, PPP**, etc.

---

### **Sliding Window Protocols**

---

#### **1. Definition**

* **Sliding Window Protocols** are a class of **flow and error control protocols** used in the data link layer and transport layer.
* They allow the sender to **transmit multiple frames before needing an acknowledgment**, improving **efficiency** and **throughput** over high-latency links.

---

### **2. Purpose**

* To **increase transmission efficiency** by allowing multiple outstanding (unacknowledged) frames.
* To handle **lost, delayed, duplicated, or out-of-order frames** using sequence numbers and acknowledgments.

---

### **3. Working Principle**

* Both sender and receiver **maintain a window**:

  * The **sender's window** contains frames it is allowed to send.
  * The **receiver's window** contains sequence numbers of frames it is willing to accept.

* As ACKs are received or frames are processed, the **window "slides"** forward, allowing transmission or acceptance of new frames.

---

### **4. Key Terminology**

| Term                | Description                                                             |
| ------------------- | ----------------------------------------------------------------------- |
| **Window Size**     | Number of frames that can be sent without waiting for ACK               |
| **Sequence Number** | Unique number attached to each frame to track order                     |
| **Acknowledgment**  | Signal from receiver confirming successful receipt of frame             |
| **Sliding**         | Movement of window to next set of sequence numbers as data is processed |

---

### **5. Types of Sliding Window Protocols**

---

#### **A. Go-Back-N ARQ**

##### ❖ Features:

* Sender can send **N frames** before waiting for an ACK.
* Receiver only accepts **in-order frames**.
* If a frame is lost or has an error, receiver **discards it and all subsequent frames**.
* Sender **goes back** and retransmits from the failed frame.

##### ❖ Sender Window:

* Size = N (N frames can be sent before acknowledgment is required).

##### ❖ Receiver Window:

* Size = 1 (accepts only the next expected frame).

##### ❖ Example:

1. Sender sends frames 0 to 4.
2. Frame 2 is lost.
3. Receiver discards frames 3, 4.
4. Sender retransmits 2, 3, 4 after timeout.

##### ❖ Pros:

* Simple to implement.

##### ❖ Cons:

* Wastes bandwidth on retransmission of correctly received frames.

---

#### **B. Selective Repeat ARQ**

##### ❖ Features:

* Sender can send **N frames** without waiting.
* Receiver **buffers out-of-order frames** and acknowledges each one individually.
* Only **incorrect or lost frames** are retransmitted.

##### ❖ Sender Window:

* Size = N

##### ❖ Receiver Window:

* Size = N (can accept out-of-order frames).

##### ❖ Example:

1. Sender sends frames 0 to 4.
2. Frame 2 is lost.
3. Receiver receives and buffers frames 3 and 4.
4. Only frame 2 is retransmitted.

##### ❖ Pros:

* Efficient use of bandwidth.

##### ❖ Cons:

* More complex due to buffering and tracking of individual frames.

---

### **6. Window Size and Sequence Numbers**

* If sequence number is `k` bits long:

  * Maximum sequence number range = `2^k`
* For Selective Repeat:

  * Maximum window size = `2^(k-1)`
* For Go-Back-N:

  * Window size can be up to `2^k – 1`

---

### **7. Diagrammatic Representation**

```
Sender Window (Go-Back-N, Window size = 4):

+----+----+----+----+----+----+----+
| 0  | 1  | 2  | 3  | 4  | 5  | 6  |
+----+----+----+----+----+----+----+
   ↑                            ↑
Send base                  Next frame to send
```

* When ACK is received for frame 0, window slides to start at 1.

---

### **8. Comparison: Go-Back-N vs Selective Repeat**

| Feature            | Go-Back-N ARQ                        | Selective Repeat ARQ                  |
| ------------------ | ------------------------------------ | ------------------------------------- |
| Retransmission     | Retransmits from the erroneous frame | Retransmits only the erroneous frame  |
| Receiver Buffering | Not required                         | Required (stores out-of-order frames) |
| Efficiency         | Lower                                | Higher                                |
| Complexity         | Simple                               | Complex                               |
| Window Size Limit  | Up to 2^k – 1                        | Up to 2^(k–1)                         |

---

### **9. Advantages of Sliding Window Protocols**

1. **Increased Efficiency**: Better link utilization over long delays.
2. **Pipelining**: Multiple frames in transit at once.
3. **Flow Control**: Prevents overflow at the receiver.
4. **Error Control**: Ensures accurate delivery of data.

---

### **10. Summary Table**

| Component          | Go-Back-N       | Selective Repeat      |
| ------------------ | --------------- | --------------------- |
| Sender Window      | N frames        | N frames              |
| Receiver Window    | 1 frame         | N frames              |
| Out-of-Order Frame | Discarded       | Buffered              |
| Retransmission     | Multiple frames | Only erroneous frames |
| Complexity         | Simple          | Complex               |

---

### **Example Data Link Protocols**

---

### **1. HDLC (High-Level Data Link Control)**

#### ❖ Overview:

* **Bit-oriented** synchronous data link layer protocol.
* Developed by **ISO**.
* Standard for WAN communication (e.g., point-to-point and multipoint).

#### ❖ Frame Structure:

```
| Flag | Address | Control | Data | FCS | Flag |
```

* **Flag**: Marks beginning/end (`01111110`)
* **Address**: Identifies secondary station
* **Control**: Sequence numbers, ACK/NAK, frame type
* **FCS**: Frame Check Sequence (error detection via CRC)

#### ❖ Frame Types:

| Type         | Purpose                    |
| ------------ | -------------------------- |
| **I-frames** | Carry user data            |
| **S-frames** | Supervisory (ACK, NAK)     |
| **U-frames** | Unnumbered control (setup) |

#### ❖ Features:

* Error detection using CRC
* Flow control via acknowledgments
* Supports **full-duplex** communication
* Uses **bit stuffing** to handle flag collision

---

### **2. PPP (Point-to-Point Protocol)**

#### ❖ Overview:

* **Byte-oriented** protocol for direct links (e.g., dial-up, DSL).
* Used to establish direct connection between two nodes.

#### ❖ Frame Format:

```
| Flag | Address | Control | Protocol | Payload | FCS | Flag |
```

* **Flag**: Start/end delimiter (`01111110`)
* **Protocol**: Type of data (IP, etc.)
* **FCS**: CRC-16 or CRC-32

#### ❖ Features:

* Supports **multiple protocols** (e.g., IP, IPX)
* Error detection via CRC
* No flow or error correction (relies on higher layers)
* **Authentication support** (PAP, CHAP)

---

### **3. Ethernet (IEEE 802.3)**

#### ❖ Overview:

* Widely used LAN data link protocol.
* Uses **MAC addresses** for addressing.

#### ❖ Frame Format:

```
| Preamble | SFD | Destination MAC | Source MAC | Type | Data | FCS |
```

* **Preamble**: 7 bytes for synchronization
* **SFD**: Start Frame Delimiter (1 byte)
* **Type**: Protocol type (e.g., IPv4)
* **FCS**: CRC-32

#### ❖ Features:

* Uses **CSMA/CD** for medium access
* No acknowledgment (unreliable)
* **Full-duplex and half-duplex** supported
* Frame size: **64 to 1518 bytes** (standard)

---

### **4. Wi-Fi (IEEE 802.11 MAC Layer)**

#### ❖ Overview:

* Wireless LAN data link protocol.
* Uses **MAC addresses** and **CSMA/CA** (Collision Avoidance).

#### ❖ MAC Frame Format:

```
| Frame Control | Duration | Address1 | Address2 | Address3 | Seq | Data | FCS |
```

#### ❖ Features:

* **Acknowledgment** for reliable transmission
* Supports **encryption** (WEP, WPA)
* **Access Point (AP)** based communication
* Uses **RTS/CTS** for reducing collision

---

### **5. Bluetooth (IEEE 802.15.1 - L2CAP)**

#### ❖ Overview:

* Short-range wireless protocol
* Operates on the **data link layer** via **L2CAP (Logical Link Control and Adaptation Protocol)**

#### ❖ L2CAP Features:

* Supports **connection-oriented and connectionless** communication
* Multiplexing of multiple logical channels over a single physical link
* Error detection via CRC
* Fragmentation and reassembly of packets

---

### **6. Token Ring (IEEE 802.5)**

#### ❖ Overview:

* **Token-based** access protocol for LANs
* Devices pass a **token** in a ring topology
* Only the station with the token can transmit

#### ❖ Frame Format:

```
| Start Delimiter | Access Control | Frame Control | Destination | Source | Data | CRC | End Delimiter |
```

#### ❖ Features:

* Collision-free (uses token passing)
* Deterministic access method
* Replaced by Ethernet due to cost/complexity

---

### **7. LAPB (Link Access Procedure - Balanced)**

#### ❖ Overview:

* Used in **X.25** networks
* Derived from HDLC; balanced (both sides equal role)
* **Bit-oriented**, reliable data link protocol

#### ❖ Features:

* Error correction using ARQ
* Flow control with sliding window
* Point-to-point synchronous communication

---

### **8. Summary Table**

| Protocol   | Type          | Orientation   | Medium   | Error Detection | Flow Control | Usage                         |
| ---------- | ------------- | ------------- | -------- | --------------- | ------------ | ----------------------------- |
| HDLC       | Bit-oriented  | Synchronous   | WAN      | CRC             | Yes          | Leased lines, X.25            |
| PPP        | Byte-oriented | Synchronous   | Serial   | CRC             | No           | Dial-up, DSL                  |
| Ethernet   | Frame-based   | Byte-oriented | LAN      | CRC-32          | No           | Local networks                |
| Wi-Fi      | Frame-based   | Byte-oriented | Wireless | CRC             | Yes          | Wireless networks             |
| Bluetooth  | Packet-based  | Byte-oriented | Wireless | CRC             | Yes          | PANs, short-range devices     |
| Token Ring | Frame-based   | Token-based   | LAN      | CRC             | Yes          | Legacy LANs                   |
| LAPB       | Bit-oriented  | Synchronous   | WAN      | CRC             | Yes          | X.25 packet-switched networks |

---

### **HDLC (High-Level Data Link Control)**

---

### **1. Definition**

* **HDLC** is a **bit-oriented, synchronous data link layer protocol** developed by **ISO**.
* It provides both **error detection** and **flow control**.
* It is a **standard protocol** for **WAN communications**, particularly over point-to-point and multipoint links.

---

### **2. Key Features**

| Feature                  | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| **Bit-oriented**         | Uses bit sequences, not characters, for control information. |
| **Synchronous**          | Requires synchronization between sender and receiver.        |
| **Error detection**      | Uses CRC (Cyclic Redundancy Check) in the FCS field.         |
| **Flow control**         | Manages the rate of data transmission using acknowledgments. |
| **Frame types**          | Uses three types of frames: I, S, and U.                     |
| **Supports full-duplex** | Allows simultaneous bidirectional communication.             |

---

### **3. Frame Format**

```
| Flag | Address | Control | Information | FCS | Flag |
```

#### **Field Descriptions**:

* **Flag (1 byte)**:

  * Bit pattern: `01111110`
  * Indicates the **start and end** of the frame.
  * Uses **bit stuffing** to avoid confusion with data.

* **Address**:

  * Identifies the destination station.
  * Can be broadcast or individual address.

* **Control**:

  * Indicates frame type (I/S/U), sequence numbers, ACK, etc.
  * Differentiates between **data**, **acknowledgment**, and **control**.

* **Information**:

  * Contains **payload data** (present only in I-frames).

* **FCS (Frame Check Sequence)**:

  * Usually 16 or 32 bits CRC.
  * Used for **error detection**.

---

### **4. Types of HDLC Frames**

---

#### **A. Information Frames (I-frames)**

* Used to **carry user data** from the network layer.
* Also carry **sequence numbers** for flow and error control.

| Field   | Purpose                      |
| ------- | ---------------------------- |
| N(S)    | Send sequence number         |
| N(R)    | Acknowledges received frames |
| P/F bit | Poll/Final control bit       |

---

#### **B. Supervisory Frames (S-frames)**

* Used for **flow and error control only**.
* Do **not contain user data**.

| Type | Purpose                                |
| ---- | -------------------------------------- |
| RR   | Receive Ready (ACK)                    |
| RNR  | Receive Not Ready (pause sending)      |
| REJ  | Reject (retransmit frame)              |
| SREJ | Selective Reject (retransmit specific) |

---

#### **C. Unnumbered Frames (U-frames)**

* Used for **control functions** like setup, disconnect, or status.
* Example: SABME (Set Asynchronous Balanced Mode Extended)

---

### **5. Operational Modes**

| Mode                                 | Description                                                                                |
| ------------------------------------ | ------------------------------------------------------------------------------------------ |
| **Normal Response Mode (NRM)**       | Primary controls link; secondaries respond only (used in unbalanced point-to-point links). |
| **Asynchronous Response Mode (ARM)** | Secondary stations can initiate communication (less used).                                 |
| **Asynchronous Balanced Mode (ABM)** | Both stations are equal and can initiate communication (common in full-duplex).            |

---

### **6. Bit Stuffing in HDLC**

* To prevent data from imitating the flag (`01111110`), HDLC uses **bit stuffing**:

  * After five consecutive 1s in data, a **0 is inserted**.
  * The receiver removes the 0 after five 1s.

---

### **7. Error Handling**

* **Detection** via CRC in FCS field.
* **Retransmission** handled using N(R) in I-frames or REJ in S-frames.
* **Acknowledgments**: Implicit in I-frames or explicit in RR.

---

### **8. Summary Table**

| Feature         | HDLC Specification                             |
| --------------- | ---------------------------------------------- |
| Orientation     | Bit-oriented                                   |
| Communication   | Point-to-point or multipoint                   |
| Flow Control    | Sliding Window, Supervisory Frames             |
| Error Detection | CRC (FCS field)                                |
| Frame Types     | I-frame, S-frame, U-frame                      |
| Bit Stuffing    | Yes (for flag delimitation)                    |
| Operation Modes | NRM, ARM, ABM                                  |
| Standard Use    | WAN protocols (e.g., leased lines, X.25, LAPB) |

---

### **The Data Link Layer in the Internet**

---

### **1. Overview**

* In the **Internet architecture**, the **data link layer** is responsible for the **reliable transfer of data frames** between two devices directly connected by a physical link.
* It provides **framing, addressing, error detection**, and **access control** over local or wide area links.
* The Internet protocols (like **IP, TCP, UDP**) are layered on top of the **data link protocols** such as **Ethernet, Wi-Fi, PPP, etc.**

---

### **2. Role in the TCP/IP Model**

| TCP/IP Layer       | Role of Data Link Layer Equivalent                   |
| ------------------ | ---------------------------------------------------- |
| **Network Access** | Combines OSI's Data Link and Physical layers         |
|                    | Responsible for link-level addressing, framing, etc. |

---

### **3. Responsibilities of Data Link Layer in the Internet**

| Function            | Description                                                                |
| ------------------- | -------------------------------------------------------------------------- |
| **Framing**         | Divides data into manageable units called **frames**                       |
| **Addressing**      | Uses **MAC addresses** to identify source and destination on the same link |
| **Error Detection** | Uses **CRC/FCS** to detect corrupted frames                                |
| **Flow Control**    | Prevents fast sender from overwhelming slow receiver (in some protocols)   |
| **Medium Access**   | Determines how devices access the link (e.g., CSMA/CD, CSMA/CA, token)     |

---

### **4. Common Data Link Protocols Used in the Internet**

---

#### **A. Ethernet (IEEE 802.3)**

* Most common LAN protocol.
* Uses **MAC addressing**, **CRC-32** for error detection.
* **No retransmission** or error correction.
* **Supports full- and half-duplex** modes.

#### Frame Format:

```
| Preamble | Dest MAC | Src MAC | Type | Payload | CRC |
```

---

#### **B. Wi-Fi (IEEE 802.11)**

* Wireless LAN protocol used in home and enterprise networks.
* Uses **CSMA/CA** to avoid collisions.
* Includes **acknowledgment (ACK)** for reliable delivery.
* Supports **encryption** and **authentication**.

---

#### **C. PPP (Point-to-Point Protocol)**

* Used for **direct connections** (e.g., DSL, modem).
* Provides **framing, authentication**, and **error detection**.
* Supports **multiple protocols** via the Protocol field.

---

#### **D. DSL, Cable, Fiber Links**

* Used in **last-mile Internet access**.
* Operate at data link level with protocols like:

  * **DOCSIS** for cable
  * **G-PON** for fiber
  * **ATM** (older DSL technologies)

---

### **5. MAC Addresses and ARP**

* Devices in a LAN use **MAC (Media Access Control) addresses** to identify one another.
* **IP addresses** must be **mapped to MAC addresses** using the **Address Resolution Protocol (ARP)**.

#### ARP Process:

1. Host sends **ARP request**: “Who has IP x.x.x.x?”
2. Device with that IP responds with its **MAC address**.
3. Host stores mapping in **ARP cache**.

---

### **6. Bridging and Switching**

* **Switches** operate at the data link layer.
* They use **MAC address tables** to forward frames to the correct port.
* **Bridges** divide LANs and reduce collision domains.

---

### **7. Error Handling**

| Component    | Method           |
| ------------ | ---------------- |
| **Ethernet** | CRC-32 in frame  |
| **Wi-Fi**    | CRC + ACK        |
| **PPP**      | CRC-16 or CRC-32 |

* **No retransmission** at data link level in Ethernet.
* **Wi-Fi** and **PPP** may request retransmission via acknowledgments.

---

### **8. Data Link Layer vs Network Layer**

| Feature    | Data Link Layer                         | Network Layer                |
| ---------- | --------------------------------------- | ---------------------------- |
| Addressing | MAC addresses                           | IP addresses                 |
| Scope      | Local link (directly connected devices) | End-to-end (across networks) |
| Units      | Frames                                  | Packets                      |
| Routing    | Not handled                             | Handled (via IP)             |

---

### **9. Summary Table**

| Feature             | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| Layer Role          | Local delivery over physical link                                |
| Addressing          | MAC addresses                                                    |
| Common Protocols    | Ethernet, Wi-Fi, PPP, DOCSIS, ATM                                |
| Error Detection     | CRC (Frame Check Sequence)                                       |
| Integration with IP | Uses ARP for MAC-to-IP mapping; transports IP packets in payload |
| Device Examples     | Switches, Network Interface Cards (NIC), Wireless Access Points  |

---

### **The Medium Access Sublayer (MAC Sublayer)**

---

### **1. Definition**

* The **Medium Access Control (MAC) Sublayer** is the **lower part of the Data Link Layer** in the OSI model.
* Its primary responsibility is to **control how devices access and share the physical transmission medium**.
* It manages **when and how** each device can **transmit data** over a shared communication channel.

---

### **2. Functions of the MAC Sublayer**

| Function                  | Description                                                         |
| ------------------------- | ------------------------------------------------------------------- |
| **Channel Allocation**    | Determines how the shared medium is divided among users.            |
| **Medium Access Control** | Decides which device can access the medium at a given time.         |
| **Addressing**            | Adds and processes **MAC addresses** (unique hardware identifiers). |
| **Frame Delimiting**      | Marks the start and end of each frame.                              |
| **Error Detection**       | Adds Frame Check Sequence (FCS) for CRC-based error detection.      |
| **Collision Handling**    | Uses methods like **CSMA/CD**, **CSMA/CA**, or **token passing**.   |

---

### **3. MAC Sublayer in OSI and IEEE Models**

* **OSI Model**:

  * Data Link Layer is divided into:

    * **LLC (Logical Link Control)**: Error correction, flow control
    * **MAC (Medium Access Control)**: Physical access to the medium

* **IEEE 802 Model**:

  * Specifies MAC for each LAN/WLAN standard like:

    * **802.3 (Ethernet)**
    * **802.11 (Wi-Fi)**
    * **802.15 (Bluetooth)**
    * **802.16 (WiMAX)**

---

### **4. Channel Access Methods Used by MAC Sublayer**

---

#### **A. Contention-Based Methods**

* Devices **compete** for access to the medium.

##### i. **ALOHA (Pure & Slotted)**

* Earliest random access protocol.
* **Pure ALOHA**: Transmit at any time.
* **Slotted ALOHA**: Transmit only at time slots.

##### ii. **CSMA (Carrier Sense Multiple Access)**

* Devices **listen to the channel** before transmitting.
* Variants:

  * **1-Persistent**
  * **Non-persistent**
  * **P-persistent**

##### iii. **CSMA/CD (Collision Detection)** — *Used in Ethernet*

* If a collision is detected, transmission is stopped and **random backoff** is performed.
* Works only in **wired networks**.

##### iv. **CSMA/CA (Collision Avoidance)** — *Used in Wi-Fi*

* Devices avoid collisions by using **RTS/CTS** mechanism and backoff timers.
* Suitable for **wireless networks** where collisions can't be detected easily.

---

#### **B. Controlled Access Methods**

* Access to the medium is **regulated** to avoid collisions.

##### i. **Polling**

* A master device **invites slaves** to transmit.
* Used in **centralized systems**.

##### ii. **Token Passing** — *Used in Token Ring*

* A **token** (special frame) circulates; only the device holding the token can transmit.
* **Collision-free**, but adds overhead.

---

#### **C. Channelization Methods (Multiplexing)**

* Divide the channel so multiple users can access **simultaneously**.

| Method   | Description                        |
| -------- | ---------------------------------- |
| **FDMA** | Frequency Division Multiple Access |
| **TDMA** | Time Division Multiple Access      |
| **CDMA** | Code Division Multiple Access      |

---

### **5. MAC Addressing**

* Every NIC (Network Interface Card) has a **unique 48-bit MAC address**.

* Format: `MM:MM:MM:SS:SS:SS`

  * MM: Manufacturer ID
  * SS: Serial number

* MAC addresses are used for **local delivery** within the same broadcast domain.

---

### **6. MAC Frame Structure**

* The frame structure varies with the protocol (e.g., Ethernet, Wi-Fi).

#### **Ethernet MAC Frame Format**:

```
| Preamble | Dest MAC | Src MAC | Type | Payload | FCS |
```

#### **Wi-Fi MAC Frame Format**:

```
| Frame Control | Duration | Address1 | Address2 | Address3 | Seq | Payload | FCS |
```

---

### **7. MAC Sublayer in Various Technologies**

| Technology     | MAC Protocol     | Medium Access Method      |
| -------------- | ---------------- | ------------------------- |
| **Ethernet**   | IEEE 802.3 MAC   | CSMA/CD                   |
| **Wi-Fi**      | IEEE 802.11 MAC  | CSMA/CA                   |
| **Bluetooth**  | IEEE 802.15.1    | Polling / TDMA            |
| **WiMAX**      | IEEE 802.16      | Scheduling / TDMA         |
| **Token Ring** | IEEE 802.5       | Token passing             |
| **Cellular**   | LTE/5G MAC layer | Scheduling / CDMA / OFDMA |

---

### **8. Summary Table**

| Aspect                | MAC Sublayer Role                                          |
| --------------------- | ---------------------------------------------------------- |
| Main Function         | Controls access to shared medium                           |
| Addresses Used        | MAC (physical) addresses                                   |
| Framing               | Defines frame boundaries                                   |
| Error Detection       | CRC in Frame Check Sequence                                |
| Medium Access Control | CSMA/CD, CSMA/CA, Polling, Token Passing, FDMA, TDMA, CDMA |
| Device Involvement    | Switches, NICs, APs                                        |

---

### **Channel Allocation Problem**

---

### **1. Definition**

* The **channel allocation problem** refers to the challenge of **assigning the communication medium (channel)** efficiently among **multiple competing users or devices** in a network.
* It arises primarily in **shared communication environments**, such as LANs, wireless networks, and satellite channels.

---

### **2. Objective**

* To **maximize channel utilization** while minimizing **collisions, delays, and idle times**.
* To ensure **fairness**, **efficiency**, and **low overhead** in how users access the medium.

---

### **3. Causes of the Problem**

| Cause                       | Description                                                            |
| --------------------------- | ---------------------------------------------------------------------- |
| **Shared Medium**           | Many devices try to use the same communication channel simultaneously. |
| **Simultaneous Requests**   | Multiple users try to send data at the same time.                      |
| **Lack of Central Control** | In decentralized systems, managing access becomes harder.              |
| **Collisions**              | Two or more transmissions interfere with each other.                   |
| **Idle Time**               | Channel may remain unused due to poor scheduling.                      |

---

### **4. Channel Allocation Approaches**

---

#### **A. Static Channel Allocation**

##### ❖ Description:

* The total bandwidth is **divided into fixed channels** assigned to specific users or devices.

##### ❖ Methods:

* **FDMA (Frequency Division Multiple Access)**: Each user gets a unique frequency band.
* **TDMA (Time Division Multiple Access)**: Each user gets a time slot to transmit.
* **CDMA (Code Division Multiple Access)**: All users transmit simultaneously with different codes.

##### ❖ Pros:

* **Predictable performance**, **no collisions**.

##### ❖ Cons:

* **Wastes bandwidth** if users are idle.
* Not suitable for **bursty** or **dynamic** traffic.

---

#### **B. Dynamic Channel Allocation**

##### ❖ Description:

* Channels are **assigned dynamically** based on demand and availability.
* No fixed assignment to users.

##### ❖ Types:

1. **Centralized Allocation**:

   * A central controller decides which device can transmit.
   * Requires **coordination overhead**.

2. **Distributed Allocation**:

   * Devices coordinate among themselves using predefined rules.
   * Examples: **ALOHA, CSMA/CD, CSMA/CA**.

##### ❖ Pros:

* **Efficient bandwidth use**, adaptable to traffic load.

##### ❖ Cons:

* **Possibility of collisions**.
* More complex to implement.

---

### **5. Evaluation Criteria for Channel Allocation**

| Metric          | Description                                             |
| --------------- | ------------------------------------------------------- |
| **Efficiency**  | How well the available bandwidth is utilized.           |
| **Fairness**    | Whether all users get a fair chance to transmit.        |
| **Scalability** | Ability to support more users without performance drop. |
| **Delay**       | Time taken to access the channel.                       |
| **Overhead**    | Extra signaling or coordination information needed.     |

---

### **6. Real-World Examples**

| Scenario              | Allocation Problem                           | Solution                       |
| --------------------- | -------------------------------------------- | ------------------------------ |
| **Wi-Fi (802.11)**    | Many devices using the same wireless channel | CSMA/CA (Carrier Sense)        |
| **Cellular Networks** | Multiple users in the same frequency band    | FDMA, TDMA, CDMA, OFDMA        |
| **Satellite Links**   | Thousands of users accessing uplink/downlink | Time/Frequency slot scheduling |
| **Ethernet LANs**     | Devices contending for same wire             | CSMA/CD (collision detection)  |

---

### **7. Comparison Table**

| Method        | Static/Dynamic | Medium Type    | Suitable For          | Collision | Efficiency |
| ------------- | -------------- | -------------- | --------------------- | --------- | ---------- |
| FDMA          | Static         | Wired/Wireless | Constant traffic      | No        | Low        |
| TDMA          | Static         | Wired/Wireless | Predictable use       | No        | Moderate   |
| CDMA          | Static         | Wireless       | Large number of users | No        | High       |
| CSMA/CD       | Dynamic        | Wired          | LANs (Ethernet)       | Yes       | Moderate   |
| CSMA/CA       | Dynamic        | Wireless       | Wi-Fi                 | No        | Moderate   |
| Token Passing | Dynamic        | Wired          | Ring Topologies       | No        | High       |

---

### **8. Conclusion**

* **Channel allocation is critical** for efficient communication in shared networks.
* **Static methods** are simpler but inefficient in dynamic environments.
* **Dynamic methods** offer better utilization but introduce **complexity** and **collision risks**.
* Choice of allocation method depends on **network type, user load, and application needs**.

---

### **Multiple Access Protocols**

---

### **1. Definition**

* **Multiple Access Protocols** are rules that govern how multiple devices **share and access a common communication channel**.
* Used in **shared medium networks** like LANs, MANs, WLANs, and satellite systems.
* Their primary goal is to **maximize channel utilization**, **minimize collisions**, and ensure **fair access** to the medium.

---

### **2. Classification of Multiple Access Protocols**

| Category              | Description                                                 |
| --------------------- | ----------------------------------------------------------- |
| **Random Access**     | Devices transmit randomly; collisions may occur.            |
| **Controlled Access** | Access to the channel is scheduled or regulated.            |
| **Channelization**    | Channel is divided logically; users get dedicated portions. |

---

## **3. RANDOM ACCESS PROTOCOLS**

→ *Also called contention protocols*
→ All stations **contend** for the channel; used in **decentralized environments**.

---

### **3.1. ALOHA Protocols**

#### **A. Pure ALOHA**

* Developed for satellite communication.
* **Transmit whenever data is ready**.
* If a collision occurs, the sender **waits a random time** and retransmits.

##### **Efficiency**: \~18%

---

#### **B. Slotted ALOHA**

* Time is divided into **equal slots**.
* Transmissions can **only start at the beginning of a slot**.
* Reduces chances of collision.

##### **Efficiency**: \~37%

---

### **3.2. CSMA (Carrier Sense Multiple Access)**

* Devices **listen** to the channel before transmitting.

#### Variants:

| Type               | Behavior                                                           |
| ------------------ | ------------------------------------------------------------------ |
| **1-Persistent**   | If channel is idle, transmit immediately. If busy, wait and retry. |
| **Non-persistent** | Wait a random time if channel is busy. Reduces collisions.         |
| **P-persistent**   | Used in slotted channels; transmit with probability *p* if idle.   |

---

### **3.3. CSMA/CD (Collision Detection)**

→ Used in **wired Ethernet**

* Detects collisions during transmission.
* If collision is detected, transmission is **aborted**, and **jam signal** is sent.
* Uses **binary exponential backoff** to retry.

---

### **3.4. CSMA/CA (Collision Avoidance)**

→ Used in **Wi-Fi (802.11)**

* Avoids collisions by using:

  * **Interframe spaces**
  * **Random backoff timers**
  * **RTS/CTS (Request to Send / Clear to Send)** mechanism
* Cannot detect collisions (wireless limitation).

---

## **4. CONTROLLED ACCESS PROTOCOLS**

→ *Also called deterministic protocols*
→ Each device’s access is **regulated or scheduled**.

---

### **4.1. Polling**

* A **central controller** asks each device if it wants to transmit.
* Devices respond only when polled.
* Efficient for low-collision environments.

---

### **4.2. Token Passing**

* A **token** (small control frame) is circulated among devices.
* Only the device holding the token can transmit.
* Used in **Token Ring (IEEE 802.5)** and **FDDI**.

---

### **4.3. Reservation Protocols**

* Devices **reserve time slots or frequency bands** in advance.
* Reservation table maintained by a coordinator or distributed among nodes.

---

## **5. CHANNELIZATION PROTOCOLS**

→ *Divide the channel among users logically*
→ Each user transmits simultaneously without collision.

---

### **5.1. FDMA (Frequency Division Multiple Access)**

* Channel is divided into **multiple frequency bands**.
* Each user gets a unique frequency.

---

### **5.2. TDMA (Time Division Multiple Access)**

* Channel is divided into **time slots**.
* Each user transmits during their own time slot.

---

### **5.3. CDMA (Code Division Multiple Access)**

* All users transmit simultaneously over the entire frequency spectrum.
* **Unique code** is assigned to each user to separate their signal.

---

### **6. Comparison Table**

| Protocol Type | Example    | Collision | Coordination | Efficiency | Complexity | Used In          |
| ------------- | ---------- | --------- | ------------ | ---------- | ---------- | ---------------- |
| Pure ALOHA    | Satellite  | High      | No           | Low        | Low        | Satellite links  |
| CSMA/CD       | Ethernet   | Medium    | No           | Moderate   | Medium     | Wired LAN        |
| CSMA/CA       | Wi-Fi      | Low       | No           | Moderate   | Medium     | Wireless LAN     |
| Polling       | Mainframe  | No        | Centralized  | High       | High       | Centralized LAN  |
| Token Passing | Token Ring | No        | Distributed  | High       | High       | Ring networks    |
| FDMA          | Cellular   | No        | Pre-assigned | Moderate   | Low        | Mobile Networks  |
| TDMA          | GSM        | No        | Scheduled    | High       | Medium     | Mobile Networks  |
| CDMA          | 3G, 4G     | No        | Code-based   | Very High  | High       | Wireless Systems |

---

### **7. Conclusion**

* **Random access protocols** are simple but may suffer from collisions.
* **Controlled access protocols** are efficient but require coordination.
* **Channelization protocols** allow simultaneous transmissions using separation techniques.
* The **choice** depends on **network type**, **traffic load**, and **physical medium**.

---

### **Ethernet**

---

### **1. Definition**

* **Ethernet** is a **LAN (Local Area Network)** technology defined by the **IEEE 802.3** standard.
* It specifies the **physical** and **data link layer** protocols for **wired communication** in LANs.
* Uses **MAC addressing** for node identification.
* Originally used **coaxial cable** and **bus topology**, now uses **twisted pair** and **star topology** with switches.

---

### **2. Key Characteristics**

| Feature            | Description                                                              |
| ------------------ | ------------------------------------------------------------------------ |
| **Standard**       | IEEE 802.3                                                               |
| **Topology**       | Star (modern), Bus (legacy)                                              |
| **Medium**         | Twisted pair, coaxial cable, fiber optics                                |
| **Speed Variants** | 10 Mbps (Ethernet), 100 Mbps (Fast Ethernet), 1 Gbps (Gigabit), 10 Gbps+ |
| **Access Method**  | CSMA/CD (Carrier Sense Multiple Access with Collision Detection)         |
| **Frame Size**     | 64 to 1518 bytes (excluding preamble); Jumbo frames up to 9000 bytes     |
| **MAC Address**    | 48-bit unique hardware address                                           |

---

### **3. Ethernet Frame Format**

```
| Preamble | SFD | Dest MAC | Src MAC | Type/Length | Data | FCS |
```

| Field           | Size (bytes) | Description                                           |
| --------------- | ------------ | ----------------------------------------------------- |
| **Preamble**    | 7            | Synchronization pattern (`101010...`)                 |
| **SFD**         | 1            | Start Frame Delimiter (`10101011`)                    |
| **Dest MAC**    | 6            | Destination MAC address                               |
| **Src MAC**     | 6            | Source MAC address                                    |
| **Type/Length** | 2            | Protocol type (e.g., IPv4 = 0x0800) or length of data |
| **Data**        | 46–1500      | Payload from Network layer                            |
| **FCS**         | 4            | Frame Check Sequence (CRC-32) for error detection     |

---

### **4. Ethernet Standards and Speed Variants**

| IEEE Standard | Name                | Speed      | Medium               |
| ------------- | ------------------- | ---------- | -------------------- |
| 802.3         | Ethernet            | 10 Mbps    | Coaxial              |
| 802.3u        | Fast Ethernet       | 100 Mbps   | Twisted pair/fiber   |
| 802.3z        | Gigabit Ethernet    | 1 Gbps     | Fiber optics         |
| 802.3ab       | Gigabit Ethernet    | 1 Gbps     | Cat5e/Cat6 UTP cable |
| 802.3ae       | 10 Gigabit Ethernet | 10 Gbps    | Fiber optics         |
| 802.3an       | 10GBase-T           | 10 Gbps    | Twisted pair (Cat6+) |
| 802.3bz       | 2.5G/5G Ethernet    | 2.5–5 Gbps | Twisted pair         |

---

### **5. CSMA/CD (Collision Detection)**

* Used in **half-duplex Ethernet** to handle collisions on a shared medium.

#### **Steps**:

1. Listen to channel (carrier sense).
2. If idle, start transmission.
3. If collision detected:

   * Stop transmission.
   * Send **jam signal**.
   * Wait for **random backoff time**.
   * Retry transmission.

* **Modern Ethernet** is **full-duplex** (via switches), so **CSMA/CD is rarely used now**.

---

### **6. MAC Addressing**

* Each Ethernet device has a **unique 48-bit MAC address** burned into its network interface card (NIC).
* Example: `00:1A:2B:3C:4D:5E`
* MAC addresses are used for **local delivery** within the same network segment.

---

### **7. Ethernet Switching**

* **Switches** forward Ethernet frames based on the **destination MAC address**.
* Builds a **MAC address table** to map MAC addresses to ports.
* Reduces **collision domains** (each port is its own domain).
* Enables **full-duplex** communication.

---

### **8. Error Detection**

* Ethernet uses **CRC-32** in the **FCS (Frame Check Sequence)** field.
* Corrupted frames are **discarded**; no retransmission at data link layer.

---

### **9. Types of Ethernet**

| Type                          | Description                                  |
| ----------------------------- | -------------------------------------------- |
| **Standard Ethernet**         | Legacy; 10 Mbps, coaxial cable (obsolete)    |
| **Fast Ethernet**             | 100 Mbps; introduced star topology           |
| **Gigabit Ethernet**          | 1 Gbps; UTP/fiber, most common in LANs today |
| **10G/40G Ethernet**          | Used in data centers, high-speed networks    |
| **Power over Ethernet (PoE)** | Supplies power and data over a single cable  |

---

### **10. Summary Table**

| Feature           | Ethernet (IEEE 802.3)                       |
| ----------------- | ------------------------------------------- |
| Data Rate         | 10 Mbps to 100 Gbps                         |
| Addressing        | 48-bit MAC Address                          |
| Frame Size        | 64 to 1518 bytes (standard)                 |
| Access Method     | CSMA/CD (only in half-duplex modes)         |
| Transmission Mode | Full-duplex (modern) / Half-duplex (legacy) |
| Error Handling    | CRC-32 (detection only, no correction)      |
| Topology          | Star with Switches                          |
| Devices           | NICs, switches, routers                     |

---

### **Data Link Layer Switching**

---

### **1. Definition**

* **Data Link Layer Switching** refers to the process of **forwarding Ethernet frames** between devices **based on MAC addresses**.
* It operates at **Layer 2 (Data Link Layer)** of the **OSI model**.
* Performed by devices called **network switches** (or Layer 2 switches).

---

### **2. Purpose**

* To enable **efficient frame forwarding** within a **LAN**.
* To **segment collision domains**, increasing network performance.
* To use **MAC address tables** to determine the appropriate output port.

---

### **3. Working Principle**

| Step | Description                                                              |
| ---- | ------------------------------------------------------------------------ |
| 1    | **Switch receives a frame** on one of its ports.                         |
| 2    | Reads the **source MAC address** and stores it in the MAC address table. |
| 3    | Checks the **destination MAC address** in the table:                     |
|      | → If found: forwards frame to the corresponding port.                    |
|      | → If not found: **broadcasts** the frame to all ports except the source. |
| 4    | Updates the table dynamically as it learns more addresses.               |

---

### **4. MAC Address Table (Forwarding Table)**

| MAC Address      | Port   | Timestamp (optional) |
| ---------------- | ------ | -------------------- |
| `00:1A:2B:3C:4D` | Port 2 |                      |
| `00:5B:6C:7D:8E` | Port 4 |                      |

* Maps each MAC address to the switch port where it was last seen.
* Entries may **expire** after an inactivity timeout (aging).

---

### **5. Switching Techniques**

---

#### **5.1. Store-and-Forward Switching**

* Entire frame is received and **checked for errors** using FCS before forwarding.
* High reliability, **slightly more latency**.

---

#### **5.2. Cut-Through Switching**

* Switch begins forwarding as soon as the **destination MAC address** is read.
* Low latency, but **errors are not checked**.

---

#### **5.3. Fragment-Free Switching**

* Switch waits until **64 bytes** of the frame are received before forwarding.
* Reduces forwarding of **collisions** or **runt frames**.

---

### **6. Benefits of Layer 2 Switching**

| Advantage               | Explanation                                    |
| ----------------------- | ---------------------------------------------- |
| **Reduces collisions**  | Each port is a separate collision domain.      |
| **Increases bandwidth** | Full bandwidth per port; supports full-duplex. |
| **Low latency**         | Especially with cut-through switching.         |
| **Scalable**            | Easily expandable LAN segments.                |

---

### **7. VLAN Support (Optional Functionality)**

* Layer 2 switches can support **Virtual LANs (VLANs)**.
* Frames are tagged using **IEEE 802.1Q** standard.
* Allows network segmentation **logically**, not physically.

---

### **8. Switch vs Hub**

| Feature          | Switch (Layer 2)             | Hub (Layer 1)           |
| ---------------- | ---------------------------- | ----------------------- |
| Forwarding       | Based on MAC address         | Broadcasts to all ports |
| Collision Domain | Per-port (isolated)          | Shared (one domain)     |
| Performance      | High                         | Low                     |
| Intelligence     | Has MAC table, learns routes | No learning or memory   |
| Full-duplex      | Yes                          | No                      |

---

### **9. Limitation of Layer 2 Switching**

| Limitation             | Explanation                                                        |
| ---------------------- | ------------------------------------------------------------------ |
| **No routing**         | Cannot forward packets across different networks (IP subnets).     |
| **Broadcast storms**   | Flooding behavior can lead to congestion if loops exist.           |
| **No traffic control** | Cannot apply routing policies or QoS without higher-layer support. |

---

### **10. Summary Table**

| Feature                | Description                                              |
| ---------------------- | -------------------------------------------------------- |
| Operates at Layer      | Layer 2 (Data Link Layer)                                |
| Forwarding Based On    | Destination MAC Address                                  |
| Device Used            | Switch                                                   |
| Key Function           | Efficient forwarding, collision isolation                |
| MAC Table              | Maintains port-to-MAC mapping                            |
| Switching Types        | Store-and-Forward, Cut-Through, Fragment-Free            |
| Enhancements Supported | VLANs, full-duplex communication, Spanning Tree Protocol |
| Not Capable Of         | Inter-network routing, IP-based decisions                |

---

### **Wireless LAN (WLAN)**

---

### **1. Definition**

* **Wireless LAN (WLAN)** is a type of **Local Area Network** that uses **radio waves** instead of wires to connect devices.
* Defined by the **IEEE 802.11** standard.
* Allows laptops, phones, tablets, and other devices to connect wirelessly within a **limited area** (home, office, campus).

---

### **2. IEEE 802.11 Standard**

| Standard           | Speed          | Frequency Band  | Description                          |
| ------------------ | -------------- | --------------- | ------------------------------------ |
| 802.11b            | Up to 11 Mbps  | 2.4 GHz         | First popular WLAN standard          |
| 802.11g            | Up to 54 Mbps  | 2.4 GHz         | Faster, backward compatible with 11b |
| 802.11n            | Up to 600 Mbps | 2.4 / 5 GHz     | MIMO antennas introduced             |
| 802.11ac           | Up to 1.3 Gbps | 5 GHz           | High-speed with beamforming          |
| 802.11ax (Wi-Fi 6) | Up to 9.6 Gbps | 2.4 / 5 / 6 GHz | OFDMA, MU-MIMO, improved efficiency  |

---

### **3. Components of WLAN**

| Component               | Function                                                            |
| ----------------------- | ------------------------------------------------------------------- |
| **Access Point (AP)**   | Connects wireless devices to wired LAN and provides radio coverage. |
| **Station (STA)**       | Any device (laptop, phone) with wireless NIC.                       |
| **Wireless NIC**        | Interface card to transmit and receive WLAN signals.                |
| **Distribution System** | Connects APs to wired network (usually Ethernet).                   |

---

### **4. WLAN Topologies**

---

#### **A. Infrastructure Mode**

* Devices communicate via **Access Point (AP)**.
* Most common topology.

```
Client Device ←→ Access Point ←→ Router/Switch
```

---

#### **B. Ad-Hoc Mode**

* Devices communicate **peer-to-peer** without AP.
* Used for direct, short-range communication.

```
Device ←→ Device
```

---

### **5. MAC Sublayer in WLAN (802.11)**

| Feature                    | Description                                                             |
| -------------------------- | ----------------------------------------------------------------------- |
| **Access method**          | **CSMA/CA** (Collision Avoidance) instead of CSMA/CD (used in Ethernet) |
| **No collision detection** | Due to signal interference and half-duplex operation                    |
| **RTS/CTS**                | Optional handshake mechanism to avoid hidden terminal problem           |
| **ACKs**                   | Frames are acknowledged to confirm successful reception                 |
| **Inter-frame spaces**     | Time gaps used to prioritize traffic types                              |

---

### **6. Frame Structure**

| Field                | Description                                                |
| -------------------- | ---------------------------------------------------------- |
| **Frame Control**    | Type/subtype, control flags (ACK, RTS, etc.)               |
| **Duration**         | Time the medium is reserved                                |
| **Address Fields**   | Source, Destination, AP addresses (up to 4 addresses used) |
| **Sequence Control** | Frame sequencing                                           |
| **FCS**              | Frame Check Sequence (CRC)                                 |

---

### **7. Security Protocols**

| Protocol       | Description                                       |
| -------------- | ------------------------------------------------- |
| **WEP**        | Weak encryption; obsolete                         |
| **WPA**        | Temporary fix for WEP vulnerabilities             |
| **WPA2 (AES)** | Strong encryption; widely used                    |
| **WPA3**       | Latest security standard with enhanced protection |

---

### **8. Challenges in WLAN**

| Issue                 | Description                                                 |
| --------------------- | ----------------------------------------------------------- |
| **Interference**      | From other wireless devices or obstacles                    |
| **Hidden terminal**   | Two clients out of range of each other may collide at AP    |
| **Exposed terminal**  | A node wrongly defers transmission due to neighbor activity |
| **Security threats**  | Eavesdropping, spoofing, unauthorized access                |
| **Lower reliability** | Compared to wired LAN due to wireless medium limitations    |

---

### **9. Advantages of WLAN**

| Advantage         | Description                                  |
| ----------------- | -------------------------------------------- |
| **Mobility**      | Users can move within coverage area freely   |
| **Scalability**   | Easy to add or remove devices                |
| **No wiring**     | Cost-effective and flexible installation     |
| **Accessibility** | Enables network access in hard-to-wire areas |

---

### **10. Disadvantages of WLAN**

| Disadvantage          | Explanation                                   |
| --------------------- | --------------------------------------------- |
| **Interference**      | From microwaves, Bluetooth, other APs         |
| **Limited Range**     | Typically 30–100 meters indoors               |
| **Security Risks**    | Wireless medium is more vulnerable than wired |
| **Bandwidth Sharing** | All clients share access point’s bandwidth    |

---

### **11. Comparison: WLAN vs Wired LAN**

| Feature          | WLAN (Wireless)             | Wired LAN (Ethernet)   |
| ---------------- | --------------------------- | ---------------------- |
| **Medium**       | Radio Waves                 | Copper or Fiber Cables |
| **Installation** | Easy                        | More complex           |
| **Mobility**     | High                        | Low                    |
| **Speed**        | Moderate to High (1–9 Gbps) | Very High (1–100 Gbps) |
| **Security**     | Vulnerable unless encrypted | Physically secure      |
| **Latency**      | Higher due to overhead      | Lower                  |

---

### **12. Summary Table**

| Parameter          | Value                                      |
| ------------------ | ------------------------------------------ |
| IEEE Standard      | 802.11                                     |
| Topologies         | Infrastructure, Ad-hoc                     |
| Access Method      | CSMA/CA                                    |
| Frame Format       | 802.11 MAC frame (multiple address fields) |
| Speed              | 11 Mbps to 9.6 Gbps                        |
| Frequency Bands    | 2.4 GHz, 5 GHz, 6 GHz                      |
| Key Devices        | APs, Wireless NICs, Routers                |
| Security Protocols | WPA2, WPA3                                 |

---

### **Broadband Wireless**

---

### **1. Definition**

* **Broadband Wireless** refers to **high-speed wireless internet access** over a **wide area** using **radio-frequency (RF)** technologies.
* Provides broadband speeds (≥25 Mbps) without physical cables.
* Used in both **fixed** (e.g., home broadband) and **mobile** (e.g., 4G/5G) environments.

---

### **2. Types of Broadband Wireless**

| Type                  | Description                                                               |
| --------------------- | ------------------------------------------------------------------------- |
| **Fixed Wireless**    | Internet delivered to a fixed location (e.g., home) via wireless signals. |
| **Mobile Wireless**   | Internet access while moving using cellular networks (3G/4G/5G).          |
| **Portable Wireless** | Internet access from portable hotspots (e.g., 4G dongles, MiFi).          |

---

### **3. Characteristics**

| Feature                     | Description                                                      |
| --------------------------- | ---------------------------------------------------------------- |
| **Wireless Medium**         | Uses licensed or unlicensed radio frequencies.                   |
| **Broad Coverage**          | Covers areas ranging from meters (Wi-Fi) to kilometers (LTE/5G). |
| **High Data Rates**         | Supports multi-megabit to gigabit speeds.                        |
| **No Cabling Required**     | Ideal for remote or difficult-to-wire areas.                     |
| **Multiple Access Support** | Uses multiple access methods (OFDMA, CDMA, TDMA).                |

---

### **4. Technologies Used in Broadband Wireless**

---

#### **4.1. WiMAX (IEEE 802.16)**

* **Worldwide Interoperability for Microwave Access**.
* Fixed/mobile broadband over long distances (up to 50 km).
* Supports up to 70 Mbps.
* Replaced largely by LTE and 5G.

---

#### **4.2. LTE (Long Term Evolution)**

* 4G technology standardized by 3GPP.
* Offers **100 Mbps+** for mobile users.
* Uses **OFDMA** for downlink and **SC-FDMA** for uplink.

---

#### **4.3. 5G (Fifth Generation)**

* Latest mobile broadband technology.
* Speeds up to **10 Gbps**, latency < 1 ms.
* Uses **millimeter-wave (mmWave)** spectrum and **massive MIMO**.

---

#### **4.4. Satellite Broadband**

* Broadband via **satellites** in geostationary (e.g., HughesNet) or LEO orbits (e.g., Starlink).
* Useful in remote and rural areas.
* Higher latency due to distance.

---

#### **4.5. Wi-Fi (IEEE 802.11)**

* Common indoor broadband wireless in homes/offices.
* Supports **802.11ac/ax** for multi-gigabit speeds.
* Limited range (\~100 meters indoor).

---

### **5. Frequency Bands Used**

| Technology | Frequency Bands             |
| ---------- | --------------------------- |
| Wi-Fi      | 2.4 GHz, 5 GHz, 6 GHz       |
| LTE        | 700 MHz – 2.6 GHz           |
| 5G         | <6 GHz, 24–100 GHz (mmWave) |
| WiMAX      | 2.3 GHz, 2.5 GHz, 3.5 GHz   |
| Satellite  | Ku-band, Ka-band, L-band    |

---

### **6. Medium Access Control in Broadband Wireless**

| Method      | Description                                                             |
| ----------- | ----------------------------------------------------------------------- |
| **TDMA**    | Users transmit in different time slots.                                 |
| **FDMA**    | Users use different frequency channels.                                 |
| **OFDMA**   | Subset of OFDM used in LTE/5G; allocates subcarriers dynamically.       |
| **CDMA**    | All users transmit simultaneously using unique codes (used in 3G).      |
| **CSMA/CA** | Used in Wi-Fi; devices sense and avoid collisions using backoff timers. |

---

### **7. Applications**

| Area                     | Examples                                            |
| ------------------------ | --------------------------------------------------- |
| **Residential Access**   | 4G/5G routers, WiMAX for homes                      |
| **Enterprise**           | Business backup links, wireless bridging            |
| **Public Hotspots**      | Wi-Fi in cafes, airports, hotels                    |
| **Rural Connectivity**   | Satellite and fixed wireless access in remote areas |
| **IoT and Smart Cities** | 5G for smart meters, sensors, autonomous vehicles   |

---

### **8. Advantages**

| Advantage           | Explanation                                        |
| ------------------- | -------------------------------------------------- |
| **Easy Deployment** | No need for physical cables.                       |
| **Wide Coverage**   | Especially with LTE, 5G, and satellite.            |
| **High Speed**      | Supports streaming, gaming, video conferencing.    |
| **Scalability**     | Easy to add users/devices.                         |
| **Mobility**        | Works for users in motion (e.g., in cars, trains). |

---

### **9. Disadvantages**

| Disadvantage           | Explanation                                                         |
| ---------------------- | ------------------------------------------------------------------- |
| **Interference**       | RF signals may be affected by other signals, weather, or obstacles. |
| **Security Risks**     | Wireless medium is vulnerable to eavesdropping and attacks.         |
| **Latency**            | Higher in satellite links or congested mobile networks.             |
| **Signal Attenuation** | Distance and physical obstructions reduce signal strength.          |

---

### **10. Summary Table**

| Feature        | Description                                   |
| -------------- | --------------------------------------------- |
| Definition     | High-speed wireless Internet over radio waves |
| Technologies   | WiMAX, LTE, 5G, Wi-Fi, Satellite              |
| Data Rates     | 10 Mbps to 10 Gbps                            |
| Coverage       | Local (Wi-Fi) to Global (Satellite, 5G)       |
| Access Methods | TDMA, FDMA, OFDMA, CDMA, CSMA/CA              |
| Use Cases      | Home, enterprise, mobile, rural, IoT          |
| Standards      | IEEE 802.16, 802.11, 3GPP (LTE/5G)            |

---

### **Bluetooth**

---

### **1. Definition**

* **Bluetooth** is a **short-range wireless communication technology** designed to connect devices over the **2.4 GHz ISM band**.
* It enables **device-to-device communication** without cables, primarily for **personal area networks (PANs)**.
* Standardized under **IEEE 802.15.1**, maintained by the **Bluetooth SIG (Special Interest Group)**.

---

### **2. Purpose**

* Designed for **low-power**, **low-cost**, and **short-range** wireless communication.
* Common uses include **wireless headsets**, **file transfers**, **IoT**, **smartphones**, **keyboards**, **speakers**, etc.

---

### **3. Bluetooth Architecture**

| Component      | Function                                                             |
| -------------- | -------------------------------------------------------------------- |
| **Master**     | Controls communication within a piconet (Bluetooth network).         |
| **Slave**      | Listens and responds to the master.                                  |
| **Piconet**    | A network formed by one master and up to 7 active slaves.            |
| **Scatternet** | A network of interconnected piconets (a device may act as a bridge). |

---

### **4. Bluetooth Versions and Speeds**

| Version             | Max Data Rate       | Range        | Key Features                             |
| ------------------- | ------------------- | ------------ | ---------------------------------------- |
| Bluetooth 1.2       | 1 Mbps              | \~10 meters  | Initial standard                         |
| Bluetooth 2.0 + EDR | 3 Mbps              | \~10 meters  | Enhanced Data Rate                       |
| Bluetooth 3.0 + HS  | 24 Mbps (via Wi-Fi) | \~10 meters  | High speed using Wi-Fi for bulk transfer |
| Bluetooth 4.0 (LE)  | 1 Mbps              | \~50–100 m   | Bluetooth Low Energy (BLE) introduced    |
| Bluetooth 5.0       | 2 Mbps (LE)         | \~240 meters | Higher speed, longer range, BLE improved |
| Bluetooth 5.2       | 2 Mbps (LE)         | \~240 meters | Isochronous channels, LE Audio           |

---

### **5. Bluetooth Protocol Stack**

#### **A. Core Layers**

| Layer                                                    | Description                                                      |
| -------------------------------------------------------- | ---------------------------------------------------------------- |
| **Radio**                                                | Physical layer; defines modulation (GFSK, etc.) and frequencies. |
| **Baseband**                                             | Handles connection setup, addressing, and low-level links.       |
| **L2CAP** (Logical Link Control and Adaptation Protocol) | Multiplexes protocols, handles segmentation.                     |
| **HCI** (Host Controller Interface)                      | Interface between hardware and software stacks.                  |

#### **B. Middleware and Application Layers**

| Layer                                | Function                                                        |
| ------------------------------------ | --------------------------------------------------------------- |
| **RFCOMM**                           | Serial port emulation                                           |
| **SDP** (Service Discovery Protocol) | Allows devices to discover services offered                     |
| **Profiles**                         | Define specific use cases (e.g., A2DP for audio, HID for input) |

---

### **6. Medium Access Control in Bluetooth**

* Uses **Frequency Hopping Spread Spectrum (FHSS)** over 79 channels (1 MHz each).
* Hops 1600 times per second to reduce interference and improve reliability.
* **TDMA-based access** with master controlling time slots.

---

### **7. Bluetooth Low Energy (BLE)**

| Feature              | Description                                     |
| -------------------- | ----------------------------------------------- |
| **Low Power**        | Optimized for devices with limited battery      |
| **Fast Connection**  | Instant connection and data transfer            |
| **Used In**          | Fitness trackers, smartwatches, medical devices |
| **Protocol Simpler** | Fewer overheads than classic Bluetooth          |

---

### **8. Bluetooth Profiles (Use Cases)**

| Profile  | Description                                          |
| -------- | ---------------------------------------------------- |
| **A2DP** | Advanced Audio Distribution Profile (wireless audio) |
| **HFP**  | Hands-Free Profile (phone headsets)                  |
| **HID**  | Human Interface Device (keyboards, mice)             |
| **OBEX** | File transfer between devices                        |
| **PAN**  | Internet sharing between devices                     |

---

### **9. Advantages**

| Advantage                 | Explanation                                   |
| ------------------------- | --------------------------------------------- |
| **No cables**             | Wireless short-range connectivity             |
| **Low power consumption** | Especially BLE for battery-powered devices    |
| **Global compatibility**  | Operates on the license-free 2.4 GHz ISM band |
| **Built-in security**     | Supports authentication and encryption        |

---

### **10. Limitations**

| Limitation            | Description                                         |
| --------------------- | --------------------------------------------------- |
| **Short range**       | Typically < 10 meters for classic Bluetooth         |
| **Interference**      | Shares 2.4 GHz with Wi-Fi, microwave ovens, etc.    |
| **Low data rates**    | Not suitable for high-definition video streaming    |
| **Connection limits** | Limited number of simultaneous devices in a piconet |

---

### **11. Comparison with Other Wireless Technologies**

| Feature         | Bluetooth                            | Wi-Fi           | Zigbee          |
| --------------- | ------------------------------------ | --------------- | --------------- |
| **Range**       | \~10–240 meters                      | \~50–150 meters | \~10–100 meters |
| **Speed**       | Up to 3 Mbps (Classic), 2 Mbps (BLE) | Up to 10 Gbps   | \~250 kbps      |
| **Power Usage** | Low                                  | High            | Very low        |
| **Use Case**    | PAN, peripherals                     | LAN, internet   | IoT, sensors    |

---

### **12. Summary Table**

| Parameter        | Value                                                        |
| ---------------- | ------------------------------------------------------------ |
| Standard         | IEEE 802.15.1                                                |
| Frequency        | 2.4 GHz ISM band                                             |
| Data Rate        | 1–3 Mbps (Classic), 2 Mbps (BLE), 24 Mbps (Bluetooth 3.0 HS) |
| Range            | 10–240 meters depending on version and power class           |
| Topology         | Piconet (1 master + 7 slaves), Scatternet                    |
| Access Method    | FHSS + TDMA                                                  |
| Key Applications | Audio, file transfer, IoT, peripherals, healthcare           |
| Security         | Authentication, encryption (E0, AES for BLE)                 |

---

