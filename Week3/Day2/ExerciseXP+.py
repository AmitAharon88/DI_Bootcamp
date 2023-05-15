class Family :
    def __init__(self, members, last_name) :
        self.members = members
        self.last_name = last_name

family1 = Family([
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
], 'Smith')

print(family1.__dict__)