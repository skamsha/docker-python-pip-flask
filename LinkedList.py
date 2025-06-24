import collections.abc # Added for safe iterable checks in flatten_reverse
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

    def add(self, val, current = None):
        """
        Adds a node containing val to the end of the linked list
        """
        if self._head is None:  # If the list is empty
            self._head = Node(val)
        elif current is None:
            self.add(val, self._head) #Start checking through the Nodes at the head
        elif current.next is None: # Reached the end of the list
            current.next = Node(val)
        else:
            self.add(val, current.next) #Keep checking through the nodes


    def remove(self, val, current = None, previous = None):
        """
        Removes the first node containing val from the linked list
        """
        if self._head is None:  # If the list is empty
            return
        if current is None:
            current = self._head
        if current.data == val:  # If the node to remove is the head
            if previous is None:
                self._head = current.next
            else:
                previous.next = current.next
            return
        if current.next is not None:
            self.remove(val,current.next,current)

    def contains(self, val, current = None, counter = 0):
        """Returns True if the LinkedList contains a value, returns False otherwise"""
        if counter == 0:
            current = self._head #Assign on first passthrough
        if current is None: #Empty list won't contain the value
            return False
        if current.data == val:
            return True
        return self.contains(val, current.next, counter+1) #Recursively iterate through all next values

    def insert(self, val, pos, current = None, counter = 0):
        """Inserts a given value into a given position """
        if counter == 0:
            current = self._head
            if pos == 0: #If inserting at the beginning
                new_head = Node(val)
                new_head.next = self._head
                self._head = new_head
                return
        if current is None:
            current = Node(val) #Empty list
            return
        if counter == pos - 1: #If the counter is right before the desired position,
            new_node = Node(val)
            new_node.next = current.next #adjust new node next to point to the current next
            current.next = new_node #have current.next now point to the new node
            return
        if current.next is None: # end of the list
            current.next = Node(val)
            return
        return self.insert(val, pos, current.next, counter + 1) #recursion

    def reverse(self, current = None, previous = None):
        """Reverses the LinkedList by reversing the pointers"""
        if current is None:
            current = self._head
        if current is None: # empty list
            return
        if current.next is None: #end of list
            self._head = current
            current.next = previous
            return
        next_node = current.next
        current.next = previous
        self.reverse(next_node, current)

    def to_plain_list(self, current = None, plain_list = None):
        """
        Takes the elements of the LinkedList and returns them in the form of
        a regular Python list
        """
        if plain_list is None:
            plain_list = []
        if current is None:
            current = self._head
        if current is None:
            return plain_list
        plain_list.append(current.data)
        if current.next is None:
            return plain_list
        else:
            return self.to_plain_list(current.next, plain_list)
    
    # New method added below for flatten_reverse functionality
    def flatten_reverse(self, max_depth=float('inf'), current_depth=0):
        """
        Returns a generator that yields flattened elements from the linked list
        in reverse order, handling nested containers up to max_depth.
        - Yields lazily without modifying the original list.
        - Flattens iterables (including nested LinkedList) recursively.
        - If max_depth is reached, yields the container as-is.
        """
        def flatten_item(item, depth):
            """Helper to flatten a single item recursively."""
            if depth > max_depth:
                yield item
            elif isinstance(item, LinkedList):
                # Recurse into nested LinkedList, maintaining reversal and depth
                yield from item.flatten_reverse(max_depth, depth)
            elif isinstance(item, collections.abc.Iterable) and not isinstance(item, str):
                # Flatten other iterables in their natural order
                for subitem in item:
                    yield from flatten_item(subitem, depth + 1)
            else:
                yield item
        
        def helper(current):
            """Recursive helper to traverse the list in reverse."""
            if current is None:
                return
            # Recurse to the next node first (for reversal)
            yield from helper(current.next)
            # Then yield flattened items from current node's data
            yield from flatten_item(current.data, current_depth)
        
        # Start traversal from the head
        return helper(self._head)
