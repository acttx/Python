from comparable import Comparable

class Date(Comparable):
    """
    This class is immutable and inherits from Comparable.
    Please code this using private instance variables.
    Each instance variable should have a getter, but no setters.
    Code the compare method, but do not call the base class compare.
    Code a __str__ method.
    """
    def __init__(self, year, month, day):
        self.__year = int(year)
        self.__month = int(month)
        self.__day = int(day)

    def get_day(self):
        return self.__day

    def get_month(self):
        return self.__month

    def get_year(self):
        return self.__year

    def compare(self, other_date):
        """
        If this date is equal to other_date, a 0 is returned. If
        this date is later than the other_date, a 1 is returned.
        If this date is earlier than the other_date, a 1 is 
        returned. If you wish to count the number of comparisons,
        """
        if self.__year > other_date.get_year():
            return 1
        if self.__year < other_date.get_year():
            return -1
        # Years are equal    
        if self.__month > other_date.get_month():
            return 1
        if self.__month < other_date.get_month():
            return -1
        # Months are equal
        if self.__day > other_date.get_day():
            return 1
        if self.__day < other_date.get_day():
            return -1
        if self.__day == other_date.get_day():
            return 0
        return None

    def __str__(self):
        return "{}-{}-{}".format(self.__month, self.__day, self.__year)
