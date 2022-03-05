list1 = ["가위", "바위", "보"]

ans1 = input() #Man1
ans2 = input() #Man2

if ans1 == list1[0] :
    if ans2 == list1[0] : ans = "Draw"
    elif ans2 == list1[1] : ans = "Man2 Win!"
    else : ans = "Man1 Win!"
elif ans1 == list1[1] :
    if ans2 == list1[0] : ans = "Man1 Win!"
    elif ans2 == list1[1] : ans = "Draw"
    else : ans = "Man2 Win!"
else :
    if ans2 == list1[0] : ans = "Man2 Win!"
    elif ans2 == list1[1] : ans = "Man1 Win!"
    else : ans = "Draw"

print("Result : %s" % ans)