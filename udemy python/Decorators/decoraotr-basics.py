# the basics of the decorator is that it is a function that takes another function as an argument and extends its behavior without explicitly modifying it.
# decorators are used to add functionality to existing functions in a clean and readable way.
from functools import wraps


def decorator_function(function):
    @wraps(function)  # this is used to preserve the metadata of the original function, such as its name and docstring. (you will get it at the end of the code)

    def wrapper_function():                          # This wrapper function is neccesssary to write because python expects to return a function when we use @decorator_function.
        print("Wrapper executed before ")
        result = function()
        print("Wrapper executed after ")
        return result                                 # this is the result of the function that was passed as a parameter to the decorator_function if we want to have the result from the function
    return wrapper_function
    

@decorator_function                                  # this is a decorator syntax, it is equivalent to `display = decorator_function(display)`. 
                                                     #This states that the line after @decorator_function is passed as a parameter to the decorator_function.
def display():                                       # this function will be passed as a parameter to the decorator_function
    print("Display function executed") 
    
display()                                            # when we call the display function, it will execute the decorator_function first, then the display function.
print(display.__name__)                              # output: wrapper_function, this is because the display function is now replaced by the wrapper_function due to the decorator syntax.

## =================  use this link to learn more === https://claude.ai/share/f8c8ff53-ca6d-4345-b8f0-47d1a86a47f1 ===========================================


#-------------------> This is how the decorator works behind the scenes <-------------------
# When python starts reading the code, it does the following:
# 1. First, it creates the original function
def display():
    print("Display function executed")
    return "Success!"

# 2. Then it immediately does this:
display = decorator_function(display)   # @decorator_function 

# 3. Then it executes the decorator_function with the display function as an argument, which returns the wrapper_function.
# 4. Finally, it assigns the wrapper_function to the display variable, so when we call display(), it actually calls the wrapper_function.