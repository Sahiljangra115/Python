# ------------------------>>> here's how we can self in intializing the variables in a class <<<------------------------

# we can only CREATE using self. in the __init__ method and use in any method/function of the class

class Car:
    def __init__(self, name, model, brand):
        self.name = name
        self.model = model
        self.brand = brand
    def display(self):
        return f"Car Name: {self.name}, Model: {self.model}"
 
class my_car():
    def __init__(self, tyre):
        self.tyre = tyre
        self.name = "My Car"
        pass

mine = Car("Toyota", "Corolla", "japan")
print(mine.display())