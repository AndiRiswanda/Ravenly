from random import randint
import time
import os

output = 'Hello, World!'
out = ""



def binary(n):
    return ''.join(str(randint(0, 1)) for _ in range(n))
os.system("cls")
for i in output:
    for j in range(10):
        if i != " " or i != ",":

            bin1 = binary(5)+ " " 
            bin2 = " " + binary(5)
            maintext = out + output[randint(0, len(output)-1)]

            print("\033[32m" + 
                bin1 + maintext + bin2 +"\033[0m", end='\r')


            time.sleep(0.05)
        else:
            
            bin1 = binary(5)+ " " 
            bin2 = " " + binary(5)
            maintext = out + " " 

            print("\033[32m" + 
                bin1 + maintext + bin2 +"\033[0m", end='\r')
            break


            
    out += i
os.system("cls")
print("\033[32m" +output +"\033[0m")
