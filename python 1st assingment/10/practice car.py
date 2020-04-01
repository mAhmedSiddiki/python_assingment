class Car:
    def __init__(self, n, m, c, y, cc):
        self.name = n
        self.color = c
        self.manufacturer = m
        self.year = y
        self.cc = cc

    def start(self):
        print("Starting the engine")


car = Car("Corolla", "Toyota", "White", 2017, 1800)
car.start()
print(car.name, car.color, car.year,car.manufacturer,car.cc)
