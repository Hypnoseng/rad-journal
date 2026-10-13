# Bandit Level 1 → 2

## Goal

Find the password for Level 2.

## Commands (คำสั่งที่ใช้)

### 1. List files (แสดงรายการไฟล์)

```bash
ls -l
```

The output showed a file named `-`.

(ผลลัพธ์แสดงไฟล์ชื่อ `-`)

### 2. Read the file (อ่านเนื้อหาไฟล์)

```bash
cat ./-
```

The `./` prefix tells the command to read the file from the current directory.

(`./` ใช้ระบุว่าไฟล์อยู่ในไดเรกทอรีปัจจุบัน ช่วยป้องกันไม่ให้ `-` ถูกตีความเป็น option)

## What I Learned (สิ่งที่ได้เรียนรู้)

- `ls -l` shows file details. (แสดงรายละเอียดของไฟล์)
- `cat` displays file contents. (แสดงเนื้อหาไฟล์)
- `./` specifies a path from the current directory. (ระบุพาธจากไดเรกทอรีปัจจุบัน)

## Result (ผลลัพธ์)

Found the password for Level 2.

Passwords are stored locally and are not included in this repository.

(เก็บรหัสผ่านไว้ในเครื่องเท่านั้น และไม่อัปโหลดลง GitHub)
