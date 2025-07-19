# here we will discuss the access of base class by code duplication, explicitly, and super method simultaneously

class Base:
    def __init__(self, name):
        self.name = name

    def display(self):
        return f"Base Name: {self.name}"

class Derived(Base):
    def __init__(self, name, age):
        self.name = name            # duplicated code
        self.age = age

class Derived(Base):
    def __init__(self, name, age):
        Base.__init__(self, name)   # Explicitly calling the base class constructor
        self.age = age

class Derived(Base):
    def __init__(self, name, age):
        super().__init__(name)     # Using super() to call the base class constructor
        self.age = age   

# super() is more used in the programming world because it is more flexible and allows for multiple inheritance
