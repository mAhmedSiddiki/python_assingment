def namta(n=1):
    m = 1
    while m <= 10:
        print(n, "x", m, "=", n * m)
        m += 1


number = int(input("Please enter a positive integer: "))
namta(number)
namta()