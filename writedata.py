f = open("C:\python\새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.wirte(data)
f.close()
