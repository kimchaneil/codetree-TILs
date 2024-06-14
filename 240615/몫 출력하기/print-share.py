cnt = 0
while cnt != 3:
    x = int(input())
    if x%2 == 0 :
        x //= 2
        print(x)
        cnt += 1