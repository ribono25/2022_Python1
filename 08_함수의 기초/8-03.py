import math

def ispn(var):
    if var == 1: print("소수가 아닙니다.")
    elif var == 2: print("소수입니다.")
    else:
        if var % 2 == 0: print("소수가 아닙니다.")
        else:
            cnt = 0
            for i in range(2, int(math.sqrt(var)+1)):
                
                if var % i == 0:
                    cnt += 1
            if cnt == 0:
                print("소수입니다.")
            else:
                print("소수가 아닙니다.")

a = int(input())
ispn(a)