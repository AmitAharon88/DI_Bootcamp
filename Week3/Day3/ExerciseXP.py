# Exercise 1
def __abs__(x) :
    '''function that returns the absolute valye of a value'''
    return abs(x)

print(__abs__(-5))
print(__abs__.__doc__)


def __int__(x) :
    '''function that returns the integer of a value'''
    return int(x)

print(__int__(1.358))
print(__int__.__doc__)
    
def get_name () :
    '''function that ask the user for their name then returns the name'''
    name = input('What is your name?') 
    return name
    
print(get_name())
print(get_name.__doc__)

# Exercise 2

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self) :
        return f'{self.amount} {self.currency}'
        
    
    def __int__(self) :
        return (self.amount)
    
    def __repr__(self) :
        return f'{self.amount} {self.currency}'

    def __add__(self, other) :
        if isinstance (other, int) :
            return self.amount + other
        elif isinstance (other, Currency) and self.currency == other.currency :
            return self.amount + other.amount
        else :
            raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")

    def __iadd__(self, other) :
        if isinstance (other, int) :
            self.amount += other
            return f'{self.amount} {self.currency}'
        elif isinstance (other, Currency) and self.currency == other.currency :
            self.amount += other.amount
            return f'{self.amount} {self.currency}'
        else :
            raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
       
       
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)


print(str(c1))
print(int(c1))
print(repr(c1))
print(c1+5)
print(c1+c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
c1 += c3
print(c1)