# THE ULTIMATE HACKERANK TUTORIAL wAHAAHAH


# THE ULTIMATE 2 ITERATING SHIT
n = 5
ii = []
jj = []
for i in range(n-1):
    ii.append(i)
    for j in range(i+1,n):
        jj.append(j)

print(ii)
a = [0, 1, 2, 3]
print(jj)
[1, 2, 3, 4,        2, 3, 4,     3, 4,      4]

for i in range(1,len(a)):
    print(a[i])




"""ALICELEADERBOARD"""
def climbingLeaderboard(ranked, player):
    ranked = sorted(set(ranked), reverse=True)
    ranks = []
    l = len(ranked)

    for score in player:
        while (l > 0) and (score >= ranked[l-1]):
            l -= 1
        ranks.append(l+1)

    return ranks
