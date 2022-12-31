#Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area.
#Creați o clasă Shape.Inițializați-o cu lungime și lățime Creați metoda Area.
#Create class rectangle and square which inherits shape and access the method Area.
#Creează o clasă dreptunghi și un pătrat care moștenește forma și accesează metoda Area.
#afla suprafața avand lungime, latime

class Shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def Area(self):
        print("Area:",self.length*self.breadth)

class Rectangle(Shape):
    def __init__(self,length,breadth):
        super().__init__(length,breadth)
    def Area(self):
        super().Area()

class Square(Shape):
    def __init__(self,length,breadth):
        super().__init__(length,breadth)
    def Area(self):
        super().Area()

r=Rectangle(10,20)
r.Area()
s=Square(10,10)
s.Area()