# 문자열

x = 'Big Money '
x[2]            # x 에서 2번 글자
'g'

x[:4]           # x 에서 처음부터 4번 까지
'Big M'

x[1] != 'B'     # 문자열에 들어가있는 글자는 바꿀 수 없음

x.find('B')     # 글자가 몇번째 자리에 있는지 찾기
0

x.rstrip()      # 오른쪽 공백 제거    
'Big Money'

x.split()       # 문자열 분할
['Big', 'Money']

# 리스트

Num = [2, 1, 8, 0]

Num.append(4)       # Num 에 4 를 추가
Num
[2, 1, 8, 0, 4]

Num.sort()          # Num 을 정렬
Num
[0, 1, 2, 4, 8]

Num.insert(3, 7)
Num
[0, 1, 7, 2, 4, 8]

del Num(1)
Num
[0, 7, 2, 4, 8]

a = Num.pop()
a
1