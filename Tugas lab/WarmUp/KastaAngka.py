n = 50

def kasta_angka(n):

    hasil =  ""

    if n <= 0:
        hasil += "A"
    elif n > 0 and n <= 100:
        hasil+= "B"
    elif n > 100 and n <= 200:
        hasil+= "C"
    elif n > 200:
        hasil+= "D"
    
    if n % 3 == 0:
        hasil += "3"
    elif n % 3 == 1:
        hasil += "1"
    elif n % 3 == 2:
        hasil += "3"
    return hasil


print(kasta_angka(50))

        
