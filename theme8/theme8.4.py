value = int(input("Enter the value: "))

if value < 10 or value > 100:
    print("Не подходит под условие задачи")
else:
    first = value // 10
    second = value % 10*10
    value2 = second+first
    print(value2)