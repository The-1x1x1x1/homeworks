class vehicle:
    def __init__(self,fareprice,seating):
        self.fareprice=fareprice
        self.seating=seating
    def calculate(self):
        return self.fareprice+self.seating

class bus(vehicle):
    def __init__(self, fareprice, seating, maintenance = 0.10):
        super().__init__(fareprice, seating)
        self.maintenance=maintenance
    def fullfare(self):
        fr=self.calculate()
        return fr + (fr*self.maintenance)
    
busfare=bus(50,100)
print("total bus fare: ",busfare.fullfare())