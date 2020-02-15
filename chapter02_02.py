# Chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700 #변수의 값을 할당한다.

# 출력
print(n)
print(type(n)) #type함수는 변수 n에 있는 값의 자료형을 보여준다.
print()

# 동시 선언
x = y = z = 700
print(x, y, z)
print()

# 선언
var = 75
# 재선언
var = "Change Value"

# 출력
print(var)
print(type(var))

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777
n = 777

print(n, type(n))
print()

m = n # n의 값을 m에 대입
# m -> 777 <- n

print(m, n)
print(type(m), type(n))
print()

m = 400

print(m, n)
print(type(m), type(n))
print()

# id(identity)확인 : 객체의 고유값 확인
m = 800
n = 655

print(id(m))
print(id(n))
print(id(m)==id(n))
print()

# 같은 오브젝트 참조
# 변수를 재사용하거나 똑같은 값을 할당할거면 파이썬 내부에서는 하나의 오브젝트로 생성.
# Why? 효율성과 생산성 속도 때문에!
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m)==id(n))
print()

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Method선언할때
# Pascal Case :  NumberOfCollegeGraduates -> Class선언할때
# Snake Case :  number_of_college_graduates -> 파이썬에서 변수로 선언할때 많이 사용 (전부 소문자)

# 허용하는 변수 선언 법
# 소문자나 Snake Case형태로 변수 선언하는 것이 매우 깔끔한 코드를 만들 수 있다는 것
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 예약어는 변수명으로 불가능
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not
class	from	or
continue	global	pass
"""
