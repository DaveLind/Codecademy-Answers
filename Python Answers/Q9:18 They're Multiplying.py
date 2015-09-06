class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def description(self):
        print self.name
        print self.age
        
hippo = Animal("Xenye", 76)
hippo.description
sloth = Animal ("Sally", 89)
ocelot = Animal ("Portia", 32)

print sloth.health
print hippo.health
print ocelot.health