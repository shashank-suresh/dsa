class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class ArrayStack:
    """LIFO Stack implementation using Python list"""

    def __init__(self):
        """Create an empty stack"""
        self._data = []
    
    def __len__(self):
        """Return the number of elements present in the stack"""
        return len(self._data)
    
    def is_empty(self):
        """Return True if the stack has no elements"""
        return (len(self._data) == 0)
    
    def push(self, e):
        """Add element e to the top of the stack"""
        self._data.append(e)
    
    def top(self):
        """Return the element at the top of the stack without removing it
        
        Raise Empty Exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        """Remove and return the element at the top of the stack
        
        Raise Empty Exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()