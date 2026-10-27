# Remove the corrupting 'BBBBBBBBBB' bytes from the file
with open("chall.jpg", "rb") as bad_img, open("flag.jpg", "wb") as flag_img:
    corrupted_data = bad_img.read()
    flag_img.write(corrupted_data.replace(b"BBBBBBBBBB", b""))