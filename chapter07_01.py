# Chapter07-1
# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError....
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)발생하는 예외도 중요

# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시 --> 좋은 방법은 아니다!

# SyntaxError : 문법 오류
# print('error)
# print('error'))
# if True
#   pass

# NameError : 참조 없음
# a = 10
# b = 15
# print(c)

# ZeroDivisionError

# print(100 / 0)

# IndexError

# x = [50, 70, 90]
# print(x[1])
# print(x[4])
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop()) --> 마지막은 빈 리스트이기 때문 출력하면 예외가 발생

# KeyError --> dictionary에서 나오는 에러

# dic = {'name': 'Lee', 'Age': 41, 'City': 'Busan'}
# print(dic['hobby'])
# print(dic.get('hobby')) --> get method를 쓰는게 좀 더 안전하다
# get method는 예외를 발생시키지 않고 없으면 None을 가져오기 때문 (dictionary에서 배운 내용!)

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAFP)
