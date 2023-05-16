from deep_translator import GoogleTranslator

french_words = ['Bonjour', 'Au revoir', 'Bienvenue', 'A bientôt'] 
english_words = GoogleTranslator(source='auto', target='en').translate_batch(french_words)
translated_dict = dict(zip(french_words, english_words))

print(translated_dict)

# I'm not sure why Bonjoir does not translate to english