import re
import os

os.chdir("C:/Users/ASUS/OneDrive/Documents/RavenlyRepo/TestRun")
pattern = r'\d{3}-\d{3}-\d{3}'


with open("number.txt", "r") as no1:
    hasil = no1.read()
    hasil2 = re.findall(pattern,hasil)
    for a in hasil2:
        print (a)