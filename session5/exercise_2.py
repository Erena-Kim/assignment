#2-a
def even_gugu():
    for i in range(1,10):
            for j in range(2,10,2):
                print("%2d * %2d = %2d" %(j, i, i*j), end="\t")
            print()

def odd_gugu():
    for i in range(1,10):
            for j in range(1,10,2):
                print("%2d * %2d = %2d" %(j, i, i*j), end="\t")
            print()

def gugudan_odd_or_even(num):
    if num == 1:
        odd_gugu()
    elif num == 2:
        even_gugu()
    else:
        print("잘못된 인자를 입력하셨습니다.")

#main code
gugudan_odd_or_even(3)
print()
gugudan_odd_or_even(1)
print()
gugudan_odd_or_even(2)
print("-"*60)

#2-b
def gugudan_num(num):
    for i in range(1, 10):
        for j in range(num, 10, 2):
            print("%2d * %2d = %2d" %(j, i, i*j), end="\t")
        print()

def gugudan_odd_or_even_2(num):
    if num % 2 == 0:
        gugudan_num(2)
    else:
        gugudan_num(1)

#main code
gugudan_odd_or_even_2(31)
print()
gugudan_odd_or_even_2(14)
print("-"*60)