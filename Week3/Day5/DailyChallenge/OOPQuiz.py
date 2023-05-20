# Part 1: Quiz
'''
Answer the following questions
    What is a class?
        Provides structure
        blueprint from how something should be defined but doesnt offer any actual content itself.
        Used to create user-defined data structures
        Example- questionare
    What is an instance?
        Also called objects
        Copy of the class with actual values
        Can have as many instances as you want
        Example- my copy of a completed questionnaire
    What is encapsulation?
        Restricting access to a method or variable to prevent data from firect modification.
        Hide information
    What is abstraction?
        Process of handling complexity by hiding unnecessary information from the user. 
    What is inheritance?
        Process by which one class takes on the attributes and methods of another.
    What is multiple inheritance?
        The ability to inhereit from 2 or more different classes.
    What is polymorphism?
        Different or related classes that use the same names for their functions.
    What is method resolution order or MRO?
         Used in inheritance. It is the order in which a method is searched for in a classes hierarchy.
'''

# Part 2
import itertools, random

class Card :        #The instructions were very unclear what to do with this class
    def __init__(self) :
        self.suit = ['Spade','Heart','Diamond','Club']
        self.value = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        
class Deck :
    def __init__(self) :
        self.suit = ['Spade','Heart','Diamond','Club']
        self.value = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        self.deck= []
        
    def create_deck (self) :
        for n in self.suit :
            for c in self.value :
                self.deck.append(f'{c} of {n}')
        # deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
        return self.deck
    
    def shuffle_deck (self) :
        try: 
            if len(self.deck) == 52 :
                random.shuffle(self.deck)
                return self.deck
            else :
                raise ValueError('You do not have a full deck of cards')
        except ValueError as error :
            print(error)
            
    def deal(self):
        delt_card = self.deck[0] # Since the deck was shuffled i didnt need to pick a card at random, I chould just chose the first card.
        print(delt_card)
        self.deck.remove(delt_card)
       
    ''' 
    If I wanted to pick a random card from the shuffled deck
    
        delt_card = random.choice(self.deck)
        print(delt_card)
        self.deck.remove(delt_card)
        print(self.deck)
     '''
        

cards = Deck()
print(cards.create_deck())
print(cards.shuffle_deck())
cards.deal()
cards.deal()
cards.deal()
cards.deal()



