data = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
ans_list = [0,0,0,0] # A,B,O,AB
for i in data:
    if i == 'A': ans_list[0] += 1
    elif i == 'B': ans_list[1] += 1
    elif i == 'O' : ans_list[2] += 1
    else : ans_list[3] += 1

print("{'A': %d, 'O': %d, 'B': %d, 'AB': %d}" % (ans_list[0], ans_list[2], ans_list[1], ans_list[3]))
