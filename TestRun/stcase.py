n = 1008
kur = set(str(n))
print(kur)
pembagibulat = 0
for i in kur:
    if i     != 0:
        if (n/int(i))%2 == 0:
            pembagibulat += 1
    else :
        pass
print(pembagibulat)