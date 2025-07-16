# ----> Comprehensions means that we create a list , dictionary or set , generators etc with single line of code as shown below

Radhavallabh = ["Radha", "Krishna", "Govind", "Gopal", "Gopal"]
# List Comprehension

new_list = [name for name in Radhavallabh if "a" in name]
print(new_list)  # Output: ['Radha', 'Gopal']

new_set = {name for name in Radhavallabh } # it will autmatically remove all the duplicates as it starts from curly braces or its a set comprehension
print(new_set)

chai = {
    "tea": ["chai", "chai wala", "chai wala"],
    "coffee": ["koffee", "koffee wala", "chai wala"],
    "milk": ["doodh", "doodh wala", "chai"],
}

chai_price = {
    "tea":50,
    "coffee": 100,
    "milk": 30,
}

#final = {person for vendor in chai.values() for person in vendor}# for unique values

final = {vendor:sell/5 for vendor, sell in chai_price.items() } # to remove wala from the final set

print(final) # {'koffee', 'koffee wala', 'chai wala', 'chai', 'doodh wala', 'doodh'}


# ==========>>> remember that in place of person we write that thing which is returned to us at final

# the syntax of comprehensions is
# [expression for item in iterable if condition]
# {expression for item in iterable if condition}
# (expression for item in iterable if condition)
# (expression for item in iterable if condition) # for generators

# there is an expression and a statement
# expression is something which returns a value
# statement is something which does not return a value