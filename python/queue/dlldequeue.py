from doubly_linked_list import _DoublyLinkedBase

class Empty(Exception):
    pass

class LinkedDequeue(_DoublyLinkedBase):
    """Dequeue implementation using doubly linked list"""

    def first(self):
        """Returns the element at the front of the dequeue without removing it
        
        Raise Empty Exception if the dequeue is empty
        """
        if self.is_empty():
            raise Empty("Dequeue is empty")
        return self._header._next._element

    def last(self):
        """Returns the element at the end of the dequeue without removing it
        
        Raise Empty Exception if the dequeue is empty
        """
        if self.is_empty():
            raise Empty("Dequeue is empty")
        
        return self._trailer._prev._element
    
    def insert_first(self, e):
        """Adds an element e to the front of the dequeue"""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Adds an element e to the end of the dequeue"""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Removes and returns the element at the front of the dequeue
        
        Raise Empty Exception if the dequeue is empty
        """
        if self.is_empty():
            raise Empty("Dequeue is empty")

        return self._delete_node(self._trailer._prev)