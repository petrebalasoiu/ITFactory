from abc import ABC, abstractmethod


# # 1
# # ABSTRACTION:
# # Abstract class GeometricShape
# # Contains a field PI=3.14
# # Contains an abstract method 'area()' (optional)
# # Contains a class method 'describe()' which prints 'Most probably I have corners'


class GeometricShape(ABC):
    PI = 3.14

    @abstractmethod
    def area(self):
        raise NotImplementedError

    def describe(self):
        print('Most probably I have corners')


# # 2
# # INHERITANCE:
# # Class Square - inherits GeometricShape
# # Constructor for side

# # 3
# # ENCAPSULATION:
# # The side is private
# # Implement a getter, setter, deleter for the side
# # Implement the method required by the interface (optional)


class Square(GeometricShape, ABC):

    def __init__(self, side):
        self.__side = side

    @property
    def side(self):
        return self.__side

    @side.getter
    def side(self):
        print(f'Getter: The side is: {self.__side}')
        return self.__side

    @side.setter
    def side(self, side):
        print(f'Setter: The new side is: {side}')
        self.__side = side

    @side.deleter
    def side(self):
        print('Deleter: The side was removed')
        self.__side = None

    def area(self):
        print(f'The Square\'s area is: {self.__side ** 2}')


# # 3
# # ENCAPSULATION:
# # Class Circle - inherits GeometricShape
# # Constructor for radius
# # The radius is private
# # Implement a getter, setter, deleter for the side
# # Implement the method required by the interface - use the PI field inherited by the parent class (optional)


class Circle(GeometricShape, ABC):

    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.getter
    def radius(self):
        print(f'Getter: The side is: {self.__radius}')
        return self.__radius

    @radius.setter
    def radius(self, radius):
        print(f'Setter: The new side is: {radius}')
        self.__radius = radius

    @radius.deleter
    def radius(self):
        print('Deleter: The side was removed')
        self.__radius = None

    def area(self):
        print(f'The Circle\'s side is: {GeometricShape.PI * (self.__radius ** 2)}')

    def describe(self):
        print('I do not have corners')


cerc1 = Circle(10)
cerc1.radius
cerc1.radius = 20
cerc1.area()
del cerc1.radius
cerc1.radius

print('_____________________________')

patrat1 = Square(15)
patrat1.side
patrat1.side = 30
patrat1.area()
del patrat1.side
patrat1.side
