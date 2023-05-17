# Part I
class Text :
    def __init__(self, string) :
        self.string = string

    def sentence_list(self) :
        word_list = self.string.split(' ')
        return word_list
    
    def frequency(self, word) :
        word_list = self.sentence_list()
        try :
            if type(word) == str :
                # can use instead --> if isinstance(word, str) :
                if word in word_list :
                    print(word_list.count(word))
                else :
                    print('None')
            else :
                raise TypeError('You entered the wrong data type. Please enter a str')
        except TypeError as error:
                print(error)


    def word_dict(self) :
        word_list = self.sentence_list()
        word_dict = {word: word_list.count(word) for word in word_list}
        ''' Below was the first code i wrote then i saw when googling i can turn it into a list comprehension:
        word_count = []
        for word in word_list :
             word_count.append(word_list.count(word))
        word_dict = dict(zip(word_list, word_count))'''
        return word_dict
        
    def common_words(self) :
        word_dict = self.word_dict()
        max_frequency = max(word_dict.values())
        common_words = [word for word, freq in word_dict.items() if freq == max_frequency]
        # for the key, value in word dict, if the value is eual to the max frequency then add the its key(the word) to a list containing the common words.
        print(', '.join(common_words))
        
    def unique_words(self) :
        word_dict = self.word_dict()
        min_frequency = min(word_dict.values())
        unique_words = [word for word, freq in word_dict.items() if freq == min_frequency]
        print(unique_words)

    # Part II
    @classmethod
    def create_instance(cls, file_name) :
        with open(file_name, "r") as file :
            new_text = file.read()
        return cls(new_text)
    
# Bonus
import re
import nltk
from nltk.corpus import stopwords

class TextModification(Text) :
    
    def punctuation(self) :
        self.string = re.sub(r'[^\w\s]', '', string)
        print(self.string)

    def remove_stopwords(text):
        stop_words = stopwords.words('english')
        filtered_text = [word for word in text.split() if word.lower() not in stop_words]
        return ' '.join(filtered_text)

 # Part I output         
string = 'A good book would sometimes cost as much as a good house.'
sentence = Text(string)
sentence.frequency('book')
sentence.common_words()
sentence.unique_words()

# Part 2 output
new_instance = Text.create_instance('DI_Bootcamp/Week3/Day4/DailyChallenge/the_stranger.txt')
new_instance.frequency('book')
new_instance.common_words()
new_instance.unique_words()


# Bonus output
sentence = TextModification(string)
sentence.punctuation()
sentence.remove_stopwords()


