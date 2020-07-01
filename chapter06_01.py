# Chapter06-1
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 쉽게 말하면, 클래스는 붕어빵 틀 인스턴스는 틀에 찍어서 나온 붕어빵
# 인스턴스와 객체의 차이점 --> 인스턴스가 어떻게 보면 객체에 포함된다고도 볼 수 있다.
# 인스턴스는 내가 직접 코드를 구현해서 메모리에 올라간 그 시점이고 어떤 변수로 활용할 수 있는 그 대상이라고 생각

# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1
class Dog: # 모든 class는 object를 상속받는다.
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화 <-- 설계도를 바탕으로 구현된 것
a = Dog("mikky",2)
b = Dog("baby",3)

# 비교
print(a == b, id(a), id(b))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

# 예제2
# self의 이해
class SelfTest:
    def func1(): # --> 클래스 메소드
        print('Func1 called')
    def func2(self): #
        print(id(self))
        print('Func2 called')
# 여기에는 왜 init메소드가 없나?
# 없으면 파이썬이 내부적으로 알아서 이 코드가 클래스를 만들때 알아서 내부적으로 실행해준다.

f = SelfTest()

# print(dir(f))
print(id(f))
# f.func1() # 예외
f.func2()

# self는 인스턴스를 요구한다.
# 즉, 암묵적으로 클래스 내부의 매개 변수를 선언하는데 self가 없다 --> 클래스 메소드이다.
SelfTest.func1() # --> 클래스에 바로 접근해 직접 호출
# SelfTest.func2() # 예외
SelfTest.func2(f)

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0 # 재고

    def __init__(self, name): # --> 생성자
        # 인스턴스 변수 --> 나만의 것
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self): # --> 소멸자
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
# Warehouse.stock_num = 0.0094
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)
# 인스턴스 네임스페이스에 없으면 클래스의 네임스페이스 가서 찾아보기 클래스에 네임스페이스가 없으면 에러가 뜬다

del user1
print('after', Warehouse.__dict__)

# 예제4
class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)


# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))
