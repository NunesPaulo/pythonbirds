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


class Penguins(Animals):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age
        print('penguins are ready')

    def swim(self):
        return ('swim faster')

    def run(self):
        print('run faster')


a = Animals('Gaio', '34')
b = Animals('Flaiauei', '08')
c = Penguins('Tobi', '12')
d = Penguins('Jenny', '34')


print(f'''{a.name} is a {a.__class__.species_cat}, he is {a.age} yers old. {(a.sing("'Hey you'"))}. {(a.dance())}''')
print(f'''{b.name} is a {b.__class__.species_bird}, he is {b.age} yers old. {(b.sing("'Get away'"))}. {(b.dance())}''')
print()
print(f'{c.name}! Age: {c.age}. {c.swim().upper()}!')

