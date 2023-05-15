# # Exercise 1
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cat1 = Cat('Ginger', 2)
# cat2 = Cat('Magic', 1.5)
# cat3 = Cat('Savage', 4)

# def oldest_cat (*cats) :
#     oldest_cat = Cat('', 0)
#     for cat in cats :
#         if cat.age > oldest_cat.age :
#             oldest_cat = cat
#     return oldest_cat

# oc = oldest_cat(cat1, cat2, cat3)
# print(f'The oldest cat is {oc.name}, and is {oc.age} years olds')

# # Exercise 2
# class Dog :
#     def __init__(self, name, height) :
#         self.name = name
#         self.height = height
    
#     def bark (self) :
#         print(f'{self.name} goes woof!')
    
#     def jump (self) :
#         x = self.height * 2
#         print(f'{self.name} jumps {x} cm heigh!')
        
# davids_dog = Dog('Rex', 50)

# print(davids_dog.__dict__)
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog('Teacup', 20)
# print(sarahs_dog.__dict__)
# sarahs_dog.bark()
# sarahs_dog.jump()

# if davids_dog.height > sarahs_dog.height :
#     print(f'{davids_dog.name} is the bigger dog')


# # Exercise 3
# class Song :
#     def __init__(self, lyrics) :
#         self.lyrics = lyrics
  
#   # if the lyrics are givin to you in a string  (IGNORE)
#     # def sing_me_a_song(self) :
#     #     word_list = self.lyrics.split(' ')
#     #     for word in word_list :
#     #         print(word)
    
#     def sing_me_a_song(self) :
#         for element in self.lyrics :
#             print(element)

# song1 = Song(['Twinkle twinkle little start', 'how i wonder what you are', 'up above the world so heigh', 'like a diamond in the sky'])
# song1.sing_me_a_song()

# Exercise 4
class Zoo :
    def __init__(self, zoo_name) :
        self.z_name = zoo_name
        self.animal = []
        
    def add_animal(self, new_animal) :
        if new_animal not in self.animal :
            self.animal.append(new_animal)

    def get_animal(self) :
        for animal in self.animal :
            print(animal)

    def sell_animal(self, animal_sold) :
        if animal_sold in self.animal :
            self.animal.remove(animal_sold)
            print(self.animal)

    def sort_animal(self) :
        sorted_animals = sorted(self.animal)
        print(sorted_animals)

# Can't figure our #6 in exercise 4 
    def group_animals(self) :
        sorted_animals = sorted(self.animal)
        groups = {}
        for animal in groups.values() :
            animal_first_letter = animal[0].upper()
            if animal_first_letter in sorted_animals :
                groups[animal_first_letter].append(animal)
            else :
                groups[animal_first_letter] = animal
        print(groups)
         
    
zoo1 = Zoo('Bronx zoo')
zoo1.add_animal('tiger')
zoo1.add_animal('lion')
zoo1.add_animal('ant')
zoo1.add_animal('ape')
zoo1.add_animal('elephant')
print(zoo1.animal)

zoo1.get_animal()

zoo1.sell_animal('tiger')
zoo1.sort_animal()

zoo1.group_animals()

#Need to seperate out the animal into their own lists based on their first letter