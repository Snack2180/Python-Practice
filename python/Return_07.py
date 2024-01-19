# return 함수 = 반환

def f1(x):              # 함수 정의
    return 3 * x + 5    # 계산값 반환

print(f1(7))

# 삼각형 넓이 구하는 함수

def tri_area(a, b):         # 함수 정의
    return a * b / 2        # 반환 값 

a = int(input())
b = int(input())

print(tri_area(a, b))

# 연습 문제 : 숫자 읽기 함수

X = int(input())            # 읽어질 숫자 값

def korean_number(n):       # 함수 정의
    if n == 1:
        n = "일"
    elif n == 2:
        n = "이"
    elif n == 3:
        n = "삼"
    return n

print(korean_number(X))     ## print 는 입력 인자가 없거나, return 값이 없을 시 None 출력