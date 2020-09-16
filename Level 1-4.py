#완주 못함 사람 찾기


a=list(input().split()) # 참가자
b=list(input().split()) # 완주자
c=[]
a.sort()
b.sort()

for i in range(len(b)):
    if a[i] != b[i]:
        c.append(a[i])

print(c)