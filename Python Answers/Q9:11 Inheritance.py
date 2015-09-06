class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
        
    def display_car(self):
        return "This is a " + self.color + " " + self.model + " with " + str(self.mpg) + " MPG."
    
    def drive_car(self):
        self.condition = "used"

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.battery_type = battery_type
        self.model = model
        self.color = color
        self.mpg = mpg
        

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")