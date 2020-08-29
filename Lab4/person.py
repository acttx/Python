from comparable import Comparable
from date import Date

"""
This class is immutable and inherits from Comparable.
It uses composition by having a Date object for the birthday.
Please code this using private instance variables.
Each instance variable should have a getter, but no setters.
Code the compare method, and call the base class compare
at the top of the method: super().compare(other_person)
Code a __str__ method.
"""


class Person(Comparable):
    def __init__(self, name, year, month, day):

        super().__init__()
        self.__name = name
        self.__birthday = Date(int(year), int(month), int(day))

    def get_name(self):
        return self.__name

    def get_birthday(self):
        return self.__birthday

    def compare(self, other_person):
        super().compare(other_person)

        if self.__birthday.compare(other_person.get_birthday()) == 1:
            return 1
        elif self.__birthday.compare(other_person.get_birthday()) == -1:
            return -1
        elif self.__birthday.compare(other_person.get_birthday()) == 0:
            if self.__name > other_person.__name:
                return 1
            elif self.__name < other_person.__name:
                return -1
            elif self.__name == other_person.__name:
                return 0

    def __str__(self):
        return self.__name + ': ' + str(self.__birthday)

