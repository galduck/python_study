# 딕셔너리는 키와 값의 쌍으로 만들어지고 순서가 없으며 수정 가능한 자료 구로로 중복이 안 됨

# 리터럴 생성
person = {
    'name': '펭수',
    'age': 30
}

# 값에 접근 방법
print(person['name'])
print(person.get('name'))  # 키값이없더라도 에러가 나지 않고 리턴 None

# 키, 값을 추가하기
person['phone'] = '010-777-7777'
print(person)


# 값을 수정하기
person['name'] = '길동'
print(person)

# 아이템 제거(키 값과 해당하는 값이 같이 제거됨)
person.pop('phone')
print(person)
