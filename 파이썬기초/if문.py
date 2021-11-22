# # if문 문법
# if True:
#     print("조건이 참이면 실행")
#     print("실행코드는 띄어쓰기로 구분")
#     # if문의 코드 블록은 띄어쓰기 된 곳까지

# print("종료")

# if False:
#     # False면 실행 안 됨
#     print("조건이 참이면 실행")
#     print("실행코드는 띄어쓰기로 구분")
#     # if문의 코드 블록은 띄어쓰기 된 곳까지

# print("종료")

# a, b = 1, 10
# # a에 1이 들어가고 b에 10이 들어감
# if a > b:
#     # False라서 실행 안 됨
#     print("조건이 참이면 실행")
#     print("실행코드는 띄어쓰기로 구분")
#     # if문의 코드 블록은 띄어쓰기 된 곳까지
# elif a == b:
#     print("a b가 같다")
# else:  # if문의 조건이 거짓이면 코드 실행
#     print("if의 조건이 거짓일 때 실행")

# print("종료")


# 예제 1
number = int(input("숫자를 입력: \n"))
if ((number % 2) == 0):
    print("짝수 입니다.")
else:
    print("홀수 입니다.")

# 예제 2
height = int(input("당신의 키는 몇cm입니까?: \n"))
if height > 120:
    print("청룔열차를 타실 수 있습니다. ")
    age = int(input("당신의 나이는 ?: \n "))
    # 입력받은 나이에 따라서 요금을 출력한다. if elif else문 사용
    if age < 12:  # 12살 미만
        print("요금은 $5입니다.")
    elif age <= 16:  # 12살 이상 16살 이하
        print("요금은 $7입니다.")
    else:  # 17살 이상
        print("요금은 $12입니다.")
else:
    print("청룔열차를 타실 수 없습니다. ")
