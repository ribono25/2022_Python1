data = [1, 2, '4', 3]
sum = 1

def mul(*li):
    global sum

    for i in li:
        if type(i) is not int:
            return False
        sum *= i
    return True

if mul(*data) == True:
    print(sum)
else:
    print("에러발생")