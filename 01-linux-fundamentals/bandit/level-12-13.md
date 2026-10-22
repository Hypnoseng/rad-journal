# Bandit Level 12 → Level 13

## Goal

The password for the next level is stored in `data.txt`. The file is a
hexdump of a file that has been compressed multiple times.

## Approach 

1.  Create a temporary working directory so the original file stays
    untouched.
2.  Copy `data.txt` into the working directory.
3.  Convert the hexdump back into binary data.
4.  Identify the file type with `file`.
5.  Decompress or extract one layer at a time. After each step, run
    `file` again to identify the next format.
6.  Repeat until the result is readable text, then read the password for
    the next level.

## Commands Used

``` bash
mktemp -d
cp ~/data.txt .
xxd -r data.txt > data
file data
```

For later layers, use the command that matches the file type reported by
`file`:

``` bash
gzip -d <file>
bzip2 -d <file>
tar -xf <archive>
```

If a decompressor expects a file extension, rename the working copy with
`mv` first. Check the result with `file` after every decompression or
extraction step.

> Note: The exact sequence of compression formats depends on the file's
> contents. Identify each layer rather than assuming a fixed order.

## What I Learned 

-   A hexdump is a readable representation of binary bytes; `xxd -r`
    converts it back to binary data.
-   `file` helps identify a file's format from its contents, not just
    its filename extension.
-   Compression can be nested, so each layer must be handled separately.
-   `gzip` and `bzip2` decompress compressed files; `tar -xf` extracts
    an archive.
-   A temporary directory and a copied working file help protect the
    original challenge file.

## Result (ผลลัพธ์)

Solved Level 12 → Level 13 and obtained the next level's password.

The password is intentionally not included in this write-up.
