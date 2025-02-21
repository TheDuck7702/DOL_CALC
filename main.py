from math import sqrt

print("~"*40)
print("welcome to the Distance Of A Line Calc")
print("~"*40)
print()

print("*"*10)
print("1) give the promted infomation")
print("2) receive your value of the distance of a line!!")
print()

yn = "y"

while yn == "y":

    X1 = float(input("what is the first x value: "))
    X2 = float(input("what is the second x value: "))
    Y1 = float(input("what is the first y value: "))
    Y2 = float(input("what is the second y value: "))

    sq = X2 - X1 
    rt = Y2 - Y1
    ft = sq**2 + rt**2
    gt = sqrt(ft)
    GT = round(gt, 3)
    print(f"The lenght of the 2 points is {GT}")
    print()

    yn = input("do you want to do it again??? (y/n): ")
    print()