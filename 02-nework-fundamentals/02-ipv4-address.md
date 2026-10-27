# IPv4 Address — Part 1

> Notes from today's study session, based on the attached lesson **IPv4 Address ตอนที่ 1**.  

## Learning Objectives — จุดประสงค์การเรียนรู้

- Understand what an IPv4 address is and why devices need addresses to communicate.  
- Read IPv4 addresses in decimal and binary notation.  
- Recognize the IPv4 address classes (A–E) introduced in the lesson.  
  ทำความรู้จัก Class ของ IPv4 Address (A–E) ที่กล่าวถึงในบทเรียน
- Distinguish public and private IPv4 addresses.  
  แยกความแตกต่างระหว่าง Public IPv4 Address และ Private IPv4 Address ได้
- Identify source and destination IP addresses in a packet capture.  
  ระบุ Source IP Address และ Destination IP Address จากการจับ Packet ได้

## 1. What Is an IP Address? — IP Address คืออะไร?

An **IP address** is a *logical address* assigned to a device connected to a network.  
**IP Address** คือ *Logical Address* หรือที่อยู่เชิงตรรกะที่กำหนดให้กับอุปกรณ์ซึ่งเชื่อมต่ออยู่ในเครือข่าย

The lesson contrasts it with a **MAC address**, which it calls a *physical address*.  
บทเรียนเปรียบเทียบ IP Address กับ **MAC Address** ซึ่งเรียกว่า *Physical Address* หรือที่อยู่ทางกายภาพ

An IP address can be changed, and configuring IP addresses allows devices to communicate on a network.  
IP Address สามารถเปลี่ยนแปลงได้ และการกำหนด IP Address ช่วยให้อุปกรณ์ต่าง ๆ สามารถสื่อสารกันภายในเครือข่ายได้

เปรียบเทียบกับการส่งจดหมาย: ต้องมีที่อยู่ของผู้ส่งและผู้รับ เช่นเดียวกับการสื่อสารผ่าน Network ที่ระบุ IP Address ต้นทางและปลายทาง

- **IP address:** Logical address used for network communication.  
  **IP Address:** ที่อยู่เชิงตรรกะที่ใช้ในการสื่อสารผ่านเครือข่าย
- **MAC address:** Physical address, using the terminology in the lesson.  
  **MAC Address:** ที่อยู่ทางกายภาพตามคำศัพท์ที่ใช้ในบทเรียน

## 2. IPv4 Address Format 

An IPv4 address contains **32 bits**, divided into **four 8-bit groups**.  
IPv4 Address มีขนาด **32 บิต** แบ่งออกเป็น **4 กลุ่ม กลุ่มละ 8 บิต**

Each group is called an **octet**.  
แต่ละกลุ่มเรียกว่า **Octet**

The common human-readable format uses four decimal numbers separated by dots.  
รูปแบบที่มนุษย์อ่านได้ทั่วไปจะใช้เลขฐานสิบ 4 ชุด โดยคั่นแต่ละชุดด้วยจุด

Example — ตัวอย่าง:

```text
192.168.1.100
```

Each octet has a decimal value from **0 to 255**, corresponding to an 8-bit binary value from `00000000` to `11111111`.  
แต่ละ Octet มีค่าเลขฐานสิบตั้งแต่ **0 ถึง 255** ซึ่งตรงกับเลขฐานสองขนาด 8 บิต ตั้งแต่ `00000000` ถึง `11111111`

| Octet (กลุ่ม) | Decimal (ฐานสิบ) | Binary (ฐานสอง) |
|---|---:|---|
| 1 | 192 | `11000000` |
| 2 | 168 | `10101000` |
| 3 | 1 | `00000001` |
| 4 | 100 | `01100100` |

Therefore — ดังนั้น:

```text
192.168.1.100
= 11000000.10101000.00000001.01100100
```

### Decimal vs. Binary — เลขฐานสิบกับเลขฐานสอง

