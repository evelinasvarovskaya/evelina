value = int(input("Enter value in range 1-999: "))
if value%2==0:
    ost = 'Четное'
elif value%2 != 0:
    ost = 'Нечетное'
if value<10:
    pl = 'однозначное'
elif value>9 and value<100:
    pl = 'двузначное'
elif value>99:
    pl = 'трехзначное'
print(ost,pl, 'число.')