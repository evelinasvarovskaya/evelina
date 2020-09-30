a = int(input())
b = int(input())
c = int(input())
s_rectangle = a*b
s_square = c*c
first  = s_rectangle // s_square
second = s_rectangle % s_square
print("In rectangular", first, "square")
print("Free space in the rectangle: ", second)