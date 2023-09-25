# tabel ilmiah


first   = (input("masukan Input Pertama: "))
second  = (input("masukan Input Kedua: "))
last    = (input("masukan Input Ketiga: "))

match first:

    case "vertebrado":
        match second:
            case "ave":
                match last:

                    case "carnivoro":
                            print ("aguia")
                    case "onivoro":
                            print ("pomba")
                    case _:
                         print (f'Invalid "{last}" input')

            case "mamifero":
                 match last:

                    case "onivoro":
                        print ("homem")
                    case "herbivoro":
                        print ("vaca")
                    case _:
                         print (f'Invalid "{last}" input')
            case _:
               print (f'Invalid "{second}" input')
     
    case "invertebrado":
        
        match second:
            case "inseto":
                   match last:

                    case "hematofago":
                            print ("pulga")
                    case "herbivoro":
                            print ("lagarta")
                    case _:
                        print (f'Invalid "{last}" input')

            case "anelideo":
                   match last:

                    case "hematofago":
                            print ("sanguessuga")
                    case "onivoro":
                            print ("minhoca")
                    case _:
                        print (f'Invalid "{last}" input')

            case _:
                print (f'Invalid "{second}" input')
    case _:
          print (f'Invalid "{first}" input')
