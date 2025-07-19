class A:
    label = "A" 

class B(A):
    label = "B"

class C(A):
    label = "C"

class D(B, C):
    pass

cup = D()
print(cup.label)

# Now it will output the label from class B, which is "B"
# because the Method Resolution Order (MRO) prioritizes B over C in the inheritance hierarchy.
#if we swipe the order of inheritance in class D: like class D(C, B): it will output "C"

print(D.__mro__)  