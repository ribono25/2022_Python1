var = input()
ans = var

if 65 <= ord(var) <= 90 : #대문자
    ans = var.lower()
    print("%s(ASCII: %d) => %s(ASCII: %d)" % (var, ord(var), ans, ord(ans)))
elif 97 <= ord(var) <= 122 : #소문자
    ans = var.upper()
    print("%s(ASCII: %d) => %s(ASCII: %d)" % (var, ord(var), ans, ord(ans)))
else:
    print(var)