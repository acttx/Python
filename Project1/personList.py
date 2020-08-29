import csv
from person import Person
from sortable import Sortable
from searchable import Searchable


class PersonList(list, Sortable, Searchable):
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

    def __init__(self):
        """
        Constructor: You must also call the list constructor
        """
        super().__init__()

    def person_at(self, index):
        """
        Return the Person object at a given index
        """
        return self[index]

    def populate(self, filename):
        try:
            with open(filename, 'r') as input_file:
                lines = csv.reader(input_file)
                person_list = list(lines)
                for person in person_list:
                    name = person[0].strip()
                    month = int(person[1])
                    day = int(person[2])
                    year = int(person[3])

                    p = Person(name, year, month, day)
                    self.append(p)
        except IOError:
            print("File Not Found Error.")

        return

    def sort(self, func_obj):
        """ 
        Sort the list using the passed in function 
        """
        func_obj(self)

    def search(self, func_obj, search_item):
        """
        Search the list for the search item using the passed in function
        """
        return func_obj(self, search_item)

    def __str__(self):
        """
        Returns a string consisting of the PersonList elements
        """
        string = ""

        for p in self:
            string += str(p) + " \n"

        return string
