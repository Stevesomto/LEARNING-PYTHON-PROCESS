# A CLASS IS A BLUEPRINT FOR CREATING OBJECT
# AN OBJECT IS AN INSTANCE OF A CLASS

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    
    def display_info(self):
        print(f"This is a {self.brand} {self.model} ")

# CREATE AN OBJECT
my_car  = Car ("Telsa", "model 3")
my_car.display_info()

your_car = Car("Toyota", "New model")
your_car.display_info()