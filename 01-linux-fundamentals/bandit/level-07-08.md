# Bandit Level 7 → Level 8

## Goal

Find the password for the next level. It is stored in `data.txt` next to the word `millionth`.

## Approach (วิธีทำ)

1. Search for the word `millionth` in `data.txt`.

   ```bash
   grep 'millionth' data.txt
   ```

2. Read the output to find the line containing the target word.

   `grep` displays lines that contain the specified text.

   (`grep` แสดงบรรทัดที่มีข้อความที่เราต้องการค้นหา)

3. The output contained the password for the next level.

## Result (ผลลัพธ์)

Found the password for Bandit Level 8 and saved it locally.

## What I Learned (สิ่งที่ได้เรียนรู้)

- `grep` searches for matching text in a file.  
  (`grep` ใช้ค้นหาข้อความที่ตรงกับคำค้นหาในไฟล์)

- `grep` displays the entire line containing the matching text.  
  (`grep` แสดงทั้งบรรทัดที่พบข้อความที่ค้นหา)

- The matching text does not have to be at the beginning of a line.  
  (ข้อความที่ค้นหาไม่จำเป็นต้องอยู่ต้นบรรทัด)