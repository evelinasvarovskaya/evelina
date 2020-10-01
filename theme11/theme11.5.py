value = int(input('Enter the value: '))
if value ==0:
    print('нулевое число')
else:
    if value<0:
        pl = 'Отрицательное'
    elif value>0:
        pl = 'Положительное'
    if value%2==0:
        ost = 'четное'
    elif value%2!=0:
        ost = 'нечетное'
    print(pl, ost, 'число.')
