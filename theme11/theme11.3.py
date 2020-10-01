a = int(input('Enter A: '))
b = int(input('Enter B: '))
c = int(input('Enter C: '))
ab = abs(b-a)
ac = abs(c-a)
if ab<ac:
    print('Point B is closer to A. Distance from A to B is', ab)
elif ab>ac:
    print('Point C is closer to A. Distance from A to C is', ac)
else:
    print('Distance AB == Distance AC')
