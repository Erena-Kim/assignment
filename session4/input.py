# 파이썬에서 입력을 받는 함수가 있습니다~~ 구글링해서 찾아보세요!

print('문제 1. 전화번호 받기')
print('조건 1. 저장할 때는 공백 문자 없이')
print('조건 2. -, ., , 등이 들어올 때 전부 제외 하고 숫자만 저장!')
my_number = input("전화번호를 입력하세요 >> ")
number_list = ['0','1','2','3','4','5','6','7','8','9']
real_number = ""
for number in my_number:
    if number in number_list:
        real_number += number
print("내 전화 번호는 : %s" %real_number)
print("-"*30)
print('문제 2. 영어 이름 받기')
print('choi juwon 을 입력 받으면,')
print('first name : Choi, last name: Juwon 이 출력되게 만들기')
my_name = input("영어 이름을 입력하세요 >> ")
my_name = my_name.split()
first_name = my_name[0].title()
last_name = my_name[1].title()
print(f"first name : {first_name}, last name : {last_name}")