def find_number(li, number):
    ans = 'False'

    for i in li:
        if i == number: ans = 'True'
    
    print('%d => %s' % (number, ans))

input_list = [2, 4, 6, 8, 10]
print(input_list)
find_number(input_list,5)
find_number(input_list,10)