import random

names_string = input("내기를 할 친구들의 이름을 적습니다. 콤마(,)로 분리해서 적습니다. \n")
names = names_string.split(",")

# print(names)

n = random.randint(0, len(names))
print(f"오늘 커피는 {names[n]}가 쏩니다")
