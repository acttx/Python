from comparable import Comparable
from personList import PersonList
from person import Person
from sort_search_funcs import *

def main():
    """
    This main function creates a PersonList object and populates it
    with the contents of a data file containing 30 records each
    containing the first name and birthdate as month day year
    separated by commas:  Merli,9,10,1998

    Next, a request is made to search for a certain Person.
    A Person object is created from the input.
    Then a linear search is performed with the Person object
    If the Person is located in the list, its index is returned
    Otherwise, -1 is returned.
    The number of compares for the linear search is displayed

    Next, a bubble sort is executed to sort the PersonList.
    The sorted list is displayed, along with the number of
    compares it took to sort it

    Next, a request is made to search for another Person.
    A Person object is created from the input.
    Then a binary search is performed with the Person object
    If the Person is located in the sorted list, its index is returned
    Otherwise, -1 is returned.
    The number of compares for the binary search is displayed
    """
    
    #  Create a PersonList object and add the data
    p_list = PersonList()
    p_list.populate("persons.csv")

    # Request a person to search
    print("List searched using linear search")
    print()
    
    name = input("Who do you want to search for?")
    bdate = input("What is their birthdate? (mm-dd-yyyy)")
    print()
    
    # Create a person object from the input
    month, day, year = bdate.split('-')
    p_obj = Person(name, int(year), int(month), int(day))

    # Do a linear search
    index = p_list.search(linear_search, p_obj)

    if index == -1:
        print(name, "is not in the list")
    else:
        print(name, "is at position", index, "in the list")

    # Display the number of compares
    print()
    print("The number of compares are", Comparable.get_num_compares())
    print()
    
    # Reset the compare count
    Comparable.clear_compares() 

    # Sort the list using bubble sort
    p_list.sort(bubble_sort)
    
    print("List sorted by bubble sort") 
    for p in p_list:
        print(p)

    # Display the number of compares
    print()
    print("The number of compares are", Comparable.get_num_compares())
    print()
    
    # Reset the compare count
    Comparable.clear_compares()
     
    # Request a person to search
    print("List searched using binary search")
    print()
    
    name = input("Who do you want to search for?")
    bdate = input("What is their birthdate? (mm-dd-yyyy)")
    print()
    
    # Create a person object from the input
    month, day, year = bdate.split('-')
    p_obj = Person(name, int(year), int(month), int(day))

    # Do a binary search
    index = p_list.search(binary_search, p_obj)
    
    if index == -1:
        print(name, "is not in the list")
    else:
        print(name, "is at position", index, "in the list")

    # Display the number of compares
    print()
    print("The number of compares are", Comparable.get_num_compares())

main()    
