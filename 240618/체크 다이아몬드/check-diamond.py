n = int(input())

for i in range(1,n+1,1):
    count = 0
    print(' '*(n-i),end='')
    while count != (i-1):
        print('* ',end='')
        count += 1
    print('*')
for j in range(n-1,0,-1):
    count=0
    print(' '*(n-j),end='')
    while count != (j-1):
        print('* ',end='')
        count += 1
    print('*')