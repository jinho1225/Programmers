#배열 중간값 출력

a=str(input())

if len(a)%2 != 0:
    print(a[len(a)//2])
else:
    print(a[len(a)//2 -1 : len(a)//2+1])