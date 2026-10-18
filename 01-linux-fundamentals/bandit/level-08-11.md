# OverTheWire Bandit — Level 8 to Level 11

## Level 8 → Level 9

### Goal (เป้าหมาย)

Find the only line in `data.txt` that occurs once.

ค้นหาบรรทัดเดียวใน `data.txt` ที่ปรากฏเพียงครั้งเดียว

### Approach (วิธีทำ)

First, I practiced `sort` and `uniq` in a local Kali Linux lab.

เริ่มจากทดลองใช้ `sort` และ `uniq` ใน Lab บน Kali Linux ก่อนนำไปแก้โจทย์จริง

```bash
sort data.txt
```

`sort` sorts the lines so identical lines appear next to each other.

`sort` เรียงลำดับบรรทัด เพื่อให้บรรทัดที่เหมือนกันอยู่ติดกัน

```bash
uniq data.txt
```

`uniq` removes adjacent duplicate lines. It does not detect duplicates that are separated by other lines.

`uniq` จัดการบรรทัดซ้ำที่อยู่ติดกันเท่านั้น หากบรรทัดที่เหมือนกันอยู่ห่างกัน จะไม่ถือว่าเป็นกลุ่มเดียวกัน

To display each line only once:

```bash
sort data.txt | uniq
```

คำสั่งนี้เรียงบรรทัดก่อน แล้วแสดงแต่ละบรรทัดเพียงครั้งเดียว

To display only lines that occur once:

```bash
sort data.txt | uniq -u
```

คำสั่งนี้แสดงเฉพาะบรรทัดที่ปรากฏเพียงครั้งเดียว

I then applied this technique to the Bandit challenge.

จากนั้นนำวิธีนี้ไปใช้กับโจทย์ Bandit จริง

### What I Learned (สิ่งที่ได้เรียนรู้)

- `sort` sorts lines. — ใช้เรียงลำดับบรรทัด
- `uniq` processes adjacent duplicate lines. — ใช้จัดการบรรทัดซ้ำที่อยู่ติดกัน
- `uniq -u` displays lines that occur only once. — ใช้แสดงบรรทัดที่ปรากฏครั้งเดียว
- The pipe (`|`) passes the output of one command to another. — ส่งผลลัพธ์จากคำสั่งหนึ่งไปเป็น input ของอีกคำสั่ง

---

## Level 9 → Level 10

### Goal (เป้าหมาย)

Find the password in `data.txt`. It is hidden among human-readable strings and is preceded by several `=` characters.

ค้นหา password ใน `data.txt` ซึ่งอยู่ในข้อความที่มนุษย์อ่านได้ และมีเครื่องหมาย `=` หลายตัวอยู่ข้างหน้า

### Approach (วิธีทำ)

First, I practiced extracting readable strings from a file containing binary data.

เริ่มจากฝึกดึงข้อความที่อ่านได้ออกจากไฟล์ที่มีข้อมูลไบนารี

```bash
file data.bin
strings data.bin
```

`file` identifies the type of a file. `strings` extracts readable character sequences from it.

`file` ใช้ตรวจสอบชนิดไฟล์ ส่วน `strings` ใช้ดึงลำดับตัวอักษรที่อ่านได้ออกมา

I then filtered the output:

```bash
strings data.bin | grep '='
```

This displays lines containing the `=` character.

คำสั่งนี้กรองให้เหลือเฉพาะบรรทัดที่มีเครื่องหมาย `=`

To filter lines that begin with several `=` characters:

```bash
strings data.bin | grep '^==='
```

The `^` pattern matches the beginning of a line.

เครื่องหมาย `^` ใน pattern ของ `grep` ใช้ระบุตำแหน่งเริ่มต้นของบรรทัด ดังนั้น `^===` จึงเลือกบรรทัดที่ขึ้นต้นด้วย `===`

I applied the same approach to the challenge file and used the challenge clues to identify the password.

