import os 
from cryptography.fernet import Fernet
files = []
file_name_count = 0
with open("encrypted_files", "r") as thefile:
     file_names = thefile.read()
     file_name_count = 1
files = [file for file in os.listdir() if file in file_names]

if  len(files) < file_name_count :
        print("Files not found!")
else:
    print("Files to be decrypted:", files)
with open ("thekey.key", 'rb') as key:
    unlock_key=key.read()
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypt = Fernet(unlock_key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypt)
print("\nYour files are decrypted!\n")