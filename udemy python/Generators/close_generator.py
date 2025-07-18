def chai():
    yield "masala"
    yield "milk"

def coffee():
    yield "Hot"
    yield "cold"

def favourite():
    yield from chai()
    yield from coffee()

items = favourite()            # This is not calling the Generator its assigning of generator to call a generator we need to use next() function/method
print(items)                   # output: <generator object favourite at 0x7f8c1c0b2d60>
#print(next(items))            # output: masala 


for items in favourite():
    print(items)

                               # we can actually stop the generator at some specific moments using try and except block
def chai_stall():
    try:
      #  yield "masala"
        while True:
            order = yield "What would you like to have?"
    except:
        print("Chai stall closed")

stall = chai_stall()
print(next(stall))            # Output: What would you like to have?
stall.close()                 # this will close the generator and cleans up the resources/memory used by it
 # This triggers the except block and prints "Chai stall closed"1



                             # Key difference: A generator function returns a generator object when called, but doesn't execute until you iterate over it. The for loop triggers the execution and consumes the yielded values.