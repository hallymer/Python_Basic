# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용 (JSON)
# 딕셔너리 자료형(순서X, 키 중복X, 수정O, 삭제O)

# 선언
# key는 어떤 자료형이든 지정할수있다
a = {'name': 'Kim', 'phone': '01012345678', 'birth': '870124'} # {key : value}
b = {0: 'Hello python!'}
c = {'arr': [1, 2, 3, 4]} # key만 존재한다면 value는 어떠한 자료형태도 들어올 수 있다
d = {
	 'Name' : 'Niceman',
	 'City'   : 'Seoul',
	 'Age': '33',
	 'Grade': 'A',
	 'Status'  : True
}
e =  dict([
	 ( 'Name', 'Niceman'),
	 ('City', 'Seoul'),
	 ('Age', '33'),
	 ('Grade', 'A'),
	 ('Status', True)
])

f =  dict(
	 Name='Niceman',
	 City='Seoul',
	 Age='33',
	 Grade='A',
	 Status=True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(c), e)
print('f - ', type(c), f)
print()

# 출력
print('a - ', a['name'])  # 존재X -> 에러 발생
print('a - ', a.get('name'))  # 존재X -> None 처리
print('b - ', b[0])
print('b - ', b.get(0))
print('c - ', c['arr'])
print('c - ', c['arr'][3])
print('c - ', c.get('arr'))
print('d - ', d.get('Age'))
print('e - ', e.get('Grade'))
print('f - ', f.get('City'))
# 키에 해당하는 값을 가져올 때는 get 메소드를 가져오는 것이 안전하다
# Why? Error발생을 하지않고 None처리가 되기때문에

# 딕셔너리 추가
# 바로 속성으로 접근해서 추가 또는 기존의 key가 있으면 수정이 되고 없으면 추가가 된다
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 딕셔너리 길이
print(len(a)) # len 함수는 키의 길이를 세는 것
print(len(b))
print(len(d))
print(len(e))
print()

# dict_keys, dict_values, dict_items : 반복문(iterate) 사용 가능
# keys 메소드는 key값만 가져오는 메소드
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ', list(a.keys())) # 리스트로 형 변환
print('b - ', list(b.keys()))
print('c - ', list(c.keys()))
print('d - ', list(d.keys()))
print()

# values 메소드는 value값만 가져오는 메소드
print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('d - ', d.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))
print('c - ', list(c.values()))
print('d - ', list(d.values()))
print()

# items 메소드를 사용하면 key와 value하면 리스트로 나오면서 튜플 형태로 key의 갯수만큼 출력
print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())
print('d - ', d.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))
print('c - ', list(c.items()))
print('d - ', list(d.items()))
print()

print('a - ', a.pop('name')) # pop()함수는 리스트의 마지막에 있는 요소를 리턴하고 그 요소는 삭제하는 함수
print('a - ', a)
print('b - ', b.pop(0))
print('b - ', b)
print('c - ', c.pop('arr'))
print('c - ', c)
print('d - ', d.pop('City'))
print('d - ', d)
print()

print('f - ', f.popitem()) # popitem()함수는 임의의 데이터(key,value)을 리턴하고 삭제 (데이터가 없으면 오류)
print('f - ', f.popitem()) # 추첨기 만들때 유용
print('f - ', f.popitem())
print('f - ', f.popitem())
print('f - ', f.popitem())
# 예외
# print('f - ', f.popitem())
print()

# pop이 들어가면 원본에 있는 데이터는 무조건 삭제가 된다

# in 연산자 : key가 있는지 포함되어있는지 즉흥적으로 쉽게 조회할 수 있다.
print('a - ', 'name' in a)
print('a - ', 'addr' in a)

# 수정
a['test'] = 'test_dict'
print('a - ', a)

a['address'] = 'dj'
print('a - ', a)

a.update(birth = '910904')
print('a - ', a)
temp = {'address': 'Busan'}
a.update(temp)
print('a - ', a)

f.update(Age=36)
temp = {'Age': 27}
print('f - ', f)
f.update(temp)
print('f - ', f)
