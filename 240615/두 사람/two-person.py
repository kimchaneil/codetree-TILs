a_1,s_1 = map(str,input().split())
a_2,s_2 = map(str,input().split())
a_1 = int(a_1)
a_2 = int(a_2)

if (a_1 >= 19 and s_1 == 'M') or (a_2 >= 19 and s_2 == 'M') :
    print('1')
else:
    print('0')