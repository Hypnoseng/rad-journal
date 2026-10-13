# Bandit Level 2 → 3

## Goal

Find the password for Level 3.

## Commands (คำสั่งที่ใช้)

### 1. Read a file with spaces (อ่านไฟล์ที่มีช่องว่าง)

```bash
cat './--spaces in this filename--'
```

The quotes keep the filename together as one argument.

(เครื่องหมายคำพูดช่วยให้ Shell ส่งชื่อไฟล์ทั้งหมดเป็น argument เดียว)

### 2. Handle a filename starting with a dash (จัดการชื่อไฟล์ที่ขึ้นต้นด้วยขีดกลาง)

The `./` prefix specifies a file in the current directory.

(`./` ใช้ระบุไฟล์ในไดเรกทอรีปัจจุบัน)

## What I Learned (สิ่งที่ได้เรียนรู้)

- Quotes help handle filenames containing spaces. (เครื่องหมายคำพูดช่วยจัดการชื่อไฟล์ที่มีช่องว่าง)
- Backslashes can escape spaces in Bash. (แบ็กสแลชช่วย escape ช่องว่างใน Bash)
- `./` specifies a path from the current directory. (ระบุพาธจากไดเรกทอรีปัจจุบัน)

## Result (ผลลัพธ์)

Found the password for Level 3.

Passwords are stored locally and are not included in this repository.

(เก็บรหัสผ่านไว้ในเครื่องเท่านั้น และไม่อัปโหลดลง GitHub)
