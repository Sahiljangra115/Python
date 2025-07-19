class Radha:
    @staticmethod
    # def vrindavan(self, name):
    def vrindavan(name):
        print(f"Radha in Vrindavan with {name}")

#  usually we write like this --> we need self here to access instance variables
# shriji = Radha()
# print(shriji.vrindavan("Krishna"))

# Now using static method(decorator) we can call it without creating an instance

Radha.vrindavan("Krishna")


# --> There is a limitation to the static method that it cannot access instance variables or methods.

