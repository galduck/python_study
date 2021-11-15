print('안녕하세요') 
print('이름이 무엇인가요?') #이름 묻기
myName=input() #입력 받기
print('만나서 반갑습니다' + myName)
print('당신의 이름의 길이는?: ')
print(len(myName)) # Len 문자열의 길이
print('당신의 나이는? ') #나이 묻기
myAge=input()
print('당신은 내년에 ' + str(int(myAge) + 1) + '살 입니다.') 
#파이썬에서 문자열 + 숫자는 에러가 남으로 숫자를 str(숫자)로 변경해서 더한다
