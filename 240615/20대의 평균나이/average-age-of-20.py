hap, count = 0, 0

while True:
    age = int(input())

    if age >= 30 or  age <= 19:
        break

    hap += age
    count += 1

print(f'{hap / count:.2f}')