# tabel ilmiah
f = ["vertebrado", "invertebrado"]
s = ["ave", "mamifero", "inseto", "analideo"]
l = ["onivoro", "carnivoro", "herbivoro", "hematofago"]

def validity(masukan, validinput):
    while True:
        usput = input(masukan).lower()
        if usput in validinput:
            return usput
        else :
            print ("invalid input")

first = validity(("masukan Input Pertama: "),f)
second = validity(("masukan Input kedua: "),s)
last = validity(("masukan Input ketiga: "),l)

match (first, second, last):
    case "vertebrado", "ave", "onivoro":
        print ("pomba")
    case "vertebrado", "ave", "carnivoro":
        print ("aguia")
    case "vertebrado","mamifero","onivoro":
        print ("homem")
    case "vertebrado","mamifero","herbivoro":
        print ("vaca")

    case "invertebrado","inseto", "hematofago":
          print ("pulga")
    case "invertebrado","inseto", "herbivoro":
          print ("lagarta")
    case "invertebrado","analideo","hematofago":
        print ("sanguessuga")  
    case "invertebrado","analideo","onivoro":
        print ("minhoca")
    case _:
        print ("invalid input")