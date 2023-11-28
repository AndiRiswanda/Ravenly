# def enkirsi(N, S):
#     hasil = ""
#     for i in range(N):
#         if S[i] != "*" and (S[:i].count("*"))% 2 == 0 and (S[i+1:].count("*"))% 2 == 0:
#             hasil += S[i]
#     return hasil
# N = int(input())
# S = input()
# print(enkirsi(N, S))

A = "ab.ab."
N = len(A)

def agenvalid(N,A):
    A = list(A)
    cek = {"a" : A.count("a"),
           "b" : A.count("b"),
           "c" : A.count("c"),}
    count = 0
    hasil = ""
    savefor = ""
    for key,item in cek.items():
        if item == 0:
            count += 1
            savefor += key
        if count == 2:
            return -1
        
    sui = ["a","b","c"]
    for i in range(N):
        
        if A[i] == ".":
            A[i] = sui[0]
            sui.pop(0)
    return("".join(A))
    

print(agenvalid(N,A))
