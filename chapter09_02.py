# Chapter09-2
# CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제1
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader) Header Skip
    # 객체 확인
    print(reader)
    # 타입 확인
    print(type(reader))
    # 속성 확인
    print(dir(reader))  # __iter__
    print()

    for c in reader:
        # print(c)
        # 타입 확인
        print(type(c))
        # list to str
        print(''.join(c))

# 예제2
with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')  # 구분자 선택
    # next(reader) Header 스킵
    # 확인

    for c in reader:
        # print(c)
        print(''.join(c))
