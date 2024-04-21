class Dog:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name
        
class Cat:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name

class Lion: 
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name

class Fish:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name

class Cow:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name

class Animal:
    # def __init__(self,a):
    #     self.a=a
    #     b=self.a()
    #     print(self.a())
    fish = Fish
    dog = Dog
    cow = Cow
    lion =Lion
    cat = Cat
    

class_name="fish"
name= "Fish"
animal_name=getattr(Animal,class_name)(name=name).get_name()
print(animal_name)