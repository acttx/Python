

def bubble_sort(obj_list):

    """
    Code this function.
    The PersonList is the obj_list parameter.
    Nothing is returned.
    """
    for pass_num in range(len(obj_list) - 1, 0, -1):
        for i in range(pass_num):
            if obj_list[i].compare(obj_list[i + 1]) == 1:
                temp = obj_list[i]
                obj_list[i] = obj_list[i + 1]
                obj_list[i + 1] = temp


def binary_search(obj_list, obj):
    """
    Code this function.
    The PersonList is the obj_list parameter.
    A Person is the obj to be searched.
    Return an integer: the index of found object or -1.
    """

    first = 0
    last = len(obj_list) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if obj_list[mid] == obj:
            return mid

        else:
            if obj.compare(obj_list[mid]) == -1:
                last = mid - 1
            elif obj.compare(obj_list[mid]) == 1:
                first = mid + 1
            else:
                return mid


def linear_search(obj_list, obj):
    """
    Code this function.
    The PersonList is the obj_list parameter
    A Person is the obj to be searched.
    Return an integer: the index of found object or -1.
    """

    mid = 0
    found = False
    while mid < len(obj_list) and not found:
        if obj_list[mid].compare(obj) == 0:
            return mid
        else:
            mid = mid + 1
    return mid

