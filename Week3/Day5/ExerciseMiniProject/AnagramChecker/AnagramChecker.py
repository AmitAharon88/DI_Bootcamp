from nltk.corpus import wordnet
import itertools

class AnagramChecker :
    def __init__(self, text_file) :
        with open(text_file, "r") as file :
            text = file.read()
        self.words = text
        
    def is_valid_word(self, word) -> bool:
        synsets = wordnet.synsets(word)
        if synsets :
                return True
        else :
                return False
       
    def get_anagrams(self, word) :
        anagrams = []
        for permutation in itertools.permutations(word.lower()):
            permutation_word = ''.join(permutation)
            if permutation_word != word and self.is_valid_word(str(permutation_word)) :
                anagrams.append(permutation_word)
        return anagrams
    
    def is_anagram(self, word1, word2) :
        l_word1 = word1.lower()
        l_word2 = word2.lower()
        if l_word1 != l_word2 and sorted(l_word1) == sorted(l_word2) :
           return True
        else :
            return False 

file1 = AnagramChecker('DI_Bootcamp/Week3/Day5/ExerciseMiniProject/AnagramChecker/sowpods.txt')
file1.is_valid_word('hello')
print(file1.get_anagrams('meat'))
print(file1.is_anagram('apple', 'banana'))
print(file1.is_anagram('late', 'Teal'))


