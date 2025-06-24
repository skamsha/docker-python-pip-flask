from collections.abc import Iterable

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, value, index):
        if index < 0:
            raise IndexError("Index must be non-negative")
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if not self.tail:
                self.tail = new_node
            return
        current = self.head
        prev = None
        curr_index = 0
        while current and curr_index < index:
            prev = current
            current = current.next
            curr_index += 1
        if curr_index != index:
            raise IndexError("Index out of bounds")
        prev.next = new_node
        new_node.next = current
        if new_node.next is None:
            self.tail = new_node

    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head  # after reverse, old head becomes tail
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def to_plain_list(self):
        return list(self)

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def flatten_reverse(self, max_depth=None):
        """
        Generator yielding elements in reverse order, flattening nested structures
        up to max_depth. Strings are not iterated over. Does not mutate original data.
        """
        def _flatten_reverse(value, depth):
            # Stop flattening if max_depth is reached
            if max_depth is not None and depth > max_depth:
                yield value
                return
            
            # If value is None, just yield it
            if value is None:
                yield None
                return

            # Avoid flattening strings
            if isinstance(value, str):
                yield value
                return

            # If value is LinkedList, iterate over its nodes in reverse
            if isinstance(value, LinkedList):
                # iterate nodes in reverse order
                # collect values first to reverse them
                vals = []
                current = value.head
                while current:
                    vals.append(current.value)
                    current = current.next
                for v in reversed(vals):
                    # recurse with increased depth
                    yield from _flatten_reverse(v, depth + 1)
                return

            # If value is some other iterable (list, tuple, set, etc.)
            if isinstance(value, Iterable):
                # Convert to list to reverse order
                vals = list(value)
                for v in reversed(vals):
                    yield from _flatten_reverse(v, depth + 1)
                return

            # Base case: yield the value itself
            yield value

        # To iterate the linked list in reverse order, collect nodes first
        vals = []
        current = self.head
        while current:
            vals.append(current.value)
            current = current.next

        # Yield flattened values in reverse order
        for val in reversed(vals):
            yield from _flatten_reverse(val, 1)
