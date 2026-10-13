# Bandit Level 4 → Level 5

## Goal

Find the password for the next level. It is stored in the only human-readable file inside the `inhere` directory.

## Approach (วิธีทำ)

1. Enter the `inhere` directory.

   ```bash
   cd inhere
   ```

2. Check the file types.

   ```bash
   file ./*
   ```

3. Identify the file reported as human-readable text.

   (ดูผลลัพธ์เพื่อหาไฟล์ที่สามารถอ่านข้อความได้)

4. Display the file's contents.

   ```bash
   cat <filename>
   ```

   Replace `<filename>` with the actual filename found in the output.

## Result (ผลลัพธ์)

Found the password for Bandit Level 5 and saved it locally.

## What I Learned (สิ่งที่ได้เรียนรู้)

- `file` identifies file types.
- `./*` matches non-hidden entries in the current directory.
- `cat` displays file contents.
- A file's name or extension does not always tell you what type of data it contains.

  (ชื่อไฟล์หรือนามสกุลไม่ได้บอกประเภทข้อมูลภายในได้ถูกต้องเสมอไป)