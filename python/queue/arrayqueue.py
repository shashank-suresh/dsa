class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class ArrayQueue:
    """FIFO Queue implementation using Python list"""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Returns the number of elements present in the queue"""
        return self._size
    
    def is_empty(self):
        """Returns True if there are no elements in the queue"""
        return self._size == 0
    
    def first(self):
        """Returns the value at the front of the queue without removing it
        
        Raises Empty Exception if the queue is empty
        """
        if self.is_empty():
            Empty("Queue is empty")
        return self._data[self._front]
    
    def dequeue(self):
        """Removes and returns the value at the front of the queue
        
        Raise Empty Exception if the queue is empty
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
    
    def enqueue(self, e):
        """Adds an element e at the end of the queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """Resize queue to a new list of capacity >= len(self)"""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        
        self._front = 0
