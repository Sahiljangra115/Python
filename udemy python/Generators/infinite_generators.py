def infinite_hello():
    while True:
        yield "hello bro!"

greeter = infinite_hello()
n = int(input("provide me how many times you want me to print this"))
for _ in range(n):  
    print(next(greeter))


# the infinite generstors are used when you do not know how many times you gonna print the statement while also efficiently managing the memory
