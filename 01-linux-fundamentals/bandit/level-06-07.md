# Bandit Level 6 → Level 7

## Goal

Find the password for the next level. The file is stored somewhere on the server and has these properties:

- Owned by user `bandit7`
- Owned by group `bandit6`
- 33 bytes in size

## Approach (วิธีทำ)

1. Search from the root directory.

   ```bash
   find /
   ```

   `/` starts the search from the root directory and includes its subdirectories.

2. Filter files by size and ownership.

   ```bash
   find / -type f -user bandit7 -group bandit6 -size 33c
   ```

   - `-type f` searches for regular files.
   - `-user bandit7` matches files owned by `bandit7`.
   - `-group bandit6` matches files owned by group `bandit6`.
   - `-size 33c` matches files that are exactly 33 bytes.

3. Hide permission error messages.

   ```bash
   find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
   ```

   `2>/dev/null` redirects error messages to `/dev/null`, so they are not displayed.

   (ช่วยซ่อนข้อความ Error เช่น `Permission denied` โดยไม่ซ่อนผลลัพธ์ปกติ)

4. Read the matching file.

   ```bash
   cat /var/lib/dpkg/info/bandit7.password
   ```

## Result (ผลลัพธ์)

Found the password for Bandit Level 7 and saved it locally.

## What I Learned (สิ่งที่ได้เรียนรู้)

- `find` searches through nested directories.  
  (`find` ค้นหาไฟล์และ Directory ที่อยู่ภายใน Directory ย่อยได้ด้วย)

- `-user` and `-group` filter files by ownership.  
  (`-user` และ `-group` ใช้กรองไฟล์ตามเจ้าของไฟล์และกลุ่มเจ้าของไฟล์)

- `-size 33c` matches a file size of exactly 33 bytes.  
  (`-size 33c` ใช้ค้นหาไฟล์ที่มีขนาด 33 bytes พอดี)

- `2>/dev/null` hides error messages.  
  (`2>/dev/null` ใช้ซ่อนข้อความ Error ไม่ให้แสดงใน Terminal)

- Multiple `find` conditions can be combined to narrow down results.  
  (เราสามารถรวมหลายเงื่อนไขใน `find` เพื่อจำกัดผลการค้นหาให้แคบลงได้)