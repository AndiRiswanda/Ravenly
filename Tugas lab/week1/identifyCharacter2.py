karakter = input("masukan karakter: ")

hurufbesar = karakter.isupper()
hurufkecil = karakter.islower()
nomer = karakter.isnumeric()


print(f'''huruf besar : {hurufbesar}
huruf kecil : {hurufkecil}
nomer: {nomer}''')