def showNumbers(limit):
    for i in range(limit+1):
        if i%2==0:
            print(i," Even")
        else:
            print(i," Odd")


showNumbers(int(input("Enter a number: ")))