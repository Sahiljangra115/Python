# Remenber that every object has a seperate namespace 
#it means if we create a class and then create an object of that class,
#then the object will have its own namespace and it will not affect the class namespace
# means if anything is changed or added in the object it will not affect the class 

class radha:                                               # class initialization
    temperature = 30 
    def harivansh(name):
        print(f"Harivansh {name}")

radhavallabh = radha()                                     # object creation
print(radhavallabh.temperature)                            # variable access
#radhavallabh.harivansh("Maharaj")                         # method call
                                                           # a another method is also needs to be added to the function harivansh known as Self method

radhavallabh.temperature = 40
print(f"radha: {radha.temperature}")                       # class variable access temperature is not changed by object
print(f"radhavallabh: {radhavallabh.temperature}")       

