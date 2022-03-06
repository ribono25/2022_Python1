def GBB(var1, var2):
    list = ["가위", "바위", "보"]
    x, y = list.index(var1), list.index(var2)

    if x == y:
        print("비겼습니다!")
    elif (x - y == 1) or (y - x == 2): 
        print("%s가 이겼습니다!" % var1)
    elif (x - y == 2) or (y - x == 1): 
        print("%s가 이겼습니다!" % var2)

n1 = input()
n2 = input()
a1 = input()
a2 = input()

GBB(a1, a2)