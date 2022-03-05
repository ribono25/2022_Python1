data = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sum = 0

while len(data) > 0:
    num = data.pop()

    if num >= 80:
        sum += num

print(sum) 