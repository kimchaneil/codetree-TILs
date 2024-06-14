cnt = 0
a = int(input())
while True:
    if a == 1 :
        break
    elif a%2 == 0:
        a //= 2
        cnt += 1
    else:
        a = (a*3+1)
        cnt += 1
print(cnt)