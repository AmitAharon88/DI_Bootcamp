# Exercise 1
word = input('Give me a word: ')
word_dict = {}

for position, letter in enumerate(word) :
    if letter in word_dict :
        word_dict[letter].append(position)
    else :
         word_dict[letter] = [position]

print(word_dict)

# Exercise 2

wallet = float(input('How much money do you have in your wallet? '))

store_items = {
    'shirt' : '5',
    'shorts' : '7',
    'sweatshirt' : '8',
    'pants' : '10',
}
affordable_items = []

for item, cost in store_items.items():
    if float(cost) <= wallet:     #item cost is <= to money i have
        affordable_items.append(item)   #places the clothing item in the basket
        wallet = wallet - float(cost)

if len(affordable_items) > 0:
    affordable_items.sort()
    print("You can afford the following items:")
    for item in affordable_items:
        print("- " + item)
else:
    print("Nothing")