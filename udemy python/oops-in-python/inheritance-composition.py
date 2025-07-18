class Shiva:
    def __init__(self, age):
        self.age = age
    def transfer(self):
        print(f"Shiva's age is {self.age}")

class Radha(Shiva):
    def display(self):
        print(f"trandfered to Radha at age : {self.age}")
        
me = Radha()                      # here as radha does not have any __init__ method, python will look for it in parent class Shiva and assign the valuse there
me.display()  

# --> Here remember one more thing that creating a object and a class both have different syntax.
class Radhavallabh:
    new_class  = Shiva   #==> Here we are creating a new class in do not need parantheses

    def __init__(self):
        self.chai = self.new_class(30)     # here we created an object from the new_class now we can do self.chai.transfer() instead of self.chai().transfer()

    def display(self):
        self.chai.transfer()        


# -----------------> this is the code by instructor <-----------------


class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")


class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai


shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()