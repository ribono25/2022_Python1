dic = {1:88, 2:30, 3:61, 4:55, 5:95}

for i in dic:
    ans = "불합격"
    if dic[i] >= 60:
        ans = "합격"
    
    print("%d번 학생은 %d점으로 %s입니다." % (i, dic[i], ans))
    