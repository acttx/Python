import sys

sys.setrecursionlimit(10000)
from comparable import Comparable
from person import Person
from personList import PersonList
from sort_search_funcs import *


def main():
    # File name for testing the algorithms
    PERSON_FILE32 = "person32.csv"

    # List sizes for printing
    sizes = ["1K", "2K", "4K", "8K"]

    # This is the listt of sort functions
    sort_funcs = [selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort]

    # Start sorting the small random file with each sort and print the results
    print("Sorting the 32 element Person file")
    print("==================================")
    print()

    fname = PERSON_FILE32

    for func in sort_funcs:
        p_list = PersonList()
        p_list.clear()
        p_list.populate(fname)
        p_list.sort(func)
        f_str = func.__name__

        print("Sorting 32 file {} using {}".format(fname, f_str))
        num_compares = Comparable.get_num_compares()
        print("The number of compares are {}".format(num_compares))
        print()

        print("The sorted list is:")
        for p in p_list:
            print(p)
        print()

        # Reset the compare count
        Comparable.clear_compares()

    print("Sorting the 4 different sized random Person files")
    print("=================================================")
    print()

    # This list of files are for determining the running time
    # of sorting randomized Persons
    random_files = ["person1Ka.csv", "person2Ka.csv",
                    "person4Ka.csv", "person8Ka.csv"]

    for func in sort_funcs:
        s = 0
        for fname in random_files:
            p_list = PersonList()
            p_list.clear()
            p_list.populate(fname)
            p_list.sort(func)

            f_str = func.__name__
            size = sizes[s]
            print("Sorting {} file {} using {}".format(size, fname, f_str))
            s = s + 1
            num_compares = Comparable.get_num_compares()
            print("The number of compares are {}".format(num_compares))
            print()

            # Reset the compare count
            Comparable.clear_compares()

    print("Sorting the 4 different sized sorted Person files")
    print("=================================================")
    print()

    # This list of files are for determining the running time
    # of sorting sorted Persons
    pre_sorted_files = ["person1Kb.csv", "person2Kb.csv",
                        "person4Kb.csv", "person8Kb.csv"]

    for func in sort_funcs:
        s = 0
        for fname in pre_sorted_files:
            p_list = PersonList()
            p_list.clear()
            p_list.populate(fname)
            p_list.sort(func)

            f_str = func.__name__
            size = sizes[s]
            print("Sorting {} file {} using {}".format(size, fname, f_str))
            s = s + 1
            num_compares = Comparable.get_num_compares()
            print("The number of compares are {}".format(num_compares))
            print()

            # Reset the compare count
            Comparable.clear_compares()

    print("Sorting the 4 different sized reverse sorted Person files")
    print("=========================================================")
    print()

    # This list of files are for determining the running time
    # of sorting reverse sorted Persons
    rev_sorted_files = ["person1Kc.csv", "person2Kc.csv",
                        "person4Kc.csv", "person8Kc.csv"]

    for func in sort_funcs:
        s = 0
        for fname in rev_sorted_files:
            p_list = PersonList()
            p_list.clear()
            p_list.populate(fname)
            p_list.sort(func)

            f_str = func.__name__
            size = sizes[s]
            print("Sorting {} file {} using {}".format(size, fname, f_str))
            s = s + 1
            num_compares = Comparable.get_num_compares()
            print("The number of compares are {}".format(num_compares))
            print()

            # Reset the compare count
            Comparable.clear_compares()


# main
main()
