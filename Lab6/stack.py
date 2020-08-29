class StackNode:

    def __init__(self, item, link):
        self.item = item
        self.next = link


class Stack:

    def __init__(self):
        self._top = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def peek(self):
        return self._top.item

    def pop(self):
        node = self._top
        self._top = self._top.next
        self._size -= 1

        return node.item

    def push(self, item):
        self._top = StackNode(item, self._top)
        self._size += 1
