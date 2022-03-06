str1, str2 = map(str, input().split(', '))

def islonger():
    global str1
    global str2

    len1 = len(str1)
    len2 = len(str2)

    ans = str1 if len1 > len2 else str2

    print('%s' % ans)

islonger()