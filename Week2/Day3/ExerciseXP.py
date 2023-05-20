# Exercise 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = dict(zip(keys, values))

print(new_dict)

# Exercise 2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

cost = 0
for name, age in family.items() :
    if age < 3 :
        cost1 = 0
        cost += cost1
        print(f'{name} pays ${cost1} for their ticket')
    elif age >= 3 and age <=12 :
        cost2 = 10
        cost += cost2
        print(f'{name} pays ${cost2} for their ticket')
    else :
        cost3 = 15
        cost += cost3
        print(f'{name} pays ${cost3} for their ticket')
        
print(f'Your total: {cost}')

# #BONUS

all_names = []
all_ages = []

while True :
    name = input('What is your name?')
    all_names.append(name)
    age = int(input('What is your age?'))
    all_ages.append(age)
    add_person = input('To add another family member, enter a key, or enter \'done\' to calculate your total: ')
    if add_person.lower() == 'done' :
            break

family = dict(zip(all_names, all_ages))
print(family)

cost = 0

for name, age in family.items() :
    if age < 3 :
        cost1 = 0
        cost += cost1
        print(f'{name} pays ${cost1} for their ticket')
    elif age >= 3 and age <=12 :
        cost2 = 10
        cost += cost2
        print(f'{name} pays ${cost2} for their ticket')
    else :
        cost3 = 15
        cost += cost3
        print(f'{name} pays ${cost3} for their ticket')
        
print(f'Your total: {cost}')


# Exercise 3
brand = {'name': 'Zara', 'creation_date': 1975, 'creator_name': 'Amancio Ortega Gaona', 'type_of_clothes': ['men', 'women', 'children', 'home'], 'international_competitors': ['Gap', 'H&M', 'Benetton'], 'number_stores': 7000, 'major_color': {'France': 'blue', 'Spain': 'red', 'US': 'pink, green'}}

brand['number_stores'] = 2
print(brand)

clothes_type = list(brand["type_of_clothes"])
people = ', '.join(clothes_type[0:3])
print(f'{brand["name"]}\'s client range from {people}.')

brand["country_creation"] = "Spain"
print(brand)

for i, value in brand.items() :
    if i == 'international_competitors' :
        value.append('Desigual')
        print(brand)
        
del brand['creation_date']
print(brand)

print(brand['international_competitors'][-1])

print(brand['major_color']['US'])

print(len(brand))

for key in brand.keys() :
    print(key)
    
more_on_zara = {'creation_date': 1975, 'number_stores': 10000}
brand.update(more_on_zara)
print(brand)

print(brand['number_stores'])       #the number of stores have been updated as the key already existed

## wow that was long :)

# Exercise 4

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {i: item for item, i in enumerate(users)}
print(disney_users_A)

disney_users_B = {i: item for i, item in enumerate(users)}
print(disney_users_B)

users.sort()
disney_users_C = {i: item for item, i in enumerate(users)}
print(disney_users_C)

disney_A_modified1 = []
for item in disney_users_A :
    if 'i' in item :
        disney_A_modified1.append(item)
disney_A_modified1_result = {i: item for item, i in enumerate(disney_A_modified1)}
print(disney_A_modified1_result)

disney_A_modified2 = []
for item in disney_users_A :
    if item[0] == 'M' or item[0] == 'P' :
        disney_A_modified2.append(item)
disney_A_modified2_result = {i: item for item, i in enumerate(disney_A_modified2)}
print(disney_A_modified2_result)