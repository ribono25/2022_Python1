li, e = [1,2,3,4,3,2,1], []

for i in range(10):
    e += [0]

def same_remove():
    ans_li = []

    for n in li:
        e[n] += 1
        
        if e[n] == 1:
            ans_li += [n]

    return ans_li

print(li)
print(same_remove())