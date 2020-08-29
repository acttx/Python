from comparable import Comparable

"""
    This class is immutable and inherits from Comparable.
    Please code this using private instance variables.
    Each instance variable should have a getter, but no setters.
    Code the compare method, but do not call the base class compare.
    Code a __str__ method.
"""


class Date(Comparable):

    def __init__(self, year, month, day):
        super().__init__()
        self.__year = int(year)
        self.__month = int(month)
        self.__day = int(day)

    def get_year(self):
        return self.__year

    def get_month(self):
        return self.__month

    def get_day(self):
        return self.__day

    def compare(self, other_date):
        if self.__year > other_date.get_year():
            return 1
        elif self.__year < other_date.get_year():
            return -1
        elif self.__year == other_date.get_year():

            if self.__month > other_date.get_month():
                return 1
            elif self.__month < other_date.get_month():
                return -1
            elif self.__month == other_date.get_month():

                return 0
    def __str__(self):
        return '{}-{}-{}'.format(self.__month, self.__day, self.__year)



