import hashlib

name = "Henri_De_Toulouse-Lautrec"
hash_object = hashlib.sha256(name.encode())
hash_hex = hash_object.hexdigest()

flag = f"ctf{{{hash_hex}}}"
print(flag)