#single-inheritance

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Another child class inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating instances of the child classes
dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")

# Calling the speak method on instances
print(dog_instance.speak())  # Output: Buddy says Woof!
print(cat_instance.speak())  # Output: Whiskers says Meow!'

#multilevel-inheritance

# Grandparent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Parent class inheriting from Animal
class Mammal(Animal):
    def give_birth(self):
        return f"{self.name} gives birth to live young."

# Child class inheriting from Mammal
class Dog(Mammal):
    def speak(self):
        return f"{self.name} says Woof!"

# Creating instances of the classes
dog_instance = Dog("Buddy")

# Calling methods on instances
print(dog_instance.speak())       # Output: Buddy says Woof!
print(dog_instance.give_birth())  # Output: Buddy gives birth to live young.


#hiererchical-inheritance

# Parent class
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

# Child class 1
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Child class 2
class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Child class 3
class Square(Rectangle):
    def __init__(self, name, side):
        super().__init__(name, side, side)

# Creating instances of the classes
circle_instance = Circle("Circle", 5)
rectangle_instance = Rectangle("Rectangle", 4, 6)
square_instance = Square("Square", 4)

# Calling the area method on instances
print(circle_instance.area())     # Output: 78.5
print(rectangle_instance.area())  # Output: 24
print(square_instance.area())     # Output: 16

#multiple-inheritance

# Parent class 1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Parent class 2
class Bird:
    def fly(self):
        return f"{self.name} can fly."

# Child class inheriting from both Animal and Bird
class Parrot(Animal, Bird):
    def speak(self):
        return f"{self.name} says Squawk!"

# Creating an instance of the Parrot class
parrot_instance = Parrot("Polly")

# Calling methods on the instance
print(parrot_instance.speak())  # Output: Polly says Squawk!
print(parrot_instance.fly())    # Output: Polly can fly.