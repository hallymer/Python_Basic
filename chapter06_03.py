# Chapter06-3
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할된 개별적인 모듈로 구성
# __init__.py : Python3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
# 상대경로 : .. (부모 디렉토리), .(현재 디렉토) --> 모듈 내부에서만 사용

# 예제1
import sub.sub1.module1
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# 예제2
from sub.sub1 import module1
from sub.sub2 import module2 as m2 # as --> alias (별명)

# 사용
module1.mod1_test1()
module1.mod1_test2()

# 사용
m2.mod2_test1()
m2.mod2_test2()

print()
print()
print()

# 예제3
from sub.sub1 import *
from sub.sub2 import *
# *(별표)는 웬만하면 사용하지말자!
# 파이썬이 실행 될 때 모든 모듈을 다 사용하는 것이 아니기 때문
# 굳이 불 필요한 작업을 할 필요가 없다! 누적이되면 메모리를 잡아먹어 성능저하가 될 수 있다!

# 사용
module1.mod1_test1()
module1.mod1_test2()

# 사용
module2.mod2_test1()
module2.mod2_test2()

print()
print()
print()