- **Decimal (base 10):** Uses digits `0–9`; convenient for people to read and remember IP addresses.  
  **เลขฐานสิบ (ฐาน 10):** ใช้ตัวเลข `0–9` ทำให้มนุษย์อ่านและจดจำ IP Address ได้สะดวก
- **Binary (base 2):** Uses digits `0` and `1`; computers and network devices process information in binary form.  
  **เลขฐานสอง (ฐาน 2):** ใช้ตัวเลข `0` และ `1` โดยคอมพิวเตอร์และอุปกรณ์เครือข่ายประมวลผลข้อมูลในรูปแบบเลขฐานสอง

When converting an IPv4 address, convert each octet separately and keep each binary octet at **8 bits**.  
เมื่อแปลง IPv4 Address ให้แปลงทีละ Octet และเขียนเลขฐานสองของแต่ละ Octet ให้ครบ **8 บิต**

For example, decimal `1` is written as `00000001` in an IPv4 octet.  
ตัวอย่างเช่น เลขฐานสิบ `1` จะเขียนเป็น `00000001` เมื่ออยู่ใน Octet ของ IPv4

## 3. IPv4 Address Classes — Class ของ IPv4 Address

The lesson introduces the historical class-based grouping of IPv4 addresses: **Class A, B, C, D, and E**.  
บทเรียนแนะนำการแบ่ง IPv4 Address ตามระบบ Class แบบดั้งเดิม ได้แก่ **Class A, B, C, D และ E**

| Class | Range shown or described in the lesson (ช่วง Address ในบทเรียน) | Notes from the lesson (หมายเหตุจากบทเรียน) |
|---|---|---|
| A | `0.0.0.0 – 127.0.0.0`; the lesson also gives first-octet values `1–126` as an easy rule of thumb | Addresses beginning with `127` are identified as loopback addresses. / Address ที่ขึ้นต้นด้วย `127` ถูกระบุว่าเป็น Loopback Address |
| B | `128.0.0.0 – 191.255.255.255` | Class B range / ช่วง Address ของ Class B |
| C | `192.0.0.0 – 223.255.255.255` | Class C range / ช่วง Address ของ Class C |
| D | `224.0.0.0 – 239.255.255.255` | Multicast addresses / Address สำหรับ Multicast |
| E | `240.0.0.0 – 255.255.255.255` | Reserved addresses in the lesson's diagram / Address ที่สงวนไว้ตามแผนภาพในบทเรียน |

### Loopback — ที่อยู่ Loopback

The lesson identifies addresses beginning with `127` as **loopback addresses**, reserved for testing on the local system.  
บทเรียนระบุว่า Address ที่ขึ้นต้นด้วย `127` เป็น **Loopback Address** ซึ่งสงวนไว้สำหรับทดสอบการทำงานภายในระบบของเครื่องตัวเอง

A commonly used example is `127.0.0.1`.  
ตัวอย่างที่ใช้กันทั่วไปคือ `127.0.0.1`

> **Additional context — beyond the lesson:** Class A/B/C is a historical classful model. Modern IPv4 network design generally uses CIDR prefixes and subnet masks instead of relying on address classes alone.  
> **ข้อมูลเพิ่มเติมนอกเหนือจากบทเรียน:** Class A/B/C เป็นรูปแบบการแบ่ง Address แบบดั้งเดิม ปัจจุบันการออกแบบเครือข่าย IPv4 มักใช้ CIDR Prefix และ Subnet Mask แทนการอาศัย Class เพียงอย่างเดียว

## 4. Public and Private IPv4 Addresses — Public และ Private IPv4 Address

The lesson further divides addresses into **public IPv4** and **private IPv4**.  
บทเรียนแบ่ง IPv4 Address ออกเป็น **Public IPv4** และ **Private IPv4** เพิ่มเติม

### Public IPv4 — IPv4 สาธารณะ

A **public IPv4 address** is an address used in the public Internet's routing space.  
**Public IPv4 Address** คือ Address ที่ใช้ในพื้นที่การกำหนดเส้นทาง (Routing) ของอินเทอร์เน็ตสาธารณะ

