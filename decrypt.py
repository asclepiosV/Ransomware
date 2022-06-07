#!/usr/local/bin/python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir("my_files"):
    if file == "script.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile("my_files/" + file):
        files.append(file)

print(files)


secretkey = input("Enter the secret phrase to decryp your files\n")

for file in files:
    with open("my_files/" + file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open("my_files/" + file, "wb") as thefile:
        thefile.write(contents_decrypted)
    print("Content decrypted")

print("All files are decrypted with the secret key")