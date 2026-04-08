# Part 1
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print("Brand:", self.brand)
        print("Year:", self.year)


# Part 2
class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)  
        self.model = model

    def display_info(self):
        super().display_info()
        print("Model:", self.model)

# Part 3
class Motorcycle(Vehicle):
    def __init__(self, brand, year, model, engine):
        super().__init__(brand, year)
        self.model = model
        self.engine = engine

    def display_info(self):
        super().display_info()
        print("Model:", self.model)
        print("Engine:", self.engine) 