The lesson describes it as an address that is not duplicated and is routed on the Internet.  
บทเรียนอธิบายว่าเป็น Address ที่ไม่ซ้ำกันและสามารถถูก Route บนอินเทอร์เน็ตได้

Its example is a computer at home with a public IP and a shared file that could be accessed remotely over the Internet.  
ตัวอย่างในบทเรียนคือคอมพิวเตอร์ที่บ้านซึ่งมี Public IP และเปิดแชร์ไฟล์ไว้ ทำให้สามารถเข้าถึงไฟล์จากระยะไกลผ่านอินเทอร์เน็ตได้

In practice, successful access also depends on routing, firewall rules, and service configuration; a public IP alone does not guarantee that a service is reachable.  
ในทางปฏิบัติ การเข้าถึงได้จริงยังขึ้นอยู่กับ Routing, กฎ Firewall และการตั้งค่าบริการด้วย การมี Public IP เพียงอย่างเดียวไม่ได้รับประกันว่าบริการจะเข้าถึงได้

### Private IPv4 — IPv4 ส่วนตัว

A **private IPv4 address** is used inside a home network or organization.  
**Private IPv4 Address** คือ Address ที่ใช้ภายในเครือข่ายบ้านหรือองค์กร

The same private address can be reused in different private networks and is not routed directly over the public Internet.  
Private Address เดียวกันสามารถนำกลับมาใช้ซ้ำในเครือข่ายส่วนตัวคนละเครือข่ายได้ และจะไม่ถูก Route โดยตรงผ่านอินเทอร์เน็ตสาธารณะ

The lesson highlights two reasons for private addresses:  
บทเรียนยกเหตุผลสำคัญสองประการที่ต้องใช้ Private Address ได้แก่

- Help conserve the limited supply of public IPv4 addresses.  
  ช่วยประหยัดจำนวน Public IPv4 Address ที่มีอยู่อย่างจำกัด
- Allow devices to communicate within a home or organizational network.  
  ช่วยให้อุปกรณ์สามารถสื่อสารกันภายในเครือข่ายบ้านหรือองค์กรได้

The lesson diagram shows these private IPv4 ranges:  
แผนภาพในบทเรียนแสดงช่วง Private IPv4 ดังต่อไปนี้

| Private range (ช่วง Address ส่วนตัว) | CIDR notation (รูปแบบ CIDR) |
|---|---|
| `10.0.0.0 – 10.255.255.255` | `10.0.0.0/8` |
| `172.16.0.0 – 172.31.255.255` | `172.16.0.0/12` |
| `192.168.0.0 – 192.168.255.255` | `192.168.0.0/16` |

**Additional context:** Private networks commonly access the Internet through a router performing Network Address Translation (NAT).  
**ข้อมูลเพิ่มเติม:** โดยทั่วไปเครือข่ายส่วนตัวจะเชื่อมต่ออินเทอร์เน็ตผ่าน Router ที่ทำหน้าที่ Network Address Translation (NAT)

NAT is common in these setups, but it is not the definition of a private IP address.  
NAT เป็นวิธีที่พบได้บ่อยในรูปแบบเครือข่ายนี้ แต่ NAT ไม่ใช่คำจำกัดความของ Private IP Address

### Public vs. Private at a Glance — เปรียบเทียบ Public กับ Private แบบย่อ

| Property (คุณสมบัติ) | Public IPv4 | Private IPv4 |
|---|---|---|
| Typical use (การใช้งานทั่วไป) | Public Internet communication / การสื่อสารผ่านอินเทอร์เน็ตสาธารณะ | Internal LANs and private networks / LAN และเครือข่ายส่วนตัว |
| Reuse (การใช้ซ้ำ) | Must be unique within the relevant public routing context / ต้องไม่ซ้ำในบริบทของการ Route บนอินเทอร์เน็ตสาธารณะ | Can be reused in separate private networks / ใช้ซ้ำในเครือข่ายส่วนตัวที่แยกจากกันได้ |
| Directly routed on the public Internet (การ Route โดยตรงบนอินเทอร์เน็ตสาธารณะ) | Yes, when allocated and routed correctly / ได้ หากจัดสรรและกำหนด Routing อย่างถูกต้อง | No / ไม่ได้ |
| Example (ตัวอย่าง) | A globally routed address / Address ที่ Route บนอินเทอร์เน็ตสาธารณะ | `192.168.1.100` on a home LAN / `192.168.1.100` ภายใน LAN ที่บ้าน |

