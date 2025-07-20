name = []
total_bill = float(input("Enter the total bill amount: "))
if total_bill <= 0:
    print("Total bill must be greater than zero.")
    exit()
friends = int(input("Enter the number of friends: "))
share = total_bill / friends

if friends <= 0:
    print("Number of friends must be greater than zero.")
else:
    for i in range(friends):
        name.append(input("Enter your name: "))
        i += 1

for number in range(len(name)):
    print(f"{name[number]} gets a share of bill = {share:.2f}")
