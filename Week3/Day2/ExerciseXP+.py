# Exercise 1
class Family :
    def __init__(self, members, last_name) :
        self.members = members
        self.last_name = last_name

    def born(self, **child) :
        self.members.append(child)
        if child['age'] > 18 :
            child['is_child'] = True
        else :
            child['is_child'] = False
        print('Congradulations, you have a new addition to you family!')
        
    def family_presentation(self) :
        first_names = ''
        for person in self.members :
            first_names += person['name'] + ' '
        print(f'{self.last_name} : {first_names}')
        
family1 = Family([
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
], 'Smith')

family1.born(name='Amanda', age= 0, gender='female')
family1.family_presentation()

# Exercise 2
class TheIncredibles(Family) :
    
    def use_power(self, name) :
        for person in self.members :
            if person['name'] == name :
                if person['age'] > 18 :   #could us 'is_child' = True
                    print(f"{person['name']} has the power to {person['power']}")
                   
                else :
                    raise Exception(f"{person['name']} is not over 18 years old")
                    
    def incredible_presentation(self) :
        super().family_presentation()
        for person in self.members :
            if person['incredible_name'] != '' :
                print(f"{person['incredible_name']}: {person['power']}")
        

family1 = TheIncredibles([
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
], 'Incredible')

family1.use_power('Sarah')
family1.incredible_presentation()
family1.born(name='jack', age= 0, gender='female', power='Unknown Power', incredible_name= '')
print(family1.__dict__)
family1.incredible_presentation()