จากนั้นใช้วิธีเดียวกันกับไฟล์โจทย์จริง และพิจารณาคำใบ้เพื่อระบุ password

### What I Learned (สิ่งที่ได้เรียนรู้)

- `strings` extracts readable text from a file. — ดึงข้อความที่อ่านได้จากไฟล์
- `grep` filters lines using a search pattern. — กรองบรรทัดด้วยรูปแบบการค้นหา
- `^` matches the beginning of a line. — ใช้ระบุตำแหน่งเริ่มต้นของบรรทัด
- Pipes help combine commands to reduce irrelevant output. — ใช้ pipe เชื่อมคำสั่งเพื่อลดผลลัพธ์ที่ไม่เกี่ยวข้อง

---

## Level 10 → Level 11

### Goal (เป้าหมาย)

Decode the Base64 data stored in `data.txt` to obtain the next password.

ถอดรหัสข้อมูล Base64 ใน `data.txt` เพื่อค้นหา password ของ Level ถัดไป

### Approach (วิธีทำ)

I created a local practice file and encoded it using Base64.

สร้างไฟล์สำหรับฝึกในเครื่อง แล้วแปลงข้อมูลเป็น Base64

```bash
base64 message.txt > encoded.txt
```

The encoded output was saved in `encoded.txt`.

ผลลัพธ์ที่ผ่านการแปลงถูกบันทึกลงใน `encoded.txt`

I then decoded the file:

```bash
base64 -d encoded.txt
```

The command decodes the Base64 data and prints the result.

คำสั่งนี้ถอดข้อมูล Base64 แล้วแสดงผลลัพธ์บน Terminal

I practiced the encoding and decoding process before applying the technique to the Bandit challenge.

ฝึกทั้งการแปลงและการถอดกลับก่อนนำแนวคิดไปใช้กับโจทย์ Bandit

### What I Learned (สิ่งที่ได้เรียนรู้)

- `base64` encodes data into Base64 representation. — แปลงข้อมูลให้อยู่ในรูปแบบ Base64
- `base64 -d` decodes Base64 data. — ถอดข้อมูล Base64 กลับ
- `>` redirects command output to a file. — เปลี่ยนปลายทาง output ให้บันทึกลงไฟล์
- Base64 is an encoding scheme, not encryption. — Base64 เป็นการเข้ารหัสรูปแบบข้อมูล (encoding) ไม่ใช่การเข้ารหัสลับ (encryption) จึงไม่ได้ป้องกันผู้อื่นอ่านข้อมูลด้วยตัวมันเอง

---

## Key Takeaways (สรุปสิ่งที่ได้เรียนรู้)

| Command | Purpose (หน้าที่) |
|---|---|
| `sort` | Sort lines (เรียงบรรทัด) |
| `uniq` | Process adjacent duplicates (จัดการบรรทัดซ้ำที่อยู่ติดกัน) |
| `strings` | Extract readable strings (ดึงข้อความที่อ่านได้) |
| `grep` | Search text using patterns (ค้นหาข้อความด้วย pattern) |
| `base64` | Encode or decode Base64 (แปลงหรือถอด Base64) |
| `\|` | Pass output between commands (ส่ง output ระหว่างคำสั่ง) |
| `>` | Redirect output to a file (เปลี่ยน output ไปยังไฟล์) |

The main lesson was to understand how each command works and combine simple tools to solve a problem.

บทเรียนสำคัญคือการเข้าใจหลักการทำงานของแต่ละคำสั่ง และนำเครื่องมือพื้นฐานมาเชื่อมต่อกันเพื่อแก้ปัญหา แทนการจำคำสั่งโดยไม่เข้าใจเหตุผล

*Passwords and other secrets are intentionally excluded from this write-up.*

ตั้งใจไม่ใส่ password หรือข้อมูลลับอื่น ๆ ลงใน Write-up นี้