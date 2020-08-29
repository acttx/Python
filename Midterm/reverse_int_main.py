from queue_llist import Queue
from stack_list import Stack


def main():
    # (1) Initialize the number to be reversed
    #     and a holder for the reversed number

    orig_num = 1234567  # original number
    rev_num = 0  # reversed number

    # (2) Create the queue and stack for this assignment

    queue = Queue()
    stack = Stack()

    # (3) Call rev_int_rec passing in the original num and the queue
    #     There is no need to return the Queue,
    #     as the reference was passed

    rev_int_rec(orig_num, queue)

    # (4) Loop through the queue:
    #     Dequeue each digit and multiply by the correct power of 10
    #     Start with the highest power of ten, use length of queue
    #     Add these terms to get the reversed number which you
    #     should store in rev_num.

    power = pow(10, len(queue))
    rev_num = 0

    while not queue.is_empty():
        power = power // 10
        num = queue.dequeue()
        rev_num += num * power

    print("Original: ", orig_num, " Reversed: ", rev_num)

    # (5) Call rev_int_stack passing in reversed number
    #     This is the number you built in steps 3 and 4.
    #     There is no need to return the Stack,
    #     as the reference was passed

    rev_int_stack(rev_num, stack)

    # (6) Loop through stack:
    #     Pop each digit and multiply by the appropriate power of 10
    #     Start with the lowest power of ten
    #     Add these terms to get the original number

    power = 1
    orig_num = 0

    while not stack.is_empty():
        num = stack.pop()
        orig_num += num * power
        power = power * 10

    print("Reversed: ", rev_num, " Original: ", orig_num)


def rev_int_stack(num, stack):
    """
    Using a loop:
    Remove each last digit from num using the % operator
    Add each last digit to the stack
    With each round of the loop reduce num by dividing by 10
    Base case is when num is less than 10
    """

    while num > 10:
        last_digit = num % 10
        stack.push(last_digit)
        num = num // 10
    stack.push(num)


def rev_int_rec(num, queue):
    """
    Remove each last digit from num using the % operator
    Add each last digit to the queue
    With each round of recursion reduce num by dividing by 10
    Base case is when num is less than 10
    """

    # Base case: If num < 10
    # Enqueue last digit and return

    if num < 10:
        queue.enqueue(num)

    # else Not Base case:
    # Enqueue last digit and recurse

    else:
        last_digit = num % 10
        num = num // 10
        queue.enqueue(last_digit)
        rev_int_rec(num, queue)


main()

