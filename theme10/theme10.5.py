value = int(input("Enter the value: "))
r4 = value%10
r1 = value//1000
r3 = value//10%10
r2 = value//100%10
if r1==r4 and r2==r3:
    print("Данное число читается одинаково слева направо и справа налево")
else:
    print("Данное число НЕ читается одинаково слева направо и справа налево")