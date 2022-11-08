class _DoublyLinkedBase:
    """Base class for doubly linked list representation"""

    class _Node:
        """Node for doubly linked list"""
        __Slots__ = '_element', '_next', '_prev'

        def __init__(self, element=None, prev=None, next=None):
            """Creates a new node with data element and prev and next pointers"""
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Creates an empty doubly linked list"""
        self._header = self._Node()
        self._trailer = self._Node()
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """Returns the number of elements in the doubly linked list"""
        return self._size
    
    def is_empty(self):
        """Returns True if there are no elements present in the doubly linked list"""
        return self._size == 0
    
    def _insert_between(self, e, pred, succ):
        """Add an element between 2 existing nodes and return a new node"""
        new = self._Node(e, pred, succ)
        pred._next = new
        succ._prev = new
        self._size += 1

        return new

    def _delete_node(self, node):
        """Delete a node and return its element"""
        pred = node._prev
        succ = node._next
        pred._next = succ
        succ._prev = pred
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None

        return element