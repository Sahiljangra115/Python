# Attribute shadowing means that if we changes the value of an attribute in an object,
# it will not change the value of that attribute in the class.
# but if we remove the new changes from that object it falls back to the class value of that attribute.


class radha:                                               
    temperature = 30
    strength = "strong"

harivansh = radha()
harivansh.strength = "very strong"
print(harivansh.strength)                      # Output: very strong
print(radha.strength)                          # Output: strong

# what if we del the attribute from the object
del harivansh.strength
print(harivansh.strength)                      # Output: strong (falls back to class attribute)
# print(radha.strength)


# but what happen if we add a new attribute to the object which not exist in the class
harivansh.age = 25
print(harivansh.age)                            # Output: 25

# now delete that attribute
del harivansh.age
print(harivansh.age)                          # Raises AttributeError: 'radha'