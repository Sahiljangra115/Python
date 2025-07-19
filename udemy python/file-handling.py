# file = open("radha.txt", "w")
# try:
#     file.write("Hello, Radha!")
# finally:
#     file.close()
# 
# we can write the above code in a more concise way using the `with` statement:


with open("radha.txt", "w") as file:  # calls the dunders automatically 
    file.write("Hello, Radha!")

# behind the scene two dunders are used: `__enter__` and `__exit__`
# `__enter__` is called when the block is entered, and `__exit__` is called when the block is exited, even if an exception occurs.
# this ensures that the file is properly closed after its block of code is executed, regardless of whether an error occurs or not