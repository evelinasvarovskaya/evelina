value = int(input("Enter the value: "))

if 10<=value and value<20:
    if value == 10:
        print('десять ')
    if value == 11:
        print('одиннадцать')
    if value == 12:
        print('двенадцать')
    if value == 13:
        print('тринадцать')
    if value == 14:
        print('четырнадцать')
    if value == 15:
        print('пятнадцать')
    if value == 16:
        print('шестнадцать')
    if value == 17:
        print('семнадцать')
    if value == 18:
        print('восемнадцать')
    if value == 19:
        print('девятнадцать')
    print('учебных заданий')
if value>=20:
    if value//10 == 2:
        print('двадцать')
    if value//10 == 3:
        print('тридцать')
    if value//10 == 4:
        print('сорок')
    if value&10 == 1:
        print('одно')
    if value%10 == 2:
        print('два')
    if value%10 == 3:
        print('три')
    if value%10 == 4:
        print('четыре')
    if value%10 == 5:
        print('пять')
    if value%10 == 6:
        print('шесть')
    if value%10 == 7:
        print('семь')
    if value%10 == 8:
        print('восемь')
    if value%10 == 9:
        print('девять')
    if value%10 == 1:
        print('учебное задание')
    elif value%10 == 2 or value%10 == 3 or value%10 == 4:
        print('учебных задания')
    else:
        print('учебных заданий')
