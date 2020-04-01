a = input()
length = len(a)

up = ""
low = ""
num = ""
oth = ""

for i in range(0,length):
    if a[i].isupper():
        up = up + a[i]
    elif a[i].islower():
        low = low + a[i]
    elif a[i].isnumeric():
        num = num + a[i]
    else:
        oth = oth + a[i]

print(up)
print(low)
print(num)
print(oth)