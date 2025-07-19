class Radha:

    def __init__(self, name , place):
        self.name = name
        self.place = place

    @classmethod
    def from_string(cls, name_place_str):
        name, place = name_place_str.split('-')
        return cls(name, place)
    @classmethod
    def from_dict(cls, data_input):
        return cls(
           data_input['name'],
           data_input['place']
        )
    @staticmethod
    def vrindavan(name):
        print(f"Radha in Vrindavan with {name}")   


data = {'name': 'Radha', 'place': 'Vrindavan'}
name_place_str = "krishna-Vrindavan"
shyama = Radha.from_dict(data)
print(shyama)                                       #output: <__main__.Radha object at 0x7f8c1c0b3d60>
print(shyama.name)                                  #output: Radha
print(Radha.vrindavan("Krishna"))                   #output: Radha in Vrindavan with Krishna


shyam = Radha.from_string(name_place_str)
print(shyama.name)

# We can do something nice here like this these will give dictionary output
print(shyama.__dict__)
print(shyam.__dict__)