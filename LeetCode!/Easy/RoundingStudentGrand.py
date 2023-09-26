grades = [73,67,38,33]
student = 5

z = []
for i in grades:
    x = (i // 5 + 1) * 5
    if x >= 40:
        if x - i < 3:
            z.append(x)
        else:
            z.append(i)
    else :
        z.append(i)
    print (z)

