import re

pattern = '^a...s$'
test_string = "abyss"
result = re.match(pattern, test_string)
result1 = re.finditer(r"\w", test_string)



print ("\nresult findiiter\n")
for iter in result1:
    print (iter)
print ("\nresult match\n")
print (result)
print ("\n")




if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")