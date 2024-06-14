while True:
    a,b,c = map(str,input().split())
    if c == 'c':
        break
    a,b = int(a),int(b)
    print(a*b)