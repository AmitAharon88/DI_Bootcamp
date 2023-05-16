class Circle:
    circle_list = []
    
    def __init__(self, name, radius=0, diameter=0):
        self.radius = float(radius)
        self.diameter = float(diameter)
        self.name = name
        Circle.circle_list.append(self)

    def __str__(self) : #str dunder method is to display a informative sentence about the object
        sentence  = f'{self.name} with a radius of {self.radius} and diameter of {self.diameter}'
        return sentence

    @classmethod
    def from_radius(cls, name,radius):
        '''Calculate the diameter getting the radius as arg'''
        return cls(name = name, radius = radius, diameter = radius*2)
    
    @classmethod
    def from_diameter(cls, name, diameter):
        '''Calculate the radius getting the diameter as arg'''
        return cls(name = name, diameter = diameter, radius = diameter/2)
    
    def get_area(self) :
        '''Calculate the area'''
        return float(3.14 * self.radius ** 2)
    
    def __add__(self, other_circle) :
        '''Adds two circle areas'''
        sum_of_circles = self.get_area() + other_circle.get_area()
        print(f'The sum of {self.name} and {other_circle.name} is {sum_of_circles}')
        return sum_of_circles

    def __gt__(self, other_circle) :
        if self.get_area() > other_circle.get_area() :
            return f'{self.name} is bigger than {other_circle.name}'
        elif other_circle.get_area() > self.get_area() :
            return f'{other_circle.name} has a is bigger than {self.name}'
        else :
            return f'{self.name} is the same size as {other_circle.name}'

    def sort_circles(self) :
       sorted_circles = sorted(Circle.circle_list, key=lambda c: c.get_area())
       print(sorted_circles)
# I can't seem to get the names of the circles after i sort them
  

circleA = Circle.from_diameter('circleA', diameter = 4)
circleB = Circle.from_radius('circleB', radius = 4)
circleC = Circle('circleC', 3,6)
circleD = Circle('circleD', 2,4)
circleE = Circle('circleD', 2,4)

(circleA.get_area())
(circleB.get_area())
(circleC.get_area())
(circleD.get_area())
(circleE.get_area())

print(circleA)
print(circleB)
print(circleC)
print(circleD)
print(circleE)

circleA + circleB
circleC + circleD

print(circleC > circleD)
print(circleB > circleA)
print(circleD > circleE)



circleA.sort_circles()
