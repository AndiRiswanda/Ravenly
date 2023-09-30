def palindorme(string):
    '''
    fungsi yang akan menerima input string
    akan mereverse string tersebut dan 
    melakukan pengecekan sama atau tidaknya
    reverse string dan string asli
    
    '''
    biasa = ("".join(map(str,[huruf for huruf in string if huruf.isalnum])))
    reverse = biasa[::-1]

    if reverse.lower() == biasa.lower():
        print ("PALINDROME\n")
    else:
        print ("bukan PALINDROME\n")

palindorme("Step on no pets")
palindorme("bububgaknih")
palindorme("Radar")
palindorme("akuSukaCilok")
palindorme("A man, a plan, a canal, Panama!")
palindorme("12321")
