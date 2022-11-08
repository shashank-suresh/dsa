class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class ArrayDequeue:
    """Dequeue implementation using Python list"""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty dequeue"""
        self._data = [None] * ArrayDequeue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Returns the number of elements present in the dequeue"""
        return self._size
    
    def is_empty(self):
        """Returns True if there are no elements present in the dequeue"""
        return self._size == 0

    def add_first(self, e):
        """Add an element e at the front of the dequeue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1
    
    def add_last(self, e):
        """Add an element e at the end of the dequeue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def delete_first(self):
        """Remove and return the first element from the dequeue
        
        Raise Empty Exception if dequeue is empty
        """
        if self.is_empty():
            Empty("Queue is empty")
        
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return answer

    def delete_last(self):
        """Remove and return the last element from the dequeue
        
        Raise Empty Exception if dequeue is empty
        """
        if self.is_empty():
            Empty("Queue is empty")

        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1

        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return answer

    def first(self):
        """Returns the element at the front of the dequeue without removing it
        
        Raise Empty Exception if dequeue is empty
        """
        if self.is_empty():
            Empty("Queue is empty")
        
        return self._data[self._front]

    def last(self):
        """Returns the element at the end of the dequeue without removing it
        
        Raise Empty Exception if dequeue is empty
        """
        if self.is_empty():
            Empty("Queue is empty")

        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    
    def _resize(self, cap):
        """Resize dequeue to a new list of capacity >= len(self)"""
        old = self._data
        walk = self._front
        self._data = [None] * cap

        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)

        self._front = 0