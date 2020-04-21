#인스턴스 변수로 지정
class FourCal:

    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

        self.add_num = 0
        self.sub_num = 0
        self.mult_num = 0
        self.div_num = 0

    def add(self, n1, n2):
        self.add_num += 1
        result = n1 + n2
        return result

    def subtract(self, n1, n2):
        self.sub_num += 1
        result = n1 - n2
        return result

    def multiply(self, n1, n2):
        self.mult_num += 1
        result = n1 * n2
        return result

    def divide(self, n1, n2):
        if n2 == 0:
            return "0으로 나눌 수 없습니다."
        self.div_num += 1
        result = n1 / n2
        return result
    
    def showcount(self):
        print("덧셈 : %2d" %self.add_num)
        print("뺄셈 : %2d" %self.sub_num)
        print("곱셈 : %2d" %self.mult_num)
        print("나눗셈 : %2d" %self.div_num)

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
calculator1.showcount()
print()
calculator2.showcount()