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
