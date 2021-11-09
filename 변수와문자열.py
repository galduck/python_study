'''
# 여러개의 변수를 동시에 초기화
# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)

#예제 3
x, y, z = 1, 2, 3
print(x, y, z) # 출력시 변수 여러 개 가능


#예제4
x = 5
y = 3.33
z = "호피폴라"
print(type(x))
print(type(y))
print(type(z))

#5
a= input("a: ")
b= input("b: ")

a, b = b, a
print("a: " + a)
print("b: " + b)

'''


# 문자열
# 긴 문자열은 따옴표 3개(''', """)
var3 = '''
'따옴표' 3개는
끝나는 "문장:까지 모두를 문자열로 처리
---------------------!
'''

print(var3)

'''
# 문자열(+) 연산
성='홍'
이름='길동'
name = 성+ ' ' + 이름

print(name)

# 타입변환 : str(), int(), float()

print(type(int(str(100))))

'''
# 예제1 
str1 = '\tIt\'s a "kind of" sunny\n Have a nice Day!'
print(str1)

# 예제2
str2 = ''' 다스베이더가 말했다 \n "내가 니 애비다" \n 그 말을 들은 루크는 '깜짝'놀랐다. '''
print(str2)

city=input('태어난 도시가 어디인가요 ? \n')
petName = input('애완 동물의 이름은? \n')
print('당신의 밴드이름은 ' + city + ' ' + petName)