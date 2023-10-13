def kataSingkat(kata):
    katatengah = len(kata)//2
    hasil = kata[1:katatengah] + kata[katatengah+1:-1]

    return hasil



"""
testcase

"""



# print(kataSingkat("AkuSukaCilok"))

print(kataSingkat("James"))

print(kataSingkat("Bakso"))

print(kataSingkat("Presiden"))


