import random

class Game:
    def __init__(self):
        self.user_item = self.get_user_item()
        self.computer_item = self.get_computer_item()

    @staticmethod
    def get_user_item():
        moves = ['r', 'p', 's']
        user_item = input('select an item:\n R : rock \n P : paper \n S : scissors\n').lower()
        while user_item not in moves:
            user_item = input('Please select a valid item:\n R : rock \n P : paper \n S : scissors\n').lower()    
        return user_item
    
    @staticmethod
    def get_computer_item():
        moves = ['r', 'p', 's']
        computer_item = random.choice(moves)
        return computer_item

    def get_game_result(self):
        if self.user_item == self.computer_item:
            return 'Draw'
        elif self.user_item == "p" and self.computer_item == "r" or self.user_item == "r" and self.computer_item == "s" or self.user_item == "s" and self.computer_item == "p":
            return 'Win'
        else:
            return 'Loss'
        
    def play(self):        
        print(f'You selected {self.user_item}. The computer selected {self.computer_item}. You {self.get_game_result()}')
        return self.get_game_result()
