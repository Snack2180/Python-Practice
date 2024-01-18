# for 문 = 원하는 명령을 반복

family = ['father', 'mother', 'big sister', 'small sister']

for x in family:        # family의 각 항목 x 에 대하여
    print(x, len(x))    # x 와 x 의 길이를 출력

# range() = 어떤 정수의 인자로 범위 안의 정수 만듦
    
A = list(range(3, 9))   # 3 이상 9 미만
range(3, 9)
print(A)

for cake in A:         # A 안에 있는 정수 나열 
    print(cake)        # for ~ in X / X 에 있는 원소를 ~에 대입

# 연습문제 : 입력받은 숫자만큼 반복하기
    
num = int(input())

for i in range(num): # num 값에 대하여
    print('', num)   # 입출력 구분

# 연습문제 : 제곱표

Num = int(input())          # 변수 입력

for y in range(1, Num + 1): # 1 부터 변수값까지 범위 설정 / 원소를 y 에 대입
    print(y, y * y)

# 연습문제 : 화학 실험실
    
Min, Max = (input().split())            # 다중 입력값 받기
Min = int(Min)                          # 받은 입력값을 정수형으로 정의
Max = int(Max)
T = int(input())                        # 입력받을 온도 변수

while T != -999:                        # -999 를 받을 때 까지 반복
    if T <= Min:                        # 온도가 최솟값보다 작을때
        print("Alert!")
        break
    elif T >= Max:                      # 온도가 최댓값보다 클 때
        print("Alert!")
        break
    elif Min <= T <= Max:               # 온도가 적정값일 때
        print("Nothing to report")
    T = int(input())                    # 다시 입력받을 온도 받기

# 문제 풀이 단계 1. 문제 해석 2. 쪼개서 하나씩 코딩 3. 실행 하면서 오류 찾기
    
# 1. 온도 입력값 2. 반복적으로 3. 입력값과 최소 최대 온도의 비교 4. 출력
    
L = input().split() # 다중 입력 값을 list 로 나열
a = int(L[0])       # list 첫번째 값
b = int(L[2])       # list 세번째 값
c = int(L[3])       # list 네번째 값