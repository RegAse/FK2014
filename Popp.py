cases = int(input())
popp = []
hi = 0
last = 0
key = ""
for test in range(0,cases):
    a,b = map(int,input().split())
    popp.append(a)
    popp.append(b)
for k in range(1,max(popp) + 1):
    hi = 0
    for u in range(0,len(popp),2):
        if k >= popp[u] and popp[u + 1] + popp[u] > k:
            hi += 1
            if hi > last:
                last = hi
                key = k
print(key,last)