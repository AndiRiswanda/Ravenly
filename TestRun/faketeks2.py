import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''


pattern = r"[a-zA-z\-\.1-9]+@[a-zA-Z-]+\.\w+"

result = re.match(pattern, emails)
result2 = re.finditer(pattern, emails)
print(result)

for iter in result2:
    print (iter)


if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")