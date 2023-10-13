def kataSingkat(kata):
    try:
        panjang = len(kata)

        depan = kata[0]

        if panjang%2 == 0:
            tengah = (kata[(panjang//2)-1])+ (kata[panjang//2])
        else:
            tengah = (kata[panjang//2]) 

        belakang = kata[panjang-1]

        return (f"{depan}{tengah}{belakang}")
    
    except TypeError: return ("Input Invalid")


"""
testcase

"""

print(kataSingkat("AkuSukaCilok"))

print(kataSingkat("James"))

print(kataSingkat("Bakso"))

print(kataSingkat("Presiden"))


