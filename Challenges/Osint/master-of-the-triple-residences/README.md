# master-of-the-triple-residences

- **Category:** OSINT
- **Difficulty:** Medium
- **Points:** 500

## Description

Patricia Lareme is our secret agent. She likes to walk down in a nice square cut in three streets. In one of those streets, a famous artist lived there at number 19, 19bis and 21. Find his full name and you will get the flag.

## Solution Analysis

1. Researching the address numbers `19, 19bis, 21` (located on Avenue Frochot in Paris) points to the residence of the famous French post-impressionist painter **Henri de Toulouse-Lautrec**.
2. Following the formatting rules (`name separated with underscore and capital letters at every word`), the name becomes:
   `Henri_De_Toulouse-Lautrec`
3. Computing the SHA-256 hash of this string yields the flag.

## Solution Script

solve.py
