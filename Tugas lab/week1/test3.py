a = 50

for b in range (a):
    for c in range(b):
        
        if b%2 == 0:
            if c%2 == 0:
                print ("+", end= (""))
            else:
                print ("-", end= (""))
        else:
            if c%2 == 0:
                print ("-", end= (""))
            else:
                print ("+", end= (""))
        


    print ()



# a = 5
# for v in range(1,a+1):
#     print (f"\n{v}")
#     for b in range (1,v):
#         print("#")
#         if b == (v-1):
#             print("#", end= (""))
#         for i in range (b):
#                 print("#",end= "")

# for a in range(5):
#     for b in range (a):
#         if b%2 == 0:
#             print ("#", end= " ")
#         else:
#             print ()
#     print ()