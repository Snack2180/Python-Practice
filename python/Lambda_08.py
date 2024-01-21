# Lambda = 함수를 한 줄로 정의할수 있음
# lambda 매개변수 : 표현식

def hap(x, y):      # 두 수를 더하는 함수
    return x + y

(lambda x, y : x + y)(10, 20) # lambda를 사용해 한 줄로 정의

# map 함수 = 리스트에서 원소를 함수에 적용시켜 새로운 리스트 작성

map(lambda x: x ** 2, range(5))         # map(함수, 리스트)
[0, 1, 4, 9, 16]
list(map(lambda x: x ** 2, range(5)))   # 다른 내용
[0, 1, 4, 9, 16]

# reduce 함수 = 시퀀스 (문자열, 리스트, 튜플) 원소들을 누적하며 함수에 적용

from functools import reduce                    #
reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])     # reduce(함수, 시퀀스)
10

# filter 함수 = 리스트에 있는 원소들을 함수에 적용시켜 결과가 참인 값들로 새로운 리스트 작성

filter(lambda x: x < 5, range(10))              # 5 미만의 원소만 참
[0, 1, 2, 3, 4]

# 이터러블 - 순회 가능한 / 이터레이터 - 순회 가능하게 해주는