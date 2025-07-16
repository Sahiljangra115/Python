# we are gonna send some message to the yield 
# Remember that we use next() to start the generator 

# refer to my claude chat for easy understanding to Yield and constructors :

#                                  https://claude.ai/share/d0608b35-fdc2-4f2e-aaf6-3b2c7e1e880b


# def send_generators():
#     print("Started generator")
#     received_value = yield
#     yield received_value

# values = send_generators()
# next(values) # output: Startes generator   ---> we cannot send values to a just started generator
# print(values.send("4"))



def send_generators():
    print("Started generator")
    received_value = yield              # this is taking the value from the send() method
    yield received_value                # this will send the received value back to the caller
    while True:
        print(received_value)           # this will keep on running because the loop will run infinitely until we pause it 
        # break                         # this will give output but raises an error StopIteration
        # yield                         #this will pause the loop after first received value to yield until we give it next value using send() method
        received_value = yield

values = send_generators()
next(values)                            # output: Started generator   ---> we cannot send values to a just started generator
values.send("4")
values.send("4")
values.send("4")




# ---> So basically   received_value = yield  it pauses the generator and waits for a value to be sent to it using the send() method and then stores it in received_value variable.
# and yield received_value sends the value back to the caller, which can be captured by the caller.