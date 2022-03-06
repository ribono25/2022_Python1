data = list(range(1, 11))
ans = list(map(lambda x:x ** 2, list(filter(lambda x:x % 2 == 0, data))))
print(ans)