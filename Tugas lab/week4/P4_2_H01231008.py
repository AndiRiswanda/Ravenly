def palindorme(string):
    biasa = ("".join(map(str,[huruf for huruf in string if huruf not in "? !,."])))
    reverse = biasa[::-1]
    if reverse.lower() == biasa.lower():
        print ("PALINDROME\n")
    else:
        print ("bukan PALINDROME\n")

palindorme("Step on no pets")
palindorme("bububgaknih")
palindorme("Radar")
palindorme("aku")
palindorme("A man, a plan, a canal, Panama!")
palindorme("12321")
