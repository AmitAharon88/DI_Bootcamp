# Exercise 1
word = input('Give me a word: ')
index_dict = {}

for i, char in enumerate(word) :
    index_dict[char] = []
    print(index_dict)
    index_dict[char].append(i)
    print(index_dict)

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
        print(wallet)

if len(affordable_items) > 0:
    affordable_items.sort()
    print("You can afford the following items:")
    for item in affordable_items:
        print("- " + item)
else:
    print("Nothing")