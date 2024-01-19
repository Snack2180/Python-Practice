# match - case 문

for n in range(1, 11):              # 범위 지정 / 원소 중 하나 대입
    match n % 2:                    # 원소를 나눔
        case 0:                     # 나머지가 0 : 짝수
            print(f"{n} is even.")
        case 1:                     # 나머지가 1 : 홀수
            print(f"{n} is odd.")

print("\nFizzBuzz\n")           # 피즈 버즈 (Fizz Buzz) - 나눗셈을 가르치는 단어 게임

for a in range(1, 12):
    match (n % 3, n % 5):
        case (0, 0):            # 위의 식을 평가 / 나머지가 둘다 0 인 경우
            print("FizzBuzz")
        case (0, _):            # 3으로 나눈 나머지가 0
            print("Fizz")
        case (_, 0):            # 5로 나눈 나머지가 0
            print("Buzz")
        case _:                 # 그 밖의 모든 경우
            print(n)

# for - else
            
for x in [1, 10]:
    if x % 3:                   # x 가 3의 배수가 아니면 출력
        print(x)
    else:
        break                   # x 가 3의 배수이면 반복문에서 빠져나감
else:
    print('리스트의 원소를 모두 출력했어요.')

# while - else

countdown = 5               # 변수 값 지정
while countdown > 0:        # 반복문 조건
    print(countdown)
    countdown -= 1          # 1 씩 빼짐
    if input() == '중단':   # 중단을 치면 멈춤
        break
else:
    print('발사!')