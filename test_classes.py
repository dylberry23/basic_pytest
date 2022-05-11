# class Person:
#     def __init__(self, name):
#         self.name = name

# def test_classes_compare():
#     p1 = Person("Mindy")
#     p2 = Person("Daniel")
#     assert p1.name == p2.name

import pytest

class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

def test_classes_compare():
    p1 = Person("Mindy")
    p2 = Person("Mindy")
    assert p1 == p2



class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age

        return False


john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 25)
mary = Person('Mary', 'Doe', 27)

print(john == jane)  # True
print(john == mary)  # False


john = Person('John', 'Doe', 25)
print(john == 20)  # False