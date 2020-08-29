class Queue:

    def __init__(self):
        self._items = list()

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

    @property
    def items(self):
        return self._items