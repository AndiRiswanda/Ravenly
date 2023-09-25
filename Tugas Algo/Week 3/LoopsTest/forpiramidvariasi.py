b = 5

for a in range (b):
    print("#"*(a+1))
print()

for a in range (b):
    print(" "*(b-a), end=(""))
    print("#"*(a+1), end=(""))
    print("#"*(a+1))
print()

for a in range (b):
    print("#"*(b-a))

for a in range (b):
    print(" "*(b-a), end=(""))
    print("#"*(a+1))
print()

for a in range (b):
    print(" "*(b),end=(""))
    print("#"*(b-a))

    

for a in range (b):
    print(" "*(b-a), end=(""))
    print("#"*(a+1))