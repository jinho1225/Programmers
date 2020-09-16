# 물품 구매

a=list(map(int, input()))
b=int(input())
c=0
d=0

a.sort()

for i in range(len(a)):
    if  c + a[i] <= b:
        c += a[i]
        d += 1

print(d)