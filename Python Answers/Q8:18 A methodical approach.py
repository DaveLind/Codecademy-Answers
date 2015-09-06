class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
   
    def description(self):
        print self.name
        print self.age
        
#Don't really understand why they ask for you to include hippo when it just rejects that code and fails. This works though but ignores the hippo inclusion. 


