li = []    
var = int(input())

def fibo(n):
    if n == 1 or n == 2:
        return 1
    
    return fibo(n-1) + fibo(n-2)

def fibo_list(k):
    global li

    for i in range(1,k+1):
        li += [fibo(i)]

fibo_list(var)

print('[', end='')
print(', '.join(map(str, li)), end=']')