var = int(input())
ans = []

while var > 0:
    ans += [var % 2]
    var //= 2

i = 0
while i < len(ans):
    print("%d" % ans[len(ans) - i - 1], end="")
    i += 1