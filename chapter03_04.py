# Chapter03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) # 불변

# 선언
# 소괄호로 묶어주면 그것이 선언이다.

a = () # 이것이 바로 튜플이다
b = (1,) # 원소가 하나일때는 ,를 찍어줘야 튜플로 인식한다!
c = (11, 12, 13, 14)
d = (100, 1000,'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine')) # 튜플 안에 튜플도 중첩 선언이 가능하다

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1]) # Captine으로 출력
print('e - ', e[-1][1]) # ('Ace', 'Base', 'Captine')에 첫번째이니깐 Base가 출력
print('e - ', list(e[-1][1])) # 튜플에서 리스트로 형변환

# 수정 X
# d[0] = 1500
# print('d - ', d)

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산
print('>>>>>')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
#print("c[0] + 'hi' - ",c[0] + 'hi') # 튜플은 절대 never 수정,삭제가 안된다.
print("'Test' + c[0] - ", 'Test' + str(c[0]))

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(5))
print('a - ', a.count(4))

# 팩킹 & 언팩킹(Packing, and Unpacking)

# 팩킹
# 여러가지를 패키지 하나로 묶는것
t = ('foo', 'bar', 'baz', 'qux')

# 출력 확인
print(t)
print(t[0])
print(t[-1])

# 언팩킹1
# 묶여있던 걸  풀어서 각각의 순서에 맞는 원소에 대입이 되는것
# 하나로 되어있던 튜플을 풀어서 각각 할당을 해주는 것
(x1, x2, x3, x4) = t # 소괄호가 있어도 없어도 언패킹이 되지만, 관습상 소괄호를 해줘야한다~

# 출력확인
print(type(x1), type(x2), type(x3), type(x4))
print(x1)
print(x2)
print(x3)
print(x4)

# 언팩킹2
(x1, x2, x3, x4) = ('foo', 'bar', 'baz', 'qux')

# 출력 확인
print(type(x1), type(x2), type(x3), type(x4))
print(x1)
print(x2)
print(x3)
print(x4)

# 팩킹 & 언팩킹
t2  =1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

# 출력 확인
print(t2)
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)

"""
tuple(튜플)은 불변한 순서가 있는 객체의 집합입니다.
list형과 비슷하지만 한 번 생성되면 값을 변경할 수 없습니다.
REPL에서 확인해봅니다.

list와 마찬가지로 다양한 타입이 함께 포함될 수 있습니다.
"""
