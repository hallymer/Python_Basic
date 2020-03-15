# Chapter04-2
# 파이썬 반복문
# FOR 실습

# for문은 if문처럼 코딩의 핵심!!

# for문 사용법
# for i in <collection>
#     <loop body>
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

for v1 in range(10): # 0부터 시작이니 N-1 시작 예를들면 10까지출력이라하면 0~9로 출력
    print("v1 is :", v1)

print()

for v2 in range(1, 11): # start : 1 end : 10 (n-1이니깐)
    print("v2 is :", v2)

print()

for v3 in range(1, 11, 2): # start : 1 end : 10 (n-1이니깐) step : 2
    print("v3 is :", v3)

print()

# 1 ~ 1000합
sum1 = 0

for v in range(1, 1001):
    sum1 += v

print('1 ~ 1000 Sum : ', sum1)

print('1 ~ 1000 Sum : ', sum(range(1, 1001)))  # sum(리스트)
print('1 ~ 1000 안에 4의 배수의 합 : ', sum(range(1, 1001, 4)))
print()
# Iterables(반복 가능한) 자료형
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]

for name in names:
    print("You are : ", name)
print()

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for number in lotto_numbers:
    print("Current number : ", number)
print()

# 예제3
word = 'Beautiful'

for s in word:
    print('word : ', s)
print()

# 예제4
my_info = {
    "name": "Lee",
    "Age": 33,
    "City": "Seoul"
}

for key in my_info:
    print(key, ":", my_info[key]) # get메소드를 이용하여 갖고와도 되고 my_info[]속성으로 접근해서 갖고와도 된다!
print()

for val in my_info.values(): # values는 값만 갖고오는 것 keys는 키만 가져오는 것 items는 키와 밸류를 다 가져오는 것
    print(val)
print()

# 예제5
name = 'FineApplE'

for n in name:
    if n.isupper(): # isupper()는 문자열의 전체가 대문자인지 Boolean형태(True,Flase)로 구분
        print(n)
    else:
        print(n.upper()) # upper()는 문자열을 모두 대문자로 바꿔준다


# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:
        print("Found : 34!")
        break
    else:
        print("Not found : ", num)
print()

# continue
# continue문은 어떤 조건안에서 continue를 만나면 다시 조건을 검사하는 부분으 이동한다
lt = ["1", 2, 5, True, 4.3, complex(4)] # complex는 복소수형

for v in lt:
    if type(v) is bool:
        continue # 쉽게 말해서 continue를 만나면 아랫구문은 실행되지않고 skip이다

    print()
    print("current type : ", v, type(v))
    print("multiply by 2 :", v * 3)
print()

# else 구문
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 24:  # 45
        print("Found : 24!")
        break
else:
    print("Not Found 24...")
# for - else에서 else문은 for문에 반복하는 모든 원소를 전부 반복했을 경우 마지막으로 else문을 실행
# 단, break문으로 도중에 for문을 빠져나가거나 또는 어떤 리턴 등으로 인해서 종료가 되었을경우에는
# else문은 실행되지 않는다
print()

# 구구단 출력

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end='') # {:4d}는 출력 폭을 4칸으로 하겠다는 의미
    print()
print()

# 변환 예제
name2 = 'Aceman'
print('Reversed : ', reversed(name2))
print('List : ', list(reversed(name2)))
print('Tuple : ', tuple(reversed(name2)))
print('Set : ', set(reversed(name2)))  # 순서X
