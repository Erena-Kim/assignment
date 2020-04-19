'''
과제 1. 별찍기 (4월 20일까지)
- 아래와 같이 * 을 출력 하는 프로그램을 만들어보세요
**********
*********
********
*******
*****
****
***
**
*

과제 2. 구구단 (4월 20일까지)
- 구구단 2단을 출력해보세요!

과제 3. while 문을 활용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보세요. (4월 20일까지)

과제 4. for 문을 활용하여 멋사 학생들의 평균 점수를 구해보세요. (4월 20일까지)
- mutsa_scores = [90, 77, 40, 55, 90, 100, 88]

과제 5. input.py 문제 2개 풀기 (4월 20일까지)

과제 6. HTML / CSS 페이스북 모바일 클론코딩 (4월 27일까지)
- 이미지 자율
- 까먹기전에 해주세요~

'''
# 과제 1
print("과제 1")
for i in range(10,0,-1):
    print("*"*i)
print("-"*30)

# 과제 2
print("과제 2")
for i in range(1,10):
    print("2 x %2d = %2d" %(i, 2*i))
print("-"*30)

# 과제 3
print("과제 3")
i = 1
hap = 0
while i < 1001:
    if i % 3 == 0:
        hap += i
    i += 1
print("1부터 1000까지 자연수 중 3의 배수 합은 : %d" %hap)
print("-"*30)

# 과제 4
print("과제 4")
mutsa_scores = [90, 77, 40, 55, 90, 100, 88]
sum_mutsa_scores = 0
for i in mutsa_scores:
    sum_mutsa_scores += i
mean_mutsa_scores = sum_mutsa_scores / len(mutsa_scores)
print("멋사 학생들의 평균 점수는 : %d" %mean_mutsa_scores)