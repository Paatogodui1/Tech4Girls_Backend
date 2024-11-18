#Defining a class Car
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print (f'Car details\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}')

#Creating an instance of the Car class
car = Car('Toyota', 'Camry', 2020)
car.display_info()
