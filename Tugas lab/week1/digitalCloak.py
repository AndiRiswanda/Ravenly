detik = int(input("Masukan detik: "))

#conversi detik ke jam,menit,detik
jam = detik // 3600
menit = detik % 3600 // 60
detik = detik % 3600 % 60

#diasumsikan tidak mengikuti batas 24 jam..
print (f"{jam:02}:{menit:02}:{detik:02}")