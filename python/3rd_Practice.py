### If - Elif - Else = 조건문 (조건을 만족하면 명령어 실행, 만족하지 못하면 다른 명령어 실행)

a = 10
b = 7

if a > b:       # 조건 a 가 b 보다 크면
    print(a)    # a 를 출력
else:           # 그렇지 않으면
    print(b)    # b 를 출력

# elif - 조건을 추가할 수 있음
    
c = 12 * 34
d = 43 * 21

if c > d:                           # 조건 1 : c 가 d 보다 크면
    print('C is greater than d')
elif c == d:                        # 조건 2 : c 와 d 가 같으면
    print('c is equal to d')
elif c < d:                         # 조건 3 : c 가 d 보다 작으면
    print('c is less than d')
else:                               # 그렇지 않으면
    print('I don\'t know')          # 출력할 때 기호를 입력하기 위해선 기호 앞에\ 추가

## == 연산자 - c 와 d 의 값이 같은가 ? / c = d 와 같지않음 (d의 값을 c에 대입)
    
ten = 10

while True:
    num = int(input())
    if num > ten:
        print(num, 'is too big!')
        break

# 연습 문제 : 숫자 읽기
    
N = int(input())    # 입력 값 변수로 정의

if N == 1:          # 입력 값이 1일 때
    print('일')
elif N == 2:        # 입력 값이 2일 때
    print('이')
elif N == 3:        # 입력 값이 3일 때 / 마무리를 else, elif 차이가 있는지 ?
    print('삼')     # else 는 나머지 조건의 경우

# 연습 문제 : 나이에 따른 세대 구분

y = int(input('What year were you born? ')) # 나이 입력 받기

gen = None

if y <= 1924:
    gen = 'The Greatest Generation'
elif y <= 1945:
    gen = 'The silent Generation'
elif y <= 1964:
    gen = 'a baby boomer'
elif y <= 1980:
    gen = 'a Gen X'
elif y <= 1996:
    gen = 'a Millennial'
else:
    gen = 'a Gen Z'

    print(f"you're {gen}.")