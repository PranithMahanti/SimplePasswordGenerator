import random
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
num = string.digits
punc = string.punctuation

print("UPPERCASE:\tU\nLOWERCASE:\tL\nDIGITS:\t\tD\nSYMBOLS:\tS")
q = input("Enter your choice of combination: ")

full_combination = ""

if "U" in q.upper():
    full_combination += upper
if "L" in q.upper():
    full_combination += lower
if "D" in q.upper():
    full_combination += num
if "S" in q.upper():
    full_combination += punc


length = input("Enter the length of the password: ")
passwd = ""

for i in range(int(length)):
    passwd += random.choice(full_combination)

print(f"Generated Password: {passwd}")
