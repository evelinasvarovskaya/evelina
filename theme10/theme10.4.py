value = int(input("Enter the value: "))
last = value%10
first = value//100
seconds = value//10%10
if first>seconds>last or first<seconds<last:
    print("Цифры данного числа образуют возрастающую или убывающую последовательность")
else:
    print("Цифры данного числа НЕ образуют возрастающую или убывающую последовательность")