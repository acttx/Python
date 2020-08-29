from stack import Stack
from queue import Queue


def main():
    """
    You are given a pessimistic poem as a group of phrases. 
    The phrases are in strings separated by pound signs: '#'.
    1. Create a single string from this group of phrases.
    2. Next, split the string of phrases into a Python list 
       of phrases using the string split method.
    3. Display the poem by walking through the list and 
       displaying each phrase one per line.
    4. And, at the same time, place each phrase on a Queue. 
    5. After all the phrases have been placed on the Queue, 
       transfer the phrases from the Queue to a Stack.
    6. Then, remove them from the Stack and, at the same time, 
       and display the phrases, one per line.
    The result is another now optimistic poem with the phrases reversed.
    """
    # Create a single string from the 16 Strings below

    str1 = "I am part of a lost generation#and I refuse to believe that#"
    str2 = "I can change the world#I realize this may be a shock but#"
    str3 = "'Happiness comes from within'#is a lie, and#"
    str4 = "'Money will make me happy'#So in 30 years I will tell my children#"
    str5 = "they are not the most important thing in my life#"
    str6 = "My employer will know that#I have my priorities straight because#"
    str7 = "work#is more important than#family#I tell you this#"
    str8 = "Once upon a time#Families stayed together#"
    str9 = "but this will not be true in my era#"
    str10 = "This is a quick fix society#Experts tell me#"
    str11 = "30 years from now, I will be celebrating the 10th anniversary of my divorce#"
    str12 = "I do not concede that#I will live in a country of my own making#"
    str13 = "In the future#Environmental destruction will be the norm#"
    str14 = "No longer can it be said that#My peers and I care about this earth#"
    str15 = "It will be evident that#My generation is apathetic and lethargic#"
    str16 = "It is foolish to presume that#There is hope#"

    poem_queue = Queue()
    poem_stack = Stack()

    #  Single string
    poem = ""
    for i in range(16):
        poem += eval("str" + str(i + 1))

    # Split poem into a list
    poem_list = poem.split("#")

    # Displaying the original poem and placing into queue
    print("Original Poem: " + "\n")
    for i in poem_list:
        print(i)
        poem_queue.enqueue(i)

    # Placing original poem into a stack
    for i in range(len(poem_queue.items)):
        poem_stack.push(poem_queue.dequeue())

    # Removing phrases from stack to display reversed poem
    print("Reversed Poem: ")
    while not poem_stack.is_empty():
        print(poem_stack.pop())


main()
