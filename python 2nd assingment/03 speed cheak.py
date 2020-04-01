def speed_of_driver(speed):
    if speed <= 70:
        print("OK")
    else:
        speed_check = (speed-70)//5
        if speed_check <= 12:
            print("point: ", speed_check)
        else:
            print("License suspended")


speed_of_driver(int(input("Enter driver speed: ")))