class Empty(Exception):
    pass

class LinkedStack:
    """Implementation of a stack using linked list"""

    class _Node:
        """Node of a linked list"""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            """Create a new node with data element that points to next node"""
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        """Returns the number of elements in the stack"""
        return self._size

    def is_empty(self):
        """Returns True if the stack is empty"""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack"""
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Returns the element at the top of the stack without removing it
        
        Raise Empty Exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element

    def pop(self):
        """Removes and returns the element at the top of the stack
        
        Raise Empty Exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1

        return answer
