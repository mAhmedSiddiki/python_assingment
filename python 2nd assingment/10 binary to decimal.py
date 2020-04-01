def binary_to_decimal(list):
    decimal = 0

    for i in range(0,len(list)):
        if i==0 and list[i] == 1:
            decimal = decimal + 128
        elif i==1 and list[i] == 1:
            decimal = decimal + 64
        elif i==2 and list[i] == 1:
            decimal = decimal + 32
        elif i==3 and list[i] == 1:
            decimal = decimal + 16
        elif i==4 and list[i] == 1:
            decimal = decimal + 8
        elif i==5 and list[i] == 1:
            decimal = decimal + 4
        elif i==6 and list[i] == 1:
            decimal = decimal + 2
        elif i==7 and list[i] == 1:
            decimal = decimal + 1
    return decimal


print(binary_to_decimal([1, 1, 1, 1, 1, 1, 1, 1]))