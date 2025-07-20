question = {"name" : "", "age":"", "city":"", "profession":"", "hobby":""}
result = {"name" : "", "age":"", "city":"", "profession":"", "hobby":""}

for que in question:
    answers = input("give me a answer for "+ que + ": ")
    result.append(answers)
    
print(result)
print("Thank you for your answers!")