def maximum(a, b):
    if (a >= b):
        largest = a
    else:
        largest = b
    return largest


a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print(maximum(a, b))