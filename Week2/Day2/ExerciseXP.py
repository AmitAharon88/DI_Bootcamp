# 🌟 Exercise 1 : Set
#1
my_fav_numbers = [1,2,4,8,16]

#2
my_fav_numbers.append(88)
my_fav_numbers.append(19)
print(my_fav_numbers)

#3
my_fav_numbers.remove(my_fav_numbers[-1])
print(my_fav_numbers)

#4
friend_fav_numbers = [1,2,5,8,10]

#5
our_fav_numbers = my_fav_numbers + friend_fav_numbers
print(our_fav_numbers)

#remove duplicates
in_my_fav_numbers = set(my_fav_numbers)
in_friend_fav_numbers = set(friend_fav_numbers)
in_friends_but_not_in_mine = in_friend_fav_numbers - in_my_fav_numbers
result = my_fav_numbers + list(in_friends_but_not_in_mine)
print(result)

# 🌟 Exercise 2 : Tuple
# No a tuple cannot be modified

# 🌟 Exercise 3 : List
#1
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Apples')

print(basket)

#2
basket.remove('Blueberries')

print(basket)

# #3
basket.append('Kiwi')

print(basket)

# #4
basket.insert(0,'Apples')

print(basket)

# #5
print(basket.count('Apples'))

# #6
basket.clear()


# #7
print(basket)