# Bandit Level 11 → Level 12

## Level Goal

The password for the next level is stored in `data.txt`, where all
lowercase (`a-z`) and uppercase (`A-Z`) letters have been rotated by 13
positions.

ไฟล์ `data.txt` เก็บ password ของ Level ถัดไป
โดยตัวอักษรภาษาอังกฤษทั้งตัวพิมพ์เล็กและตัวพิมพ์ใหญ่ถูกเลื่อนไป 13 ตำแหน่ง

## Approach (วิธีทำ)

I practiced ROT13 in a local Kali Linux lab using `tr` before applying
the same idea to the Bandit challenge.

ฉันฝึกใช้ `tr` เพื่อทำ ROT13 ใน Lab บน Kali Linux ก่อนนำแนวคิดไปใช้กับโจทย์ Bandit

``` bash
tr 'a-z' 'n-za-m' < message.txt
```

This translates lowercase letters by 13 positions. ROT13 is reversible:
applying it a second time restores the original text.

คำสั่งนี้เลื่อนตัวอักษรพิมพ์เล็กไป 13 ตำแหน่ง และเนื่องจาก ROT13 สามารถย้อนกลับได้
การทำซ้ำอีกครั้งจะได้ข้อความเดิม

For both lowercase and uppercase letters:

``` bash
tr 'A-Za-z' 'N-ZA-Mn-za-m' < message.txt
```

I then used the same ROT13 transformation on the challenge's `data.txt`
to obtain the next level's password.

จากนั้นใช้การแปลง ROT13 แบบเดียวกันกับ `data.txt` ของโจทย์เพื่ออ่าน password ของ
Level ถัดไป

## What I Learned (สิ่งที่ได้เรียนรู้)

-   `tr` translates or transforms characters. --- ใช้แปลงอักขระตามชุดที่กำหนด
-   ROT13 shifts each English letter by 13 positions. ---
    เลื่อนตัวอักษรภาษาอังกฤษไป 13 ตำแหน่ง
-   ROT13 is a simple substitution encoding, not encryption that
    provides meaningful confidentiality. --- ROT13
    เป็นการแทนที่ตัวอักษรอย่างง่าย ไม่ใช่การเข้ารหัสลับที่ให้ความปลอดภัยจริง
-   The character ranges must account for both uppercase and lowercase
    letters when both appear in the input. ---
    ต้องกำหนดช่วงตัวพิมพ์ใหญ่และตัวพิมพ์เล็กให้ครบ หากข้อมูลมีทั้งสองแบบ

## Result (ผลลัพธ์)

Solved Level 11 → Level 12 and continued to the next Bandit level.

ผ่าน Level 11 → Level 12 และดำเนินการต่อไปยัง Level ถัดไป

*Passwords and other secrets are intentionally excluded from this
write-up.*
