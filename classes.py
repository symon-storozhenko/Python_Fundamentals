class MyCar:
    wheels = 4

    def my_car_details(self):
        print("Hello, I'm your new car")


my_car = MyCar()
my_car.my_car_details()
print(my_car.wheels)


class MyFirstCar(MyCar):
    def __init__(self):
        self.brand = "VW"

    def my_car_details(self):
        print(f'Hello, {self.brand}')

vw = MyFirstCar()
vw.my_car_details()