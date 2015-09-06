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

my_car = Car("DeLorean", "silver", 88)

print my_car.condition

#Here we print the new condition of the car

my_car.drive_car()

#here we call the function to drive the car, thus "using it"

print my_car.condition

#here we print the new condition of the car, "used", after we drove it