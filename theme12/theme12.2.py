c = input("Enter the symbol: ")
n = int(input("Enter the N: "))
if c =='С':
    if n == 0:
        print("direction north")
    elif n == -1:
        print('direction west')
    elif n == 1:
        print('direction еast')
if c == 'З':
    if n == 0:
        print("direction east")
    elif n == 1:
        print('direction south')
    elif n == -1:
        print('direction north')
if c == 'Ю':
    if n == 0:
        print("direction south")
    elif n == -1:
        print('direction еast')
    elif n == 1:
        print('direction west')
if c == 'В':
    if n == 0:
        print("direction west")
    elif n == 1:
        print('direction north')
    elif n == -1:
        print('direction south')