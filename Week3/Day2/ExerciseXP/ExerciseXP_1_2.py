# # Exercise 1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# class Siamese(Cat):
#     pass

# all_cats = [cat1, cat2, cat3]

# cat1 = Bengal('Annie', 3)
# cat2 = Chartreux('Max', 1)
# cat3 = Siamese('Jerry', 2)

# all_cats = [cat1, cat2, cat3]
# sara_pets

# Exercise 2
class Dog :
    def __init__(self,name,age,weight) :
        self.name = name
        self.age = age
        self.weight = weight
        
    def bark(self) :
        print(f'{self.name} is barking')
    
    def run_speed(self) :
        run_speed = self.weight/self.age *10
        return run_speed
        
    def fight(self, other_dog) :
        run_speed = self.run_speed()
        run_speed_other_dog = other_dog.run_speed()
        if run_speed > run_speed_other_dog :
            print(f'{self.name} won the fight')
        else :
            print(f'{other_dog.name} won the fight')
            
        
dog1 = Dog('Nola', 2, 20)
dog2 = Dog('Mika', 7, 24)
dog3 = Dog('Zuko', 4, 5)

dog1.bark()
print(dog1.run_speed())
dog1.fight(dog2)

dog2.bark()
print(dog2.run_speed())
dog2.fight(dog3)

dog3.bark()
print(dog3.run_speed())
dog3.fight(dog1)

# Exercise 3- See ExerciseXP3.py file

