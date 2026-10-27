# BBBBBBBBBB

- **Category:** Forensics / Misc
- **Difficulty:** Easy
- **Points:** 500

## Description

BBBBBBBBBB BBBBBBBBBB BBBBBBBBBB...

## Solution Analysis

1. Extracted `chall.jpg` from the provided ZIP archive.
2. Inspecting the raw bytes showed repeated `BBBBBBBBBB` padding bytes corrupting the JPEG structure.
3. Used a Python script to strip out all instances of `b"BBBBBBBBBB"`.
4. Opened the cleaned `flag.jpg` image to read the flag.

## Solution Script

The automation script can be found in [`solve.py`](./solve.py):

```python
with open("chall.jpg", "rb") as bad_img, open("flag.jpg", "wb") as flag_img:
    corrupted_data = bad_img.read()
    flag_img.write(corrupted_data.replace(b"BBBBBBBBBB", b""))
```
