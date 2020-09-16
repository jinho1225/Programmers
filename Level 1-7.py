# 수박수박수박수

a=['수','박']

b= int(input())

for i in range(1,b+1):
    if i %2 == 1 :
        print(a[0], end='')
    else:
        print(a[1],end='')