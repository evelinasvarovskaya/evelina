a = int(input("Enter the value of 1st step: "))
b = int(input("Enter the value of 2nd step: "))
if a < b:
    print("There are no 2nd steps in 1st step")
else:
    result = a % b
    print("There are", result, "points left of 1st step")