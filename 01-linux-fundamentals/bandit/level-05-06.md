# Bandit Level 5 → Level 6

## Goal

Find the password for the next level. The file is stored somewhere under the `inhere` directory and has these properties:

- Human-readable
- 1033 bytes in size
- Not executable

## Approach (วิธีทำ)

1. Search for a file with the required size.

   ```bash
   find . -size 1033c
   ```

   `.` starts the search from the current directory. `find` also searches through subdirectories.

   (`find` ค้นหาภายใน Directory ปัจจุบันและ Directory ย่อยทั้งหมด)

2. Check the file type.

   ```bash
   file ./maybehere07/.file2
   ```

   Output:

   ```text
   ./maybehere07/.file2: ASCII text, with very long lines (1000)
   ```

3. Read the file.

   ```bash
   cat ./maybehere07/.file2
   ```

   The file contained the password for the next level.

## Result (ผลลัพธ์)

Found the password for Bandit Level 6 and saved it locally.

## What I Learned (สิ่งที่ได้เรียนรู้)

- `find` can search through nested directories.
- `-size 1033c` matches a file size of exactly 1033 bytes.
- `file` identifies file types.
- `cat` displays file contents.