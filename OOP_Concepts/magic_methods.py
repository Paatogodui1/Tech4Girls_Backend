class Rectangle: 
    def __init__(self, length, width): 
        self.length = length 
        self.width = width 
#Property Method
    @property
    def area(self): 
        return self.length * self.width 
    
#Property Method
    @property
    def perimeter(self): 
        return 2 * (self.length + self.width) 
    
#Dunder method
    def __str__(self): 
        return f"Rectangle(Length: {self.length}, Width: {self.width})" 
    
#Dunder method
    def __eq__(self, other): 
        if isinstance(other, Rectangle): 
            return self.area == other.area 
        return False

#Creating two rectangle instances 
rect1 = Rectangle(2, 4) 
rect2 = Rectangle(9, 8) 

#Displaying the details of the rectangles 
print(rect1) 
print(f"Area: {rect1.area}") 
print(f"Perimeter: {rect1.perimeter}") 
print()
print(rect2) 
print(f"Area: {rect2.area}") 
print(f"Perimeter: {rect2.perimeter}") 
#Comparing the two rectangles 
print(f"Are the areas of the two rectangles equal?\n{rect1 == rect2}")

