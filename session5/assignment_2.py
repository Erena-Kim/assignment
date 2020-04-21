#클래스 변수로 지정
class FourCal:
    add_num = 0
    sub_num = 0
    mult_num = 0
    div_num = 0

    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def add(self, n1, n2):
        FourCal.add_num += 1
        result = n1 + n2
        return result

    def subtract(self, n1, n2):
        FourCal.sub_num += 1
        result = n1 - n2
        return result

    def multiply(self, n1, n2):
        FourCal.mult_num += 1
        result = n1 * n2
        return result

    def divide(self, n1, n2):
        if n2 == 0:
            return "0으로 나눌 수 없습니다."
        FourCal.div_num += 1
        result = n1 / n2
        return result
    
    def showcount():
        print("덧셈 : %2d" %FourCal.add_num)
        print("뺄셈 : %2d" %FourCal.sub_num)
        print("곱셈 : %2d" %FourCal.mult_num)
        print("나눗셈 : %2d" %FourCal.div_num)

#main code
calculator1 = FourCal("영현", 22, "고려대")
print(calculator1.name, calculator1.age)
print(calculator1.add(3,4))
print(calculator1.subtract(6,2))
print(calculator1.multiply(2,19))
print(calculator1.multiply(3,2))
print(calculator1.divide(7, 0))
print()
calculator2 = FourCal("영교", 17, "광동고")
print(calculator2.name, calculator2.age)
print(calculator2.add(2,1))
print(calculator2.subtract(3,1))
print(calculator2.multiply(4,5))
print()
FourCal.showcount()
print()