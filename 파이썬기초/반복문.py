# while 반복문
# while True:
#   print("무한반복")

# 횟수가 정해진 while 반복문
# count = 0
# while count < 3:
#     print('횟수: ', count)
#     count += 1

# name = ' '
# while name != '펭수':  # name이 펭수가 되면 종료됨
#     name = input('펭수를 입력해 주세요 : ')

# print("thank you")


# hit = 0
# while hit < 10:
#     hit += 1
#     print(f'나무를 {hit}번 찍었습니다.')
#     if hit == 10:
#         print("나무가 넘어갔습니다.")


# hit = 0
# while hit < 10:
#     hit += 1
#     if hit % 2 == 0:  # hit가 짝수이면 아래 코드는 실행하지 않고 다시 조건으로
#         continue
#     print(f'나무를 {hit}번 찍었습니다.')
#     if hit == 10:
#         print("나무가 넘어갔습니다.")

# hit = 0
# while hit < 10:
#     hit += 1
#     if hit % 2 == 0:  # hit가 짝수이면 아래 코드는 실행하지 않고 다시 조건으로
#         continue
#     print(f'나무를 {hit}번 찍었습니다.')
#     if hit == 5:
#         break

# # for 반복문
# for n in [1, 2, 3]:
#     print(n)

# # []는 파이썬 리스트 타입, 반복문 for는 이 리스트 안의 내용을 한 번씩 반복
# # 대괄호[] 가 있으면 타입이 '리스트'가 됨
# for s in ['다람쥐', '펭귄', '하이에나']:
#     print(s)

# # 문자열도 리스트처럼 처리되서 첫번재 두번째 세번째 음절이 하나씩 c 안으로 들어가 반복됨
# for c in '홍길동님':  # 문자열의 음절을 반복
#     print(c)

# # for 반복문과 자주쓰는 함수 range(시작, 끝) 리턴 값은 시작 ~ 끝 -1
# for n in range(3):  # 0부터 3-1
#     print(n)

# # 1에서 100까지의 합은
# total = 0
# for x in range(1, 101):
#     total += x

# print("1에서 100까지 더한 값: ", total)

# # 구구단 2단
# for i in range(1, 10):
#     print(f'2 X {i} = {2 * i}')

# 전체 구구단 반복문
# 예제) for문을 중첩하여 2단부터 9단까지 가로로 한줄씩 만드시오

# 내가 제출한 답
for i in range(1, 10):
    print(f'2 X {i} = {2 * i}')
    print(f'3 X {i} = {3 * i}')
    print(f'4 X {i} = {4 * i}')
    print(f'5 X {i} = {5 * i}')
    print(f'6 X {i} = {6 * i}')
    print(f'7 X {i} = {7 * i}')
    print(f'8 X {i} = {8 * i}')
    print(f'9 X {i} = {9 * i}')

# 선생님 답
# 세로로
for i in range(2, 10):  # 2단부터 9단 까지
    for j in range(1, 10):  # 1~9
        print(f'{i} X {j} = {i * j}')

# 가로로
for i in range(2, 10):  # 2단부터 9단 까지
    print()
    for j in range(1, 10):  # 1~9
        print(f'{i} X {j} = {i * j}', end=" ")
