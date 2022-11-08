class Empty(Exception):
    pass

class LinkedQueue:
    """Implementation of queue using linked list"""

    class _Node:
        """Node of a linked list"""
        __slots__ = '_element', '_next'

        def __init__(self, element, next=None):
            """Creates a new node with data element and points to next node"""
            self._element = element
            self._next = next
        
    def __init__(self):
        """Create an empty queue"""
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        """Returns the number of elements in the queue"""
        return self._size
    
    def is_empty(self):
        """Returns True if there are no elements present in the queue"""
        return self._size == 0

    def first(self):
        """Returns the element at the front of the queue without removing it
        
        Raise Empty Exception if the queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head._element

    def dequeue(self):
        """Removes and returns the element at the front of the queue
        
        Raise Empty Exception if the queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1

        if self.is_empty():
            self._tail = None

        return answer

    def enqueue(self, e):
        """Adds element e to the end of the queue"""
        new = self._Node(e)

        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new
        
        self._tail = new
        self._size += 1
