# a = 5
'''
STEP 1

'''

# for b in range (a):
#     for c in range (-1,b):
#         print("O", end=(""))
#     print (end="\n")

# b = 0 1 2 3 4

'''
print default funtion
jika end= dari print tidak dinyatakan maka print akan mengasumsikan end = "\n"
print(object(s), sep=separator, end="\n", file=file, flush=flush)

'''

'''
STEP 2

'''
# for b in range (a):
#     for c in range (-1,b):
#         if c % 2 == 0:
#             print("+", end=(""))
#         else:
#             print("-", end=(""))
#     print ()



'''
STEP 3

'''
# for b in range (a):
#     if b % 2 == 0:
#         for c in range (-1,b):
#             if c % 2 == 0:
#                 print("+", end=(""))
#             else:
#                 print("-", end=(""))
#     if b % 2 != 0:
#         for c in range (-1,b):
#             if c % 2 == 0:
#                 print("-", end=(""))
#             else:
#                 print("+", end=(""))
#     print ()


'''
STEP 4

'''
def piramid(input):
    for b in range (input):
        if b % 2 == 0:
            for c in range (-1,b):
                if c % 2 == 0:
                    print("-", end="")
                else:
                    print("+", end="")
        if b % 2 != 0:
            for c in range (-1,b):
                if c % 2 == 0:
                    print("+", end="")
                else:
                    print("-", end="")
        print ()

piramid (10)
