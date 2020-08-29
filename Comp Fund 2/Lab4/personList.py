import csv
from person import Person
from sortable import Sortable
from searchable import Searchable

"""
    This class has no instance variables.
    The list data is held in the parent list class object.
    The constructor must call the list constructor: 
        See how this was done in the Tower class. 
    Code a populate method, which reads the CSV file.
        It must use: try / except, csv.reader, 
        and with open code constructs.
    Code the sort method: Must accept a function object 
        and call the function.
    Code the search method: Must accept a function object 
        and a search item Person object and call the function.
    Code a __str__ method: Look at the Tower class for help
    You may want to code a person_at method for debug purposes.
        This takes an index and returns the Person at that location.
"""


class PersonList(Sortable, Searchable, list):

    def __init__(self):
        super().__init__()

    def populate(self, filename):
        try:
            with open(filename, 'r') as input_file:
                lines = csv.reader(input_file)
                emp_list = list(lines)
                for emp in emp_list:
                    name = emp[0]
                    month = int(emp[1])
                    day = int(emp[2])
                    year = int(emp[3])
                    self.append(Person(name, year, month, day))

        except IOError:
            print("File Not Found. Program Exited.")
            exit()

    def person_at(self):
        for i in range(len(self)):
            return self.index(i)

    def sort(self, funcs):
        funcs(self)

    def search(self, func, person_obj):
        return func(self, person_obj)

    def __str__(self):

        x = '[' + '] ['.join(str(d) for d in self)
        return x



