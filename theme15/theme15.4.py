def Quarter(x, y) :
    if x>0 and y>0:
        return 1
    elif x<0 and y>0:
        return 2
    elif x<0 and y<0:
        return 3
    elif x<0 and y<0:
        return 4
for i in range(3):
    a = float(input('Enter x: '))
    b = float(input('Enter y: '))
    print('Номер координатной четверти ', Quarter(a, b))