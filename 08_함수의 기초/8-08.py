var = list(map(int, input().split(', ')))

def square(li):
    for i in li:
        print('square(%d) => %d' % (i, i**2))

square(var)