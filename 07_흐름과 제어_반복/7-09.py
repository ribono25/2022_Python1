n = 4

while n > 0:
    i = 2*n - 1
    st = ""
    
    while i > 0:
        st += '*'
        i -= 1
    print("{0:^7}".format(st))

    n -= 1