# we use try if you think this line of code can break the program, and we use else if you think this line of code will not break the program.

def order(item):

    try:
        if item == "unknown":                                       # Code that can through error
            raise ValueError("Item not known to us.")
        elif isinstance(item, int):
            raise TypeError("Item must be a string.")
    except ValueError as e:
        print(f"Error: {e}")  
    except TypeError as err:
        print(f"Error: {err}")                                      # This block will through the error to the user if the item is unknown.
    else:                                                           # --> Look carefully the else and if block are not connected/ related to each other. either the code runs if block or else block.
        print(f"Order for {item} processed successfully.")
    
    finally:
        
        print("Thank you for your order!")

user = order("chai")
user = order("unknown")
user = order(24)