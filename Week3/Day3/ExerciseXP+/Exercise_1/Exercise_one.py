# Exercise 1
from func import my_addition

print(my_addition(5, 2))

# 🌟 Exercise 2: Random Module
from random import choice

def pick_a_num() :
    your_choice = input('Pick a number from 1 to 10: ')
    comp_choice = choice(range(1, 11))
    if your_choice == comp_choice :
        print('You Win!')

pick_a_num()

# 🌟 Exercise 3: String Module
import string
from random import choices

def alpha_str() :
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    return ', '.join(choices(alphabet, k=5))
    # generate a string of 5 random letters

print(alpha_str())

# 🌟 Exercise 4 : Current Date
from datetime import date

def current_date():
    today = date.today()
    print(today)
    return today
    
current_date()

# Exercise 5 : Amount Of Time Left Until January 1st
from datetime import datetime
def time_left() :
    now = datetime.now()
    january_1st = datetime(now.year + 1, 1, 1)
    time_left = (january_1st - now)
    days_left = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    # uses the divmod() function to compute the number of hours and the remainder of the time delta in seconds after the hours are removed. 
    # first argument is the total number of seconds in the time delta, and the second argument is the number of seconds in an hour (3600).
    minutes_seconds = divmod(remainder, 60)
    # takes the remainder from the previous line as its first argument, and the number of seconds in a minute (60) as its second argument. 
    # function is a tuple containing the number of minutes and the remainder which is the number of seconds remaining after the minutes are removed.
    print(f'the 1st of January is in {days_left} days and {hours}:{minutes_seconds[0]}:{minutes_seconds[1]} hours from today')
    
time_left()

# Exercise 6 : Birthday And Minutes
def age (birthday) :
    today = date.today()
    bday = datetime.strptime(birthday, '%d/%m/%Y')
    age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))
    print(f'You have lived {age*525600} minutes in your life.')

age('08/01/1988')

# Exercise 7 : Upcoming Holiday
# Very hard for me. I found a lot on my code from google, and spent my time understanding how it works.

from datetime import date, datetime, timedelta

def holiday_countdown():
    today = current_date()      # using function from exercise 4
    # I picked universal holiday as the jewish holidays fall on different days every year and I didnt have time to figure that out. 
    holidays = {'new_years_Day': '01/01',
    'valentines_Day': '02/14',
    'mothers_Day': '05/12',
    'fathers_Day':'06/16',
    'halloween_Day': '10/31'}
    next_holiday = ''
    days_until_next = float('inf')
    
    #created the holiday dates for this year (adding a year)
    for holiday_name, holiday_date_str in holidays.items():
        holiday_date = datetime.strptime(holiday_date_str, '%m/%d').date()
        holiday_date = holiday_date.replace(year=today.year)

        if holiday_date < today:
            holiday_date = holiday_date.replace(year=today.year + 1)
    
        days_until_holiday = (holiday_date - today).days
        if days_until_holiday < days_until_next:
            next_holiday = holiday_name
            days_until_next = days_until_holiday
    print(f"The next holiday is {next_holiday}, which is in {days_until_next} days.")

holiday_countdown()

# Exercise 8 : How Old Are You On Jupiter?
def age_on_planets(age) :
    planets = {
        'Earth': 1,
        'Mercury': 0.2408467,
        'Venus': 0.61519726,
        'Mars': 1.8808158,
        'Jupiter': 11.862615,
        'Saturn': 29.447498,
        'Uranus': 84.016846,
        'Neptune': 164.79132,
        }
    for planet_name, planet_years in planets.items():
        planet_age = age / 31557600 * planet_years
        print(f'On {planet_name} you are {planet_age} years old.')

age_on_planets(1000000000)

# Exercise 9 : Faker Module

pip install Faker
import Faker

user_list = []
def populate_users() :
    fake = Faker()
    global user_list
    user = {
        'name': fake.name(),
        'adress': fake.address(),
        'langage_code': fake.language_code()
        }
    user_list.append(user)
    print(user_list)

populate_users()