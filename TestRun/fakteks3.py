import re
kata = """www.amazon.com
linkgadung.id
www.Youtube.com"""



pattern = (r'w{3}\.([a-zA-Z]+)+\.com')

hasil = re.search(pattern,kata)
print(hasil)
count = 0
# for a in hasil:
    
#     print(f"{a}")

#     count +=1



# if hasil:
#     print("ditemukan")
# else:
#     print("tidak ada ditemukan")