attend = {1:'John',2:'Tom',3:'Paul',4:'Sam'}

while True:
    x = int(input())
    if x > 5 :
        print('Vacancy')
        break
    else :
        print(attend[x])