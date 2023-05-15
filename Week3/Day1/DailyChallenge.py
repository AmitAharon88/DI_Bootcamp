class Farm :
    def __init__ (self, name) :
        self.name = name
        self.animal = {}
    
    def add_animal(self, new_animal, amount = 1) :
        if new_animal in self.animal :
            self.animal[new_animal] += amount
        else :
            self.animal[new_animal] = amount
        return self.animal
        
    def get_info(self) :
        print(f'{self.name}\'s farm \n')
        for animal, amount in self.animal.items() :
            print(f"{animal} : {amount}")
        print('\n\tE-I-E-I-0!')

    def get_animal_types(self) :
        animal_type_list =list(sorted(self.animal.keys()))
        return animal_type_list
    
  
    def get_short_info (self) :     
        animal_type_list = self.get_animal_types()
        for animal, amount in self.animal.items() :
            if amount > 1 :
                position_animal = animal_type_list.index(animal)
                animal_type_list[position_animal] += 's'
                animal_type_str = ', '.join(animal_type_list[0:-1])
            sentence = f'{self.name}\'s farm has {animal_type_str}, and {animal_type_list[-1]}.'
        print(sentence)
 

mcdonald = Farm("McDonald")
mcdonald.add_animal('cow',5)
mcdonald.add_animal('sheep')
mcdonald.add_animal('snake')
mcdonald.add_animal('goat', 12)
mcdonald.get_info()
print(mcdonald.get_animal_types())
mcdonald.get_short_info()