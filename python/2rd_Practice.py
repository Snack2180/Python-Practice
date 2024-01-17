### While문 = 반복문 ( 조건을 만족할 때 까지 반복한다)

num = 1 # 변수 지정

while num <= 50: # while = 반복문 (조건을 만족할 때까지 반복) / While문 마지막은 : 넣기
    print(num)
    num = num + 2 # num += 2  똑같은 의미

# 연습문제 : 입력받은 숫자만큼 반복하기

NUM = int(input()) # 입력 값을 변수로 정의

i = 0
while i <= NUM:    # 반복문
    print('', NUM) # 입력받은 정수 출력
    i += 1         # 조건 (입력받은 정수만큼 1씩 증가)

# 연습문제 : 제곱표
    
Num = int(input()) # 입력 값을 변수로 정의

z = 1
while z <= Num:     # 반복문
    print(z, z * z) # 출력
    z = z + 1       # 조건