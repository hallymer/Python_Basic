# Chapter05-1
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def function_name(parameter):
#     code

# 예제1
# func = function의 축약
def first_func(w1): # w1같은 인수명은 임의로 지정해줘도 상관없다
    print("Hello, ", w1)

word = "Goodboy"

first_func(word) # parameter 변수명도 임의로 지정해줘도 상관없다
print()

# 예제2
def return_func(w1):
    value = "Hello, " + str(w1)
    return value
    # return "Hello, " + str(w1) 가능하다

x = return_func('Goodboy2')
print(x)
print()

"""
return은 간단히 말하면 함수에서 값을 돌려주기 위해서 사용하는 명령문
함수란 x를 집어 넣으면 처리를 통해 y라는 값을 돌려주는 역할을 하는 것!
즉, 함수에 값을 넣으면 계산된 값을 돌려준다는 것이 핵심이다.
파이썬에서는 return을 통해 값을 반환한다
"""

# 예제3(다중반환)

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)

print(x, y ,z)
print()

# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mul2(20)

print(type(q), q, list(q))

# 리스트 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

p = func_mul2(30)

print(type(p), p, set(p))

# 딕셔너리 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2': y2, 'v3': y3}

d = func_mul3(30)
print(type(d), d, d.get('v2'), d.items(), d.keys())
print()

# 중요
# *args, **kwargs

# *args(언팩킹)
def args_func(*args): # 매개변수 명 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-----')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')
print()

# **kwargs(언팩킹)
def kwargs_func(**kwargs): # 매개변수 명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-----')

kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Cho')

# * 한개, ** 두개 공통점은 가변인자를 사용할 수 있게해준다는 것
# 차이점은 매개변수 형태가 다르다 * 한개인 경우는 튜플형태, **두개인 경우는 딕셔너리형태(key : value)로 사용한다
# ** 2개는 키워드 매개변수로 주로 사용한다.
print()

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', 'Cho', age1=20, age2=30, age3=40)
print()

# 중첩함수

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

nested_func(100)

# 실행불가
# func_in_func(1000)
print()

# 람다식 예제
# 람다식의 장점 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

# def mul_func(x, y):
#     return x * y

# lambda x, y:x*y

# 일반적함수 -> 할당
def mul_func(x, y):
    return x * y

print(mul_func(10, 50))

mul_func_var = mul_func
print(mul_func_var(20,50))
print()

# 람다 함수 -> 할당
lambda_mul_func = lambda x,y:x*y
print(lambda_mul_func(50,50))
print()

def func_final(x, y, func):
    print('>>>>', x * y * func(100, 100))

func_final(10, 20, lambda_mul_func)
print()

# Hint
def tot_length1(word: str, num: int) -> int:
    return len(word) * num


print('hint exam1 : ', tot_length1("i love you", 10))


def tot_length2(word: str, num: int) -> None:
    print('hint exam2 : ', len(word) * num)


tot_length2("niceman", 10)
