def sum_of_multiples(limit):
    l = []
    limit += 1
    for i in range(limit):
        if (i % 3 == 0 or i % 5 == 0):
            l.append(i)
    return l


print(sum_of_multiples(int(input("Enter a number: "))))
