var = int(input())
ans = [0,0,0,0,0,0,0,0,0,0]

while var > 0:
    n = var % 10
    ans[n] += 1

    var //= 10

print(' '.join(map(str, [i for i in range(10)])))
print(' '.join(map(str, ans)))