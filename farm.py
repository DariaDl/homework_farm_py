
class Animal:
    total_weight = 0
    max_weight = 0
    animal_max_name = ' '



    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

        self.eat = self.feeding()
        self.action = self.some_action()
        self.voice = self.voice()
        Animal.total_weight += self.weight


        if self.weight > Animal.max_weight:
            Animal.max_weight = self.weight
            Animal.animal_max_name = self.name



    def feeding(self):
        return (f'Животное {self.name} - накормлено')






class Goose(Animal):


    def some_action(self):
        return (f'У {self.name} яйца собраны')

    def voice(self):
        return(f'Животное {self.name} говорит "Га-Га-Га" ')







class Cow(Animal):
    def some_action(self):
        return ( f'{self.name} подоена')


    def voice(self):
        return(f'Животное {self.name} говорит "Му-му-му" ')


class Sheep(Animal):
    def some_action(self):
        return (f'Коза {self.name} - подстрижена')

    def voice(self):
        return(f'Животное {self.name} говорит "Беее-беее" ')


class Goat(Cow,Animal):

    def voice(self):
        return(f'Животное {self.name} говорит "Меее-меее" ')

class Duck(Goose,Animal):

    def voice(self):
        return(f'Животное {self.name} говорит "Кря-кря-кря" ')

class Chicken(Goose,Animal):
    def voice(self):
        return(f'Животное {self.name} говорит "Кудах-тах-тах" ')

grey  = Goose('Серый', 7)
white = Goose('Белый', 5)

manka = Cow('Манька', 720)

barashek = Sheep('Барашек', 120)
curly = Sheep('Кудрявый', 80)

koko = Chicken('Ко-Ко', 4)
kukareku = Chicken('Кукареку', 3)

horn = Goat('Рога', 50)
hoof = Goat('Копыта', 48)

kryakva = Duck('Кряква', 2)



all_animals = [grey , white , manka , barashek , curly , koko , kukareku , horn , hoof , kryakva]
for animal in all_animals:
    print(f'{animal.name}: {animal.eat}, {animal.action}, {animal.voice}')



print(f'Вес всех животных: {Animal.total_weight}')


print(f'Самое тяжелое животное - {Animal.animal_max_name}')