ch = input()
ASCII_ch = ord(ch)

ans = "소문자"
if 65 <= ASCII_ch<= 90:
    ans = "대문자"

print("%s 는 %s 입니다." % (ch, ans))