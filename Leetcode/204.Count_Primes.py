num = 4

for j in range(2, num):
    print(j)
    for i in range(2,j):
        if (j % i) == 0:
            print(j,"不是质数")
            # print(i,"乘于",j//i,"是",j)
            break
        else:
            print(j,"是质数")
            break