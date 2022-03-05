for i in range(200, 300, 2):
    first = i // 100
    second = i // 10 - (i // 100) * 10
    third = i % 10

    if first%2==0 and second%2==0 and third%2==0:
        if i == 288: print(i)
        else:
            print(i, end=",")