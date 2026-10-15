# Network Overview

## Learning Objectives

- Understand what a computer network is and why devices communicate.
- Identify the roles of common network devices.
- Understand the basic structure of home, small office, and enterprise networks.

## 1. What Is a Network?

A computer network is a group of interconnected devices that communicate and exchange data.

เครือข่ายคอมพิวเตอร์คือกลุ่มอุปกรณ์ที่เชื่อมต่อกันเพื่อสื่อสารและแลกเปลี่ยนข้อมูล

Networks allow devices to share resources and access services such as websites, email, DNS, and databases.

## 2. Common Network Devices

| Device | Main Role |
|---|---|
| Router | Connects different networks and forwards IP packets. |
| Switch | Connects devices within a LAN and forwards Ethernet frames using MAC addresses. |
| Wireless Access Point (AP) | Allows wireless devices to connect to a network. |
| Firewall | Enforces security rules that control network traffic. |
| Server | Provides services such as web hosting, email, DNS, and databases. |

### Key Differences

- A switch primarily forwards frames within a local network.
- A router forwards packets between IP networks.
- A firewall applies traffic-control rules according to its configuration.
- A server provides services to clients.

**คำอธิบาย:** Switch ทำหน้าที่ส่งต่อ Ethernet frames ภายในเครือข่ายเป็นหลัก ส่วน Router ส่งต่อ IP packets ระหว่างเครือข่าย ขณะที่ Firewall ใช้กฎเพื่อควบคุมว่า Traffic แบบใดได้รับอนุญาต

These devices may be separate or combined into one physical device.

อุปกรณ์เหล่านี้อาจแยกเป็นคนละเครื่อง หรือรวมหลายหน้าที่ไว้ในอุปกรณ์เดียวก็ได้

## 3. Basic Network Environments

### Home Network

A typical home network may include:

- An Internet Service Provider (ISP).
- An Internet connection such as ADSL or FTTH.
- An ONT for fiber-optic connections.
- A router with Wi-Fi capabilities.
- Client devices such as computers and smartphones.

**คำอธิบาย:** FTTH คือการเชื่อมต่ออินเทอร์เน็ตผ่านใยแก้วนำแสงไปยังบ้าน ส่วน ONT ทำหน้าที่แปลงสัญญาณจากเครือข่ายใยแก้วนำแสงให้เป็นการเชื่อมต่อที่อุปกรณ์เครือข่ายภายในบ้านใช้งานได้

### Small Office Network

A small office may use separate routers, switches, and access points to connect wired and wireless devices.

Business networks may also require more control over access, security, and reliability.

### Medium and Large Enterprise Networks

Larger networks may use:

- Redundant network devices and links.
- High Availability (HA) to reduce service interruptions.
- Network segmentation to separate systems and control access.
- Software-Defined Networking (SDN).
- Network automation to manage complex infrastructure.

Redundancy can reduce the risk of a Single Point of Failure (SPOF), but only when the overall design avoids other critical dependencies.

**คำอธิบาย:** Redundancy คือการมีอุปกรณ์หรือเส้นทางสำรอง ส่วน Single Point of Failure (SPOF) คือจุดที่หากเกิดความเสียหายเพียงจุดเดียว อาจทำให้ระบบทั้งหมดหรือบริการสำคัญหยุดทำงานได้

## 4. Why Networking Matters for Security

Networking fundamentals help explain how systems communicate and where security controls operate.

ความรู้พื้นฐานด้านเครือข่ายช่วยให้เข้าใจว่าระบบสื่อสารกันอย่างไร และมีการควบคุมความปลอดภัยตรงจุดใดบ้าง

Relevant security applications include:

- Understanding which systems and services are reachable.
- Identifying the role of routers, switches, and firewalls.
- Understanding network boundaries and segmentation.
- Investigating connectivity and traffic using diagnostic tools.
- Understanding how clients communicate with servers.

In authorized security labs, these concepts provide the foundation for reconnaissance, service enumeration, and network traffic analysis.

**คำอธิบาย:** Reconnaissance คือการสำรวจข้อมูลเป้าหมาย ส่วน Service Enumeration คือการตรวจสอบรายละเอียดของบริการที่ระบบเปิดให้ใช้งาน ทั้งสองอย่างต้องทำภายในขอบเขตที่ได้รับอนุญาต

## 5. Key Takeaways

- A network enables devices to communicate and share resources.
- Switches primarily forward Ethernet frames within a LAN.
- Routers forward IP packets between networks.
- Access points provide wireless network connectivity.
- Firewalls enforce traffic-control policies.
- Servers provide services to clients.
- Enterprise networks require attention to availability, segmentation, and centralized management.
