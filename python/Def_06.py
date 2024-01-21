# Def - 함수

def print_list(a): # 지금부터 print_list 함수를 만들겠다는 뜻 / a 는 매개변수
    for i in a:
        print(i)

print_list(range(1, 5))

# 연습 문제 : 자릿수를 구하는 함수 만들기

def numOfDigit(num):        # 함수 정의
    print(len(str(num)))    # 실수값 - 갯수 - 출력

numOfDigit(str(input()))    # 입력 값을 받아 함수 실행

# 연습 문제 : 구구단

a = 2
b = 1

while b <= 9:
    c = a * b
    print(str(a) + ' * ' + str(b) + ' = ' + str(c))
    b += 1

# 함수로 실행

def multi(m):                           # 함수 정의
    for n in range(1, 10):              # n 원소 대입
        print(f'{m} * {n} = {m*n:2d}')  # 공식 - 출력

m = 2

while m <= 9:   # 2 ~ 9 단까지 반복
    multi(m)
    m += 1

# 지역 변수 / 전역 변수
    
def d_is_10():
    d = 10          # 지역변수 - 함수가 끝나면 사라지는 변수
    print('d 값은 ', d, '입니다')

x = 10              # 전역변수 - 함수에 상관 없이 사용할수 있는 변수
def print():
    print(x)

def e_is_10():
    global e        # 전역변수 / 함수 안에서 전역변수 정의, 사라지지 않음
    e = 10
    print('e 값은 ', e, '입니다')