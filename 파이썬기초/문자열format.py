# 1. f -string
from types import WrapperDescriptorType


name = '홍길동'
age = 20
print(f'안녕하세요 {name}님 나이가 {age}살 이시군요')

# 2. 문자열.format()
number = 20
welcome = '환영합니다'
base = '{}번 손님 {}'

print('{}번 손님 {}'.format(number, welcome))


#예제 1
name = '김펭수'
color = '핑크'
print('안녕하세요 제 이름은 {}이고 좋아하는 색상은 {}입니다' .format(name,color))
print(f'안녕하세요 제이름은 {name}이고 좋아하는 색상은 {color}입니다.')

# 문자열 인덱스 : 문자열은 인덱스 번호를 사용가능
string1 = "abcdefg"
print(string1[2]) #c
print(string1[1:5]) #bcde
print(string1[:3])
print(string1[3:])

#슬라이싱[시작 인덱스 : 끝 인덱스],[ : : 증감]
print(string1[::-1]) #끝에서부터 시작이 됨 (뒤에서 처음까지)

#인덱스 번호로 값을 가져오는 것은 가능하지만 수정 불가
#만들어진 문자열은 수정이 불가능
# string1[0] = 'k' #에러나타남 (값을 바꿀 수 없어서)

#예제 1
#2자리 숫자를 입력한다.
#입력된 2자리 숫자를 쪼개서 하나씩 더해 출력한다
two_digit_number = input("두 자리 숫자를 입력: \n")

x = two_digit_number[0]
y = two_digit_number[1]
z = int(x) + int(y)
print(f'{x}+{y} ={z}')

#예제2
height = input("키를 미터 단위로 입력하세요: ")
weight = input("몸무게를 킬로 단위로 입력하세요: ")

BMI = float(weight) / float(height) **2
print(f'당신의 bmi는 {round(BMI,2)}입니다')