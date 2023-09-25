x = int(input('Panjang Sisi x: '))
y = int(input('Panjang Sisi y: '))
#mencari nilai z

z = (x**2 + y**2)** 0.5

#mencari luas permukaan
keliling = x + y + z
luasPermukaan = x * y / 2

print (f"luas permukaan adalah {luasPermukaan:.2f}")
print (f"keliling adalah {keliling:.2f}")