# now we will see how to use self and args in a class

class Chaicup:
    def name(self):
        return "this is without attribute"
    def rollno(self, roll):
        return f"this is with attribute {roll}"

chai = Chaicup()
print(chai.name())                              # here we donot need to pass any argument because we are calling through object 
print(chai.rollno(109))                         # here we donot need to pass any argument because we are calling through object 
print(Chaicup.name("Sahil"))                    # here we --> need to pass any argument because we are calling through class directly
print(Chaicup.rollno("Sahil", 109))             # here we --> need to pass any argument because we are calling through class directly 


# -------> We need to use self so that python can understand the difference between the calling of class and object attributes <-------
# we do not need to pass the self argument while calling the method through object
# but we need to pass the self argument while calling the method through class directly 


# ------------------------>>> here's how we can self in intializing the variables in a class <<<------------------------

# we can only CREATE using self. in the __init__ method and use in any method/function of the class

