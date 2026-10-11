# Kali Linux Environment Setup
## Environment

- OS: Kali Linux 2026.2  
- Virtualization: Oracle VirtualBox  
- Network mode: NAT  
  โหมดเครือข่าย: NAT ซึ่งช่วยให้เครื่องเสมือนเชื่อมต่อเครือข่ายภายนอกผ่านระบบเครือข่ายของเครื่อง Host ได้

## System Verification

### User

Command:

```bash
whoami
```

Result: `kali`  
ผลลัพธ์: ชื่อผู้ใช้งานปัจจุบันคือ `kali`

### Memory

Command:

```bash
free -h
```

Result: Approximately 3.8 GiB of memory available to the VM.  
ผลลัพธ์: เครื่องเสมือนมีหน่วยความจำที่ระบบตรวจพบประมาณ 3.8 GiB

### Disk

Command:

```bash
df -h /
```

Result: Root filesystem has approximately 59 GiB available.  
ผลลัพธ์: ระบบไฟล์ Root มีพื้นที่ว่างประมาณ 59 GiB

## Network Connectivity (การเชื่อมต่อเครือข่าย)

### IP Configuration (การตั้งค่า IP Address)

Command:
คำสั่ง:

```bash
ip addr
```

Observation: The network interface `eth0` is up and has IPv4 address `10.0.2.15/24`.  
ข้อสังเกต: Network interface ชื่อ `eth0` ทำงานอยู่ และมี IPv4 Address เป็น `10.0.2.15/24`

### IP Connectivity (การเชื่อมต่อด้วย IP Address)

Command:

```bash
ping -c 3 1.1.1.1
```

Result: 3 packets transmitted, 3 received, 0% packet loss.  
ผลลัพธ์: ส่งแพ็กเก็ต 3 แพ็กเก็ต ได้รับกลับครบทั้ง 3 แพ็กเก็ต และไม่มีแพ็กเก็ตสูญหาย

### DNS Resolution (การแปลงชื่อโดเมนเป็น IP Address)

Command:

```bash
getent hosts kali.org
```

Result: DNS resolution returned two IPv6 addresses.  
ผลลัพธ์: ระบบค้นหาชื่อโฮสต์และได้รับ IPv6 Address กลับมา 2 รายการสำหรับ `kali.org`

### HTTPS Connectivity (การเชื่อมต่อผ่าน HTTPS)
Command:

```bash
curl -I --max-time 10 https://kali.org
```

Result: The server returned `HTTP/2 301` and redirected to `https://www.kali.org/`.  
ผลลัพธ์: เซิร์ฟเวอร์ตอบกลับด้วยสถานะ `HTTP/2 301` ซึ่งหมายถึงมีการเปลี่ยนเส้นทางไปยัง `https://www.kali.org/`

## Conclusion

The VM boots successfully and basic IP connectivity, DNS resolution, and HTTPS connectivity have been verified.

เครื่องเสมือนสามารถเริ่มต้นระบบได้สำเร็จ และผ่านการตรวจสอบเบื้องต้นในด้านการเชื่อมต่อด้วย IP Address การค้นหาชื่อโดเมน และการเชื่อมต่อผ่าน HTTPS

These checks confirm basic connectivity, but do not constitute a comprehensive security assessment.

การทดสอบเหล่านี้ยืนยันเพียงว่าการเชื่อมต่อพื้นฐานทำงานได้ แต่ยังไม่ถือเป็นการประเมินความปลอดภัยของระบบอย่างครอบคลุม
