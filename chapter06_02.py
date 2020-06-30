# Chapter06-02
# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y): # x의 y제곱
    return x ** y

# print('-' * 15)
# print('called! inner!')
# print(add(5,5))
# print(subtract(15,5))
# print(multiply(5,5))
# print(divide(10,5))
# print(power(5,3))
# print('-' * 15)


# __name__ 사용
# main은 실행되는 그 대상을 의 --> 내 자신을 실행하는 경우는 밑에 있는 것 처럼
# 바로 실행되는 것
if __name__ == "__main__":
    print('-' * 15)
    print('called! inner!')
    print(add(5,5))
    print(subtract(15,5))
    print(multiply(5,5))
    print(divide(10,5))
    print(power(5,3))
    print('-' * 15)
