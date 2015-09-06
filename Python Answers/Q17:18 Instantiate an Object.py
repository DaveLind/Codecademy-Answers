class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    
    number_of_sides = 3
    def check_angles(self):
        if (self.angle1 + self.angle2 +self.angle3) ==180:
            return True
        else:
            return False

#important to note is that the following 3 lines must not be indented and must be left-most, out of any defs.
    
my_triangle = Triangle(90, 60, 30)
print my_triangle.number_of_sides
print my_triangle.check_angles()