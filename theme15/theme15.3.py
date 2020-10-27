def RingS(R1, R2):
    return 3.14*(R1*R1 - R2*R2)
for i in range(3):
    a = float(input('Enter R1: '))
    b = float(input('Enter R2: '))
    print('Площадь кольца ',RingS(a, b))