# 전화번호 가리기

a=list(input())                 # 전화번호 입력 / 리스트로 저장
for i in range(len(a)-4):       # 입력받은 전화번호에서 끝의 네자리를 제외하고 * 로 변경
    a[i]='*'

for i in range (len(a)):        # 전화번호 출력
    print(a[i], end = '')