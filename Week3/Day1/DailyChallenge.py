class Farm :
    def __init__ (self, name) :
        self.name = name
        self.animal = {}
        print(f'{self.name}\'s farm')
    
    def add_animal(self, new_animal, amount = 1) :
        if new_animal in self.animal.keys() :
            self.animal[new_animal] += amount
        else :
            self.animal[new_animal] = amount
        return self.animal
        
    def get_info(self) :
        for animal, amount in self.animal.items() :
            print(f"{animal} : {amount}")
        print('E-I-E-I-0!')

    def get_animal_types(self) :
        animal_type_list =list(self.animal.keys())
        return animal_type_list
    
  
    def get_short_info (self) :
        animal_type_list = self.get_animal_types()
        animal_type_str = ', '.join(animal_type_list)
        print(f'{self.name}\'s farm has {animal_type_str}.')
 
 # Tried it a different way to pluralize the animals when there is more then1 of them but was not able to get it to work.   
    # def get_short_info (self) :
    #     animal_type_list = self.get_animal_types()
    #     for animal, amount in self.animal.items() :
    #         if amount > 1 :
    #             animal = f'{animal}\'s'
    #             animal_type_list =list(self.animal.keys())
    #     print(f'{self.name}\'s farm has {animal_type_list[1]}, {animal_type_list[2]}.')

mcdonald = Farm("McDonald")
print(mcdonald.add_animal('cow',5))
print(mcdonald.add_animal('sheep'))
print(mcdonald.add_animal('sheep'))
print(mcdonald.add_animal('goat', 12))
mcdonald.get_info()
print(mcdonald.get_animal_types())
mcdonald.get_short_info()