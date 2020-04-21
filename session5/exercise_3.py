def gugu_until(num):
    for i in range(1,10):
            for j in range(1,num+1):
                print("%2d * %2d = %2d" %(j, i, i*j), end="\t")
            print()

#main code
gugu_until(5)
print()
gugu_until(9)
print()
gugu_until(10)