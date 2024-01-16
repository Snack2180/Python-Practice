print("Hello World") # Hellow World 출력

Iphone = 1000000 # 변수 값 정의
Sphone = 500000 # 변수 값 정의

All = Iphone + Sphone # 두 변수 더하기
print(All) # 합친 값 출력

Sale = Iphone * 0.8 # 변수 연산
print(Sale)

print(type(Sale)) # 자료형 확인

# 자료형 - 숫자 (int 정수형, float 실수형), 문자열 (str), 불(Boolean)

# 문자열 출력
a = 'Hello' # 문자열
b = 'World' # 문자열
c = ' ' # 문자열 공백
print(a + c + b)

# 숫자 + 문자 출력
A, B, C = 12, 36, 48 # = 은 한 문장에 한 개
print(str(A) + '더하기' + str(B) + '=' + str(C)) # 숫자에서 문자로 변환해서 출력

aa, bb = 1, 2
print(f'{aa} + {bb} = {aa + bb}') # 간단하게 출력 {} < 변수로 인식

# 불 (Boolean) 자료형
x = True # 참 , 대소문자 주의
y = False # 거짓 , 소문자 > 변수로 인식