n = int(input())
cnt = 0
for i in range (2,n,1):
    if n%i == 0:
        cnt =1
if cnt == 0 :
    print('N')
else:
    print('C')