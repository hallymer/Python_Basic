# Chapter10-1
# Hangman(행맨) 미니 게임 제작(1)
# 기본 프로그램 제작 및 테스트

import time
# 처음 인사
name = input("What is your name?")

print("Hi, "+ name,"Time to play hangman game!")
print()

time.sleep(1)
print()
time.sleep(0.5)

# 정답 단어
word = "secret"

# 추측 단어
guesses = ''

# 기회
turns = 10

# 핵심 While Loop
# 찬스 카운트가 남아 있을 경우
while turns > 0
    # 실패 횟수
    failed = 0

    # 정답 단어 반복
    for char in word:
        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses:
            # 추측 단어 출력
            print(char, end = '')
        else:
            # 틀린 경우 대시로 처리
            print("_", end = '')
            failed += 1
        # 단어 추측이 성공 한 경우
        if failed == 0:
