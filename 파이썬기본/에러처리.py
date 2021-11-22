# try / except

def div10(n):  # 입력값에 10을 나눠서 리턴
    try:
        return 10/n
    except ZeroDivisionError:
        print('에러: 0으로 나눌 수 없음')


print(div10(2))
print(div10(0))  # 0으로 나눌 수 없다
print(div10(5))
