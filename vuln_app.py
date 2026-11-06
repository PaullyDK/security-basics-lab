import os
import pickle
import hashlib
import subprocess
import yaml
import sqlite3
import requests

PASSWORD = "admin123"
API_KEY = "sk_live_1234567890abcdef"

user_input = input("Enter value: ")

# command injection
os.system("ls " + user_input)
subprocess.run("ping -c 1 " + user_input, shell=True)

# unsafe code execution
eval(user_input)
exec(user_input)

# unsafe deserialization
pickle.loads(user_input.encode())
yaml.load(user_input)

# weak hashing
hashlib.md5(user_input.encode()).hexdigest()
hashlib.sha1(user_input.encode()).hexdigest()

# SQL injection
db = sqlite3.connect(":memory:")
db.execute("SELECT * FROM users WHERE name = '" + user_input + "'")
db.execute(f"SELECT * FROM users WHERE name = '{user_input}'")

# TLS verification disabled
requests.get("https://example.com", verify=False)
