c = int(input("celcius yang ingin di konversi? "))

# Dari Celsius ke Kelvin:
# Rumus: K = °C + 273.15
kelvin = c + 273.15

# Dari Celsius ke Reamur:
# Rumus: °Re = °C × 0.8
reamur = c * 0.8

# Dari Celsius ke Fahrenheit:
# Rumus: °F = (°C × 9/5) + 32
fahrenheit = (c * 9/5) + 32


print(f'''{c} celcius ke kelvin adalah : {int(kelvin)}K,
{c} celcius ke Reamur adalah : {int(reamur)}R
{c} celcius ke fahrenheit adalah : {int(fahrenheit)}F''')





