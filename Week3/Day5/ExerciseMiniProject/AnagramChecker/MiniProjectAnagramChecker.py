import enchant
import itertools

class AnagramChecker :
    def __init__(self, text_file) :
        with open(text_file, "r") as file :
            text = file.read()
        self.words = text
    
    def is_valid_word(self, word) :
        dict = enchant.Dict("en_US")
        word = input("Enter the word: ")
        print(dict.check(word))
       
    def get_anagrams(self, word):
        word = word.lower()
        anagrams = []
        for permutation in itertools.permutations(word):
            permutation_word = ''.join(permutation)
            if permutation_word != word and self.is_valid_word(permutation_word):
                anagrams.append(permutation_word)
        return anagrams

file1 = AnagramChecker('DI_Bootcamp/Week3/Day5/ExerciseMiniProject/sowpods.txt')
AnagramChecker.is_valid_word('hello')
AnagramChecker.get_anagrams('hello', 'meat')
