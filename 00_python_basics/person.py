class person:
    def __init__(self, age, name):
        self.name = name
        self.age = self.validate_age(age)
        
    def validate_age(self, age):
        if self.age > 0 and self.age < 100:
            self.age = age
        else:
            self.age = 0
        return self.age
    
    def get_age(self):
        return self.age
    
p1 = person(10,"Wayne")
print(p1.get_age())