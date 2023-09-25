beliau = [7, 69, 2, 221, 8974]
dia = [5,5,5,5,5]

def MaxMin(ar):
    mt = []
    for i in ar:
        mt.append(sum(ar) - i)
    return max(mt), min(mt)
    
print (f"{int(MaxMin(beliau)[1])} {int(MaxMin(beliau)[0])} ")
print (f"{int(MaxMin(dia)[1])} {int(MaxMin(dia)[0])} ")


print (beliau.index(221))

# def miniMaxSum(aku):
#     mt = []
#     for i in aku:
#         mt.append(sum([x for x in aku if x != i]))
#     return print (f"{int(max(mt))} {int(min(mt))}")


# miniMaxSum(aku)
        
