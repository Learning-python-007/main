/*create 2 classes in python with main class*/

class MainClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

class SubClass(MainClass):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno=rollno
    def display(self):
        super().display()
        print("Rollno:",self.rollno)

s=SubClass("Raj",20,101)
s.display()