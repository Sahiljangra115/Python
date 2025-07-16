# --->>>>>   When you have yield "value" (yielding a direct value), it works differently than yield without a value

def shayama():
    yield "Radha"
    yield "Krishna"
    yield "Govind"
    yield "Gopal"
    yield "Radhavallabh"

# vrindavan = shayama()
# for name in vrindavan:
    #print(name)  # Output: Radha Krishna Govind Gopal Radhavallabh

# --- Yield usually stops a function time to time and resumes it from where it stopped/paused the function

# ---- The next() function returns the next item in an iterator
my_pyare = shayama()
print(next(my_pyare))  # Output: Radha
print(next(my_pyare))  # Output: Krishna
print(next(my_pyare))  # Output: Govind
print(next(my_pyare))  # Output: Gopal
print(next(my_pyare))  # Output: Radhavallabh
# print(next(my_pyare))  # Raises StopIteration error as there are no more items