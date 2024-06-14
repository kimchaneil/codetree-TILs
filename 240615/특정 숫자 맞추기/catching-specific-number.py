answer = 25
while True:
    x= int(input())
    if x==answer:
        print('Good')
        break
    elif x > answer :
        print('Lower')
    elif x < answer :
        print('Higher')