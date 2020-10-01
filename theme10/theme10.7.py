a = int(input("Enter the A: "))
b = int(input("Enter the B: "))
c = int(input("Enter the C: "))
if a < b+c and b < a+c and c < a+b:
    print('Существует треугольник со сторонами a, b, c')
else:
    print('Не существует треугольниа со сторонами a, b, c')