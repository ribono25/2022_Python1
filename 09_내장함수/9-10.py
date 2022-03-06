data = [3,5,4,1,8,10,2]

def whatmax(*li):
    return max(li)

print('max(', end='')
print(', '.join(map(str, data)), end=') => ')
print(whatmax(*data))