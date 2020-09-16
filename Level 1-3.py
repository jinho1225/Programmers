#배열 중복 제거

a=list(map(int,input()))
b=[]

for i in a:
    if i not in b:
        b.append(i)

print(b)