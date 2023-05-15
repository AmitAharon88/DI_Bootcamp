from ExerciseXP import Dog

class PetDog(Dog) :
    def __init__(self, name, age, weight, trained = False) :
        super().__init__(name, age, weight)
        self.trained = trained
        
    def train(self) :
        self.bark()
        self.trained = True
        
    def play(self, *other_dogs) :
        dog_names = ''
        if other_dogs[0:-1] :
            dog_names = self.name
            last_dog =other_dogs[-1]
            for dog in other_dogs[0:-1] :
                dog_names += ', ' + dog.name       
        print(f'{dog_names}, and {last_dog.name} all play together.')
        
    def do_a_trick(self) :
        trick_list = ['does a barrel roll', 'stands on his back legs', 'shakes your hand', 'plays dead']
        import random
        random_trick = random.choice(trick_list)
        print(f'{self.name} {random_trick}.')
            
        
dog1 = PetDog('Nola', 2, 20)
dog2 = PetDog('Mika', 7, 24)
dog3 = PetDog('Zuko', 4, 5)
        
dog1.train()
dog1.play(dog2, dog3)
dog1.do_a_trick()