# # 함수 만들기
# def hello():  # 함수 작성
#     print('하이!')
#     print('안녕!')
#     print('니 하오!')

# # hello() #함수 호출

# # 매개변수(파라미터, 인수) 있는 함 수


# def hello(name):
#     print('하이' + name)


# hello('길동')
# hello('펭수')

# # 매개변수 리턴값 있는 함수


# def add10(n):
#     return n + 10


# print(add10(10))

# 예제1) 홀수인지 짝수인지 판별하는 함수


def is_odd(n):
    if (n % 2) == 1:
        print('홀수입니다')
    else:
        print('짝수입니다')


is_odd(1)
is_odd(2)


# 예제2) 입력으로 들어오는 모든 수의 평균 값을 계산해 리턴하는 함수를 작성해보자

def avgNums(*n):  # *이 붙어 있으면 가변 매개변수임(몇 개가 들어올지는 모르겠지만 여러 개 가능)
    return sum(n) / len(n)


print(avgNums(1, 2, 3))
print(avgNums(1, 2, 3, 4, 5, 6, 7))
