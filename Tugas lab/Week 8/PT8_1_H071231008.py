import re 


def stringtulin(string):
    pattern = (r"[a-zA-Z2468]{40}[\s13579]{5}")
    hasil = re.match(pattern,string)
    if hasil:
        return True
    else: return False

print(stringtulin("subafubvj6Bdcvishafiafbkifaoiaffubvsdsdd33 33"))

print(stringtulin("aaaaaaaaaaaaaaaa3aaaaaaaaaaaaaaaaaaaaaaa33 33"))

print(stringtulin("aaaaaaaaaa4aaaaa2aaaaaaaa8aaaaaaa6aaaaaa1  33"))

print(stringtulin("aaaaaaaaaaagaaaaa2aaadadadadsadsdsadadaa33 33"))

print(stringtulin("dasdhadihs2482664grjtohjkypdadasddsadasd33 33"))

print(stringtulin("aaaaaaaaaaaaaa a2aaaaaaaaaaaaaaaaaaaaaaa33 33"))

print(stringtulin("aaaaaaaaaaaaaaa2aaaaaaaaaaaaaaaaaaaaaaa33 33"))