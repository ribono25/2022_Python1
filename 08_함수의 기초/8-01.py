def reverse(str):
    var = ""

    for i in range(len(str)):
        var += str[len(str)-i-1]
    
    print(var)

    if var == str:
        print('입력하신 단어는 회문(Palindrome)입니다.')

inp = input()
reverse(inp)