# in normal comprehension all the values at put in memory at once but in generators it does not put all the values in memory at once
# it puts the values in memory one by one as we iterate over it


# it is done for efficient memory management
numbers = [1, 2, 3, 4, 5]

total = (num for num in numbers if num >1)
print(total)                                             # output : <generator object <genexpr> at 0x7f99a2a393c0>

# the above result is there because they meant to be consumed as the throw or stream the data one by one 

total = sum(num for num in numbers if num >1)
print(total)


items = [
        {"name": "Notebook", "price": 250, "category": "Stationery"},
        {"name": "Pen", "price": 100, "category": "Stationery"},
        {"name": "Bag", "price": 1200, "category": "Accessories"},
        {"name": "Bottle", "price": 400, "category": "Utensils"},
    ]
def filter_inventory(items: list[dict]) -> tuple[list[str], set[str], dict[str, int], list[int]]:
    
    # Write your code below this line
    names_set = [names["name"] for names in items if names["price"] < 500]
    names_set_unique = {names["category"] for names in items }
    names_set_dict = {names["name"] : names["price"] for names in items}

    print(names_set)
    print(names_set_unique)
    print(names_set_dict)
filter_inventory(items)



#########################################           this is very important so read this carefully                 ############################################################


