import os
import re

os.chdir("C:/Users/ASUS/OneDrive/Documents/RavenlyRepo/TestRun")
with open("data.txt","r") as data:
    isi = (data.read())
    nomorHP = re.finditer(r'\d{3}.\d{3}.\d{4}',isi)
    for nomor in nomorHP:
        print(nomor)
    """
    nicolewhite@bogusemail.com
    """
    pattern = re.compile(r"([a-zA-Z\._])+@([a-zA-Z])+(\.\w{3})")
    listemail = re.findall(r"([a-zA-Z\._])+@([a-zA-Z])+(\.\w{3})", isi)

    """
    Naming
        ?P<name>...

    """
    for email in listemail:
        print(email)

    potongemail = pattern.sub(r"\3",isi)
    print(potongemail)
    