# 연습 문제 : 함수 정의하기

t = int(input())

def triple(x):
    return x * 3

print(triple(t))

a = triple
print(a(3))