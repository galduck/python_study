coffee = 10  # 커피수량 10ro

while True:  # 무한 반복
    print(f"남은 커피의 양은 {coffee}개 입니다.")
    money = int(input("커피 한 잔에 300원입니다. 돈을 넣어주세요: "))
    # 입금한 돈이 300원일 때, 더 클 때, 작을 경우에 따라서 if elif else
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300:
        print(f"거스름 돈 {money-300}원을 주고 커피를 줍니다.")
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려 주고 커피를 주지 않습니다.")

    if coffee == 0:
        print("커피가 다 떨어졌스빈다. 판매를 중지합니다.")
        break
