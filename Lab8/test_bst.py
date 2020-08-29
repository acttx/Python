from charCount import CharCount
from bst import *


def main():
    """
    Create a series of BSTs with TreeNodes that have CharCount elements
    """
    # a. Create a Python list CharCount objects
    #    from this provided dictionary.

    #    You must use a loop to add these dictionary items 
    #    to a Python list. 

    #    Print the list, so as to see the order of the elements.

    char_dict = {'s': 3, 'u': 2, 'p': 2, 'e': 2, 'r': 2,
                 'c': 3, 'a': 3, 'l': 3, 'i': 7, 'f': 1,
                 'g': 1, 't': 1, 'x': 1, 'd': 1, 'o': 2}

    char_list = []

    for char, count in char_dict.items():
        char_list.append(CharCount(char, count))

    print("Character Count List")

    for items in char_list:
        print(items)

    # b. Add the 15 objects as elements in 15 TreeNode objects.
    #    Insert these 15 TreeNode objects into a binary search tree, 
    #    manually. This means that you must link the nodes to 
    #    each other in the correct way so as to create a BST.
    #    The first four nodes are done for you. 

    print()
    print("Manually created tree")

    root = TreeNode(char_list[0])
    root.right = TreeNode(char_list[1])
    root.left = TreeNode(char_list[2])
    root.left.left = TreeNode(char_list[3])
    root.left.right = TreeNode(char_list[4])
    root.left.left.left = TreeNode(char_list[5])
    root.left.left.left.left = TreeNode(char_list[6])
    root.left.left.right = TreeNode(char_list[7])
    root.left.left.right.left = TreeNode(char_list[8])
    root.left.left.right.left.left = TreeNode(char_list[9])
    root.left.left.right.left.left.right = TreeNode(char_list[10])
    root.right.left = TreeNode(char_list[11])
    root.right.right = TreeNode(char_list[12])
    root.left.left.left.right = TreeNode(char_list[13])
    root.left.left.right.right = TreeNode(char_list[14])

    # c. Now, Use the BST you just created to construct a BST  
    #    using the BST class constructor.
    # d. Display this BST using each of the traversals:	
    #      in-order
    #      post_order
    #      pre-order

    ## Add your code here ##

    # from a BST tree: BST(bst = a_bst)
    bst_tree = BST(bst=root)
    print()

    # in-order
    print("BST in-order")
    bst_tree.inorder()
    print()

    # post_order
    print("BST post_order")
    bst_tree.postorder()
    print()

    # pre-order
    print("BST pre-order")
    bst_tree.preorder()
    print()

    # e. Next, construct another BST by passing in the list
    #    of CharCount objects to the BST constructor.
    # f. Display this BST using each of the traversals:	
    #      in-order
    #      post_order
    #      pre-order

    ## Add your code here ##

    # from a list: BST(list_of_objects = a_list)
    bst_list = BST(list_of_objects=char_list)

    print("List created tree")
    print()

    # in-order
    print("BST in-order")
    bst_list.inorder()
    print()

    # post_order
    print("BST post_order")
    bst_list.postorder()
    print()

    # pre-order
    print("BST pre-order")
    bst_list.preorder()
    print()
    # h. Lastly, construct another BST by inserting each CharCount
    #    object from the list created in Step a into the BST 
    # i. Display this BST using each of the traversals:	
    #      in-order
    #      post_order
    #      pre-order

    ## Add your code here ##

    # empty: BST()

    bst_insert = BST()

    for elem in char_list:
        bst_insert.insert(elem)

    print("Inserted created tree")
    print()

    # in-order
    print("BST in-order")
    bst_insert.inorder()
    print()

    # post_order
    print("BST post_order")
    bst_insert.postorder()
    print()

    # pre-order
    print("BST pre-order")
    bst_insert.preorder()
    print()

    # j. Use the BST iterator with the for each loop 
    #    to print each node

    ## Add your code here ##

    bst_iter = BSTIterator(root)

    print("Iterator displayed Tree")
    print()
    print("BST")
    for nodes in bst_iter:
        print(nodes)


main()