## 5. Source and Destination IP in Wireshark — Source และ Destination IP ใน Wireshark

The lesson shows a Wireshark capture while a computer accesses `www.cisco.com`.  
บทเรียนแสดงตัวอย่างการจับ Packet ด้วย Wireshark ขณะที่คอมพิวเตอร์เข้าใช้งาน `www.cisco.com`

In the packet's Internet Protocol (IP) header, two important fields are:  
ภายใน Header ของ Internet Protocol (IP) ใน Packet จะมีฟิลด์สำคัญสองรายการ ได้แก่

- **Source Address:** The IP address of the sender of that packet.  
  **Source Address:** IP Address ของผู้ส่ง Packet นั้น
- **Destination Address:** The IP address of the intended recipient of that packet.  
  **Destination Address:** IP Address ของปลายทางที่ Packet นั้นต้องการส่งไปถึง

For a request from a computer to a website, the source is the client-side address visible at the capture point, and the destination is the website's IP address.  
สำหรับ Request ที่ส่งจากคอมพิวเตอร์ไปยังเว็บไซต์ Source จะเป็น Address ฝั่ง Client ที่มองเห็นได้ ณ จุดที่จับ Packet ส่วน Destination จะเป็น IP Address ของเว็บไซต์

The values visible in a capture can depend on where the packet was captured, especially when NAT is involved.  
ค่าที่เห็นจากการจับ Packet อาจแตกต่างกันตามตำแหน่งที่จับข้อมูล โดยเฉพาะเมื่อมีการใช้ NAT

When analyzing traffic, check the packet direction and capture location before interpreting the addresses.  
เมื่อวิเคราะห์ Traffic ควรตรวจสอบทิศทางของ Packet และตำแหน่งที่จับข้อมูลก่อนตีความ Address

## 6. Key Takeaways — สรุปประเด็นสำคัญ

- IPv4 uses **32 bits**, divided into four **8-bit octets**.  
  IPv4 ใช้ข้อมูล **32 บิต** แบ่งเป็น 4 Octet โดยแต่ละ Octet มี **8 บิต**
- Each octet ranges from decimal `0` to `255`.  
  แต่ละ Octet มีค่าเลขฐานสิบตั้งแต่ `0` ถึง `255`
- `192.168.1.100` in binary is `11000000.10101000.00000001.01100100`.  
  `192.168.1.100` ในรูปแบบเลขฐานสองคือ `11000000.10101000.00000001.01100100`
- IP addresses are logical addresses; the lesson describes MAC addresses as physical addresses.  
  IP Address เป็นที่อยู่เชิงตรรกะ ส่วนบทเรียนเรียก MAC Address ว่าที่อยู่ทางกายภาพ
- The lesson introduces classes A–E; Class D is for multicast and Class E is reserved in its diagram.  
  บทเรียนแนะนำ Class A–E โดย Class D ใช้สำหรับ Multicast และ Class E เป็นช่วงที่สงวนไว้ตามแผนภาพ
- `127`-starting addresses are identified as loopback addresses in the lesson.  
  บทเรียนระบุว่า Address ที่ขึ้นต้นด้วย `127` เป็น Loopback Address
- The private IPv4 ranges are `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`.  
  ช่วง Private IPv4 ได้แก่ `10.0.0.0/8`, `172.16.0.0/12` และ `192.168.0.0/16`
- In packet analysis, the source identifies the sender and the destination identifies the recipient of that packet.  
  ในการวิเคราะห์ Packet ค่า Source ใช้ระบุผู้ส่ง และ Destination ใช้ระบุปลายทางของ Packet นั้น
