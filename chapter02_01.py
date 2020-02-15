# Chapter02-1
# 파이썬 완전 기초
# print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""
# 기본 출력
print('Python Start!') # '',""이 두개를 많이 사용한다.
print("Python Start!")
print('''Python Start!''') # print문에서는 잘 사용하지않는다. 기초문법이니깐 알아두자!
print("""Python Start!""")

print() # print만 작성하면 개행 즉, 줄바꿈을 의미한다.

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep= '') # sep를 사용하면 분리되어있던 문자열을 합쳐준다.
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션
print('Welcome to', end=' ') # end 옵션으로 들어간 문자로 다음 print문으로 이어질 수 있다.
print('IT News', end=' ')
print('Web Site')

print()

# file 옵션
import sys
print('Learn Python', file=sys.stdout) # sys.stdout 콘솔의 아웃을 의미

print()

# format 사용(d, s, f)
print('%s %s' % ('one','two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

print()

# %s (문자열)
print('%10s' % ('nice')) # %10s의 의미는 10개의 자리수를 의미 출력해보면 앎
                         # 양수인 경우 왼쪽부터 공백을 채우고 난 뒤 나머지 입력한 텍스트로 채워진다.
print('{:>10}'.format('nice'))
print('%-10s' % ('nice')) # 음수인 경우 오른쪽부터 공백을 채우고 난 뒤 나머지 입력한 텍스트로 채워진다.
print('{:10}'.format('nice')) # 기호가 생략되면 오른쪽을 공백으로 채운다.
print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice')) # 중앙정열은 ^표시를 해주면 알아서 위치시킨다.
print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy')) # 점을 붙이면 내가 원하는 자릿수만큼 왼쪽부터 다섯 글자만 절삭해서 출력한다.
                                # 공간은 5개
print('{:10.5}'.format('pythonstudy')) # 공간은 10개 10개중에 왼쪽부터 다섯 글자만 출력

# %d (정수)
print('%d %d' % (1,2))
print('{} {}'.format(1,2))
print('%4d' % (42))
print('{:4d}'.format(42))

print()

# %f (실수)
print('%f' % (3.14343434343))
print('{:f}'.format(3.14343434343))
print('%06.2f' % (3.141592653589793)) # 총 자릿수는 6이고 6개중에 정수부는 1자리기 때문에 나머지를 0으로 채워주고
                                      # 소수부 2자리이니깐 2개가 나온것. --> 003.14
print('{:06.2f}'.format(3.141592653589793))
