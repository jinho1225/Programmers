#대소문자 바꾸기

a=list(input())

for i in range(len(a)):
    if i==0 or i%2==0:
        a[i]=a[i].upper()

for j in range(len(a)):
     print(a[j], end='')