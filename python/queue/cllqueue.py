class Empty(Exception):
    pass

class CircularQueue:
    """Implementation of a queue using linked lists"""
    
    class _Node:
        """Node of the linked list"""
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next=None):
            self._element = element
            self._next = next
        
    def __init__(self):
        """Create an empty queue"""
        self._tail = None
        self._size = 0
    
    def __len__(self):
        """Returns the number of elements present in the queue"""
        return self._size

    def is_empty(self):
        """Returns True if there are no elements in the queue"""
        return self._size == 0
    
    def first(self):
        """Return the element at the front of the queue without removing it
        
        Raise Empty Exception if the queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        
        head = self._tail._next
        return head._element
    
    def dequeue(self):
        """Remove and return the element at the front of the queue
        
        Raise Empty Exception if the queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        
        head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = head._next

        self._size -= 1
        return head._element

    def enqueue(self, e):
        """Add an element e at the end of the queue"""
        new = self._Node(e)
        if self.is_empty():
            new._next = new
        else:
            new._next = self._tail._next
            self._tail._next = new
        
        self._tail = new
        self._size += 1

    def rotate(self):
        """Rotate the first element to the back of the queue"""
        if self._size > 0:
            self._tail = self._tail._next