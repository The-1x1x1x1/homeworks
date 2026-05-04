class Ferrari:
    def fuel_type(self):
        print("petrol")
    def max_speed(self):
        print("max speed 350")

class BMW:
    def fuel_type(self):
        print("diesel")
    def max_speed(self):
        print("max speed 240")


ferrari=Ferrari()
bmw=BMW()
for car in (ferrari,bmw):
    car.fuel_type()
    car.max_speed()