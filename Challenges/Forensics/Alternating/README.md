# Alternating

- **Category:** Forensics
- **Event:** DefCamp 2024 Quals
- **Points:** 500

## Description

We have hidden something in the file and I'm sure you won't find it. Make sure to extract the archive using WinRar. Windows is your friend.

## Solution Analysis

1. The challenge description explicitly points to **WinRAR** and **Windows**, indicating the use of **NTFS Alternate Data Streams (ADS)**.
2. Standard extraction tools discard ADS metadata, meaning the archive must be extracted using WinRAR on an NTFS file system.
3. Upon extracting via WinRAR, `Flag.txt.txt` appears as a 0-byte file because the content is hidden inside the attached stream (`:real_flag.txt`).
4. Reading the alternate stream using PowerShell reveals the flag:
   ```powershell
   Get-Content -Path "Flag.txt.txt" -Stream "real_flag.txt"
   ```
