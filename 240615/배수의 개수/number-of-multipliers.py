cnt_3,cnt_5 = 0,0
for i in range (10):
    x = int(input())
    if x%3 == 0:
        cnt_3 += 1
    if x%5 == 0:
        cnt_5 += 1
print(cnt_3,cnt_5)