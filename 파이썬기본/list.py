# 리스트는 순서가 있고 수정 가능한 자료구조이다. 값이 중복 가능

# 리터럴로 만들기
numbers = [1, 2, 3, 4, 5, ]
fruits = ['사과', '오렌지', '포도', '배']

# 값을 가져 오기
print(numbers[0])  # 1
print(fruits[0])  # 사과

# 길이(갯수)
print(len(numbers))
print(len(fruits))

# 추가하기 append
fruits.append('망고')  # 리스트의 맨 끝에 추가됨
print(fruits)

# 제거하기 remove
fruits.remove('포도')  # 아이템 값으로 제거
print(fruits)

# 인덱스로 특정 위치에 입력
fruits.insert(2, '딸기')
print(fruits)

# 특정 인덱스의 값을 제거하고 리턴(인덱스 값이 없으면 맨 끝의 인덱스를 제거)
print(fruits.pop(3))
print(fruits)

# 리스트를 거꾸로 리버스 (리스트의 순서를 바꿔서 저장)
fruits.reverse()
print(fruits)

# 정렬 리스트 (값의 순서대로 정렬)
fruits.sort()
print(fruits)
