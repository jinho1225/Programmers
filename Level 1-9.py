# 두 수를 뽑아 만들 수 있는 모든 수

a= list(map(int,input()))
b=[]
c=[]

for i in range(len(a)):
    for j in range(i+1,len(a)):
        b.append(a[i]+a[j])

b.sort()

for i in b:
    if i not in c:
        c.append(i)
print(c)
