class Node:
    """
    Represents a node within a LinkedList
    """
    def __init__(self, data):
        """Inits a Node"""
        self.data = data
        self.next = None

class LinkedList:
    """
    Implementation of a LinkedList ADT with some methods defined recursively
    """
    def __init__(self):
        """Inits a LinkedList"""
        self._head = None

    def get_head(self):
        """Returns the first Node object in the list"""
        return self._head

    def add(self, val, current=None):
        """
        Adds a node containing val to the end of the linked list
        """
        if self._head is None:
            self._head = Node(val)
        elif current is None:
            self.add(val, self._head)
        elif current.next is None:
            current.next = Node(val)
        else:
            self.add(val, current.next)

    def remove(self, val, current=None, previous=None):
        """
        Removes the first node containing val from the linked list
        """
        if self._head is None:
            return
        if current is None:
            current = self._head
        if current.data == val:
            if previous is None:
                self._head = current.next
            else:
                previous.next = current.next
            return
        if current.next is not None:
            self.remove(val, current.next, current)

    def contains(self, val, current=None, counter=0):
        """Returns True if the LinkedList contains a value, False otherwise"""
        if counter == 0:
            current = self._head
        if current is None:
            return False
        if current.data == val:
            return True
        return self.contains(val, current.next, counter + 1)

    def insert(self, val, pos, current=None, counter=0):
        """Inserts a given value into a given position"""
        if counter == 0:
            current = self._head
            if pos == 0:
                new_head = Node(val)
                new_head.next = self._head
                self._head = new_head
                return
        if current is None:
            return
        if counter == pos - 1:
            new_node = Node(val)
            new_node.next = current.next
            current.next = new_node
            return
        if current.next is None:
            current.next = Node(val)
            return
        return self.insert(val, pos, current.next, counter + 1)

    def reverse(self, current=None, previous=None):
        """Reverses the LinkedList by reversing the pointers"""
        if current is None:
            current = self._head
        if current is None:
            return
        if current.next is None:
            self._head = current
            current.next = previous
            return
        next_node = current.next
        current.next = previous
        self.reverse(next_node, current)

    def to_plain_list(self, current=None, plain_list=None):
        """Returns a standard Python list of the linked list elements"""
        if plain_list is None:
            plain_list = []
        if current is None:
            current = self._head
        if current is None:
            return plain_list
        plain_list.append(current.data)
        if current.next is None:
            return plain_list
        return self.to_plain_list(current.next, plain_list)

    def flatten_reverse(self, max_depth=None):
        def _flatten(item, current_depth=0):
            # If max_depth reached or exceeded, yield container as-is (but convert LinkedList to plain list once)
            if max_depth is not None and current_depth >= max_depth:
                if isinstance(item, LinkedList):
                    # yield plain list, not the LinkedList object
                    yield item.to_plain_list()
                else:
                    yield item
                return
            
            # Handle LinkedList by converting to plain list and recurse deeper
            if isinstance(item, LinkedList):
                yield from _flatten(item.to_plain_list(), current_depth + 1)
                return
            
            # Strings and bytes are yielded as is
            if isinstance(item, (str, bytes)):
                yield item
                return
            
            # Try to treat item as iterable
            try:
                iter_list = list(item)
            except TypeError:
                # Not iterable, yield item directly
                yield item
                return
            
            # For iterables, flatten elements in reverse order with incremented depth
            for elem in reversed(iter_list):
                yield from _flatten(elem, current_depth + 1)
    
        # Gather data from nodes in normal order
        current = self._head
        data = []
        while current:
            data.append(current.data)
            current = current.next
    
        # Yield from reversed data with flattening
        for elem in reversed(data):
            yield from _flatten(elem)
