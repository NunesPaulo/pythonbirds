class Animals:
    species_bird = 'bird'
    species_dog = 'dog'
    species_cat = 'cat'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return f'{self.name} sings {song}'

    def dance(self):
        return f'{self.name} is dancing now!'


a = Animals('Kaka', '15')
b = Animals('Gaio', '34')
c = Animals('Flaiauei', '08')

print(f'''{a.name} is a {a.__class__.species_cat}, she is {a.age} yers old. {(a.sing("'Hey you'"))}. {(a.dance())}''')
print(f'''{b.name} is a {b.__class__.species_dog}, he is {b.age} yers old. {(b.sing("'Get away'"))}. {(b.dance())}''')
print(f'''{c.name} is a {c.__class__.species_bird}, he is {c.age} yers old. {(c.sing("'Oh no!'"))}. {(c.dance())}''')

