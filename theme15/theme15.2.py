def Sign(X):
    if X < 0:
        return -1
    elif X == 0:
        return 0
    else:
        return 1
a = float(input('Enter A: '))
b = float(input('Enter B: '))
print(Sign(a)+Sign(b))
