# this is a way of controlling the to control the values that are set and get outside the class.
# here we figure out is the method or property of a class is editable outside the class or not and how to set the values outside the class.
class Radha:

    def __init__(self, guru):
        self._guru = guru         # python treats _guru as guru as used below in method
        
    @property                     # this is how you get the values outside the class 
    def guru(self):
            return self._guru + " is my guru"
    
    @guru.setter                   # this is how you set the values outside the class
    def guru(self, guru):
         if guru == "Harivansh":
            self._guru = guru
         else:
            raise ValueError("Guru must be Harivansh")  
         
naam = Radha("Harivansh")
print(naam.guru)
# print(naam.guru())               # this is not the right way because if you do so you will get an error because guru is a property, not a method. due to @property decorator.
naam = Radha("Sansari")
print(naam.guru) 
