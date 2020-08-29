def bubble_sort(obj_list):
    sorted = False
    n = len(obj_list) - 1

    while not sorted and n > 0:
        sorted = True
        for i in range(n):
            if obj_list[i].compare(obj_list[i + 1]) > 0:
                sorted = False
                obj_list[i], obj_list[i + 1] = obj_list[i + 1], obj_list[i]
        n -= 1


def selection_sort(obj_list):
    """
    Add code to do a seclection sort
    """
    for i in range(len(obj_list)):
        min_Index = i

        for j in range(i + 1, len(obj_list)):
            if obj_list[min_Index].compare(obj_list[j]) == 1:
                min_Index = j

        obj_list[i], obj_list[min_Index] = obj_list[min_Index], obj_list[i]


def insertion_sort(obj_list):
    """
    Add code to do an insertion sort
    """
    for i in range(1, len(obj_list)):
        key = obj_list[i]
        j = i - 1
        while j >= 0 and key.compare(obj_list[j]) == -1:
            obj_list[j + 1] = obj_list[j]
            j -= 1
        obj_list[j + 1] = key


def merge_sort(obj_list):
    """
    Add code to do a merge sort
    """
    if len(obj_list) <= 1:
        return obj_list

    mid = len(obj_list) // 2
    left = obj_list[:mid]
    right = obj_list[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    return merge(left_list, right_list, obj_list)


def merge(left_list, right_list, temp_list):
    """
    Add code to merge left_list and right_list into temp_List
    """

    i, j, k = 0, 0, 0

    while i < len(left_list) and j < len(right_list):
        if left_list[i].compare(right_list[j]) == -1:
            temp_list[k] = left_list[i]
            i += 1
        else:
            temp_list[k] = right_list[j]
            j += 1
        k += 1
    while i < len(left_list):
        temp_list[k] = left_list[i]
        k += 1
        i += 1

    while j < len(right_list):
        temp_list[k] = right_list[j]
        k += 1
        j += 1

    return temp_list


def quick_sort(obj_list):
    """
    Add code to do a quick sort
    """
    q_sort(obj_list, 0, len(obj_list) - 1)


def q_sort(obj_list, left, right):
    if left >= right:
        return
    pivot = partition(obj_list, left, right)
    q_sort(obj_list, left, pivot - 1)
    q_sort(obj_list, pivot + 1, right)


def partition(obj_list, left, right):
    """
    Add code to partition obj_list into left and right
    """

    # This algorithm assumes the pivot is the first element
    # Picking the middle works best when files are sorted already
    # Swap middle with first
    pivot = left + (right - left) // 2
    obj_list[left], obj_list[pivot] = obj_list[pivot], obj_list[left]
    pivot = left
    left += 1

    while right >= left:
        while left <= right and obj_list[left].compare(obj_list[pivot]) != 1:
            left += 1
        while left <= right and obj_list[right].compare(obj_list[pivot]) == 1:
            right -= 1
        if left <= right:
            obj_list[left], obj_list[right] = obj_list[right], obj_list[left]
            left += 1
            right -= 1
        else:
            break

    obj_list[right], obj_list[pivot] = obj_list[pivot], obj_list[right]

    return right


def heapify(obj_heap, size, root):
    """
    Add code to heapify a list
    """
    largest = root
    left = (2 * root) + 1
    right = (2 * root) + 2

    if left < size and obj_heap[left].compare(obj_heap[root]) > 0:
        largest = left
    if right < size and obj_heap[right].compare(obj_heap[largest]) > 0:
        largest = right
    if largest != root:
        obj_heap[root], obj_heap[largest] = obj_heap[largest], obj_heap[root]
        heapify(obj_heap, size, largest)


def heap_sort(obj_list):
    """
    Add code to do a heap_sort
    """
    size = len(obj_list)

    for i in range(size, -1, -1):
        heapify(obj_list, size, i)

    for i in range(size - 1, 0, -1):
        obj_list[0], obj_list[i] = obj_list[i], obj_list[0]
        heapify(obj_list, i, 0)


# search for an object
def binary_search(obj_list, obj):
    left = 0
    right = len(obj_list) - 1

    while left <= right:

        mid = (left + right) // 2

        # Check if obj exists at mid
        if obj_list[mid].compare(obj) == 0:
            return mid

        # If obj at mid is smaller, ignore left half
        elif obj_list[mid].compare(obj) < 0:
            left = mid + 1

        # obj is greater, ignore right half
        else:
            right = mid - 1

    return -1


# search for an object
def binary_search_rec(obj_list, obj, left=0, right=None):
    if right is None:
        right = len(obj_list) - 1
    if left > right:
        return -1

    mid = (left + right) // 2
    if obj_list[mid].compare(obj) == 0:
        return mid
    if obj_list[mid].compare(obj) > 0:
        return binary_search_rec(obj_list, obj, left, mid - 1)

    return binary_search_rec(obj_list, obj, mid + 1, right)


# search for an object
def linear_search(obj_list, obj):
    for i in range(len(obj_list)):
        if obj_list[i].compare(obj) == 0:
            return i

    return -1
