import os 
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
    if file == "file.txt" or file == "hi.txt":
        files.append(file)
print(files)
with open ("thekey.key", 'rb') as key:
    unlock_key=key.read()
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypt = Fernet(unlock_key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypt)
print("\nYour files are dencrypted!\n")        