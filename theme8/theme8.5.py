value = int(input("Enter your value: "))

if value < 100 or value > 1000:
    print("Не подходит под условие задачи")
else:
    first = value // 100
    second = value % 100*10
    value2 = second+first
    print(value2)