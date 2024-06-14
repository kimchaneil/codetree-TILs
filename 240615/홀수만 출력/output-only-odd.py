a,b = map(int,input().split())

if a<b:
    for i in range (a,b+1,2):
        print(i, end=' ')
else:
    for i in range (b,a+1,2):
        print(i,end=' ')