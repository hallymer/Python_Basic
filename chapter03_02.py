# Chapter03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4)) # len 함수는 공백 포함해서 문자열의 길이를 알려준다.

# 빈 문자열
str1_t1 = ''
str1_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str1_t2), len(str1_t2))

# 이스케이프 문자 사용
"""
참고 : Escape 코드

\n : 개행(줄바꿈)
\t : 탭
\\ : \문자
\' : '문자
\" : "문자
\000 : 널 문자
...

"""
escape_str1 = "Do you have a \"retro games\"?"
escape_str2 = 'What\'s on TV?'

# 출력1
print(escape_str1)
print(escape_str2)

# 탭, 줄바꿈
t_s1 = "Click \tStart!"
t_s2 = "New Line\n Check!"

# 출력2
print(t_s1)
print(t_s2)

# Raw String
raw_s1 = r'D:\Python\python3' # 소문자 r가 붙으면 \를 있는 그대로 표시할 수 있
raw_s2 = r"\\x\y\z\q"


# Raw String 출력
print(raw_s1)
print(raw_s2)

# 멀티라인 입력
# 멀티라인을 이용하려면 역슬러시를 사용해라!
multi_str = \
'''
String
Multi Line
Test
'''
print(multi_str)

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

# 기억하기!
print(str_o1 * 3) # Python을 3번 반복해서 출력
print(str_o1 + str_o2)
print('y' in str_o1) # y라는 알파벳이 str_o1에 있는지 확인해준다.
print('n' in str_o1) # Chapter03-1에 언급된 시퀀스들은 in 연산자를 사용할 수 있다.
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startwith, count, endswith, isalpha...)

print("Capitalize: ", str_o1.capitalize()) # 첫번째 시작 문자를 대문자로 바꿔주는 함수
print("endswith: ", str_o2.endswith("s")) # 마지막 문자가 무엇인지 체크할때 사용하는 함수
print("join str: ", str_o1.join(["I'm ", "!"])) # 리스트에 특정 구분자를 추가하여 문자열을 변환하는 함수
print("replace1: ",str_o1.replace("thon", ' Good'))
print("replace2: ", str_o3.replace("are", "was"))
print("sorted: ", sorted(str_o1)) # 문자열을 입력받아 기준에 맞게 정렬한 후 리스트 형태로 반환하는 함수
print("split: ", str_o4.split(' ')) # 특정 단어를 분리할때, 단어 단위나 문장 단위로 분리할 때 많이 사용하는 함
print("reversed1: ", reversed(str_o2))
print("reversed2: ", list(reversed(str_o2))) # list 형 변환

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # __iter__가 있으면 시퀀스를 반복할 수 있다는 것!

# 출력
for i in im_str:
    print(i)

# 슬라이싱 [start : end]
str_sl = "Nice Python"

# 슬라이싱 연습
print(str_sl[0:3]) # [start : end] []안에 시작과 끝 인덱스를 지정하면 해당 범위의 리스트를 잘라서 갖고온다.
# 주의할 점 end인덱스는 가져오려는 범위에 포함되지 않는다. 실제로 가져오려는 인덱스보다 1을 더 크게 지정한다.
print(str_sl[5:]) # str_sl[5:11]
print(str_sl[:len(str_sl)]) # str_sl[:11]이랑 같은것
print(str_sl[:len(str_sl)-1]) # str_sl[:10] 이니깐 0~9까지만 가져왔기때문에 'n'을 출력못함.
print(str_sl[1:9:2]) # [start:end:step] 몇개 단위로 점프(skip)하면서 가져올건지
print(str_sl[-5:]) # 음수가되면 오른쪽부터 출력된다.
print(str_sl[1:-2])
print(str_sl[::2]) # 처음부터 끝까지 2칸씩 간격으로 가져온다
print(str_sl[::-1]) # Nice Python이 역으로 출력된다.
# 음수는 오른쪽에서 왼쪽으로 일반적인 방향은 0부터 오른쪽으로

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a)) # 아스키 코드로 변환
print(chr(122)) # 문자로 변환
