def palindorme(string: str) -> str:
    kataAwal = ("".join(map(str,[huruf for huruf in string if huruf.isalnum()])))

    if kataAwal.lower() == (kataAwal[::-1]).lower():
        print ("PALINDROME\n")
    else:
        print ("bukan PALINDROME\n")

palindorme("Step on no pets")
palindorme("bububgaknih")
palindorme("Radar")
palindorme("akuSukaCilok")
palindorme("A man, a plan, a canal, Panama!")
palindorme("12321")
palindorme(input())
