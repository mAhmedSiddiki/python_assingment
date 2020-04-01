def prime_number(limit):
    num = 0
    while (num <= limit):
        count = 0
        i = 2
        while (i <= num // 2):
            if (num % i == 0):
                count = count + 1
                break
            i = i + 1
        if (count == 0 and num != 1):
            print(" %d" % num, end='  ')
        num = num + 1


prime_number(int(input("Enter a number: ")))