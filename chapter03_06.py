# Chapter03-6
# 집합(Sets) 특징
# 집합(Sets) 자료형(순서X, 중복X)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
# *주의* 키가 없이 원소만 나열한다면 리스트를 나열하듯이 하면 집합(Sets)이다!
# {}는 딕셔너리(Dictionary)에도 사용하지만 set에도 사용한다!!
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()
# in 연산자도 사용할 수 있는 이유는 튜플이나 리스트에서 사용하는 것, 딕셔너리에서 하는 것은 다 할 수 있다

# 튜플 변환 (set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])
print()

# 리스트 변환 (set -> list)
l = list(c)
l2 = list(e)
print('l - ', type(l), l)
print('l - ', l[0], l[1:3])
print('l2 - ', type(l2), l2)
print()

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))
print()

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2)) # intersection : 교집합

print('s1 | s2 : ', s1 | s2)
print('s1 | s2 : ', s1.union(s2)) # union : 합집합

print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2)) # difference : 차집합
