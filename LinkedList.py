from collections.abc import Iterable

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        """Add a new node with the given value to the end of the list."""
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insert(self, value, position):
        """Insert a new node with the given value at the specified position."""
        if position < 0:
            raise IndexError("Position must be non-negative")
        node = Node(value)
        if position == 0:
            node.next = self.head
            self.head = node
            if self.tail is None:
                self.tail = node
            return
        current = self.head
        idx = 0
        while current is not None and idx < position - 1:
            current = current.next
            idx += 1
        if current is None:
            raise IndexError("Position out of range")
        node.next = current.next
        current.next = node
        if node.next is None:
            self.tail = node

    def contains(self, value):
        """Check if the list contains the given value."""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_plain_list(self):
        """Convert the LinkedList to a plain Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def reverse(self):
        """Reverse the linked list in place."""
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head, self.tail = self.tail, self.head

    def flatten_reverse(self, max_depth=None):
        """
        Lazily yield elements from the linked list and nested iterables in reverse order,
        flattening nested structures up to max_depth. Does not mutate original list.
        """
        def _flatten(item, current_depth=0):
            # Handle max_depth limit
            if max_depth is not None and current_depth >= max_depth:
                if isinstance(item, LinkedList):
                    # At max depth: yield each element as is, no further flattening
                    for elem in item.to_plain_list():
                        yield elem
                else:
                    yield item
                return

            # If item is a LinkedList, flatten its plain list recursively
            if isinstance(item, LinkedList):
                yield from _flatten(item.to_plain_list(), current_depth + 1)
                return

            # Strings/bytes are treated as atomic (not flattened)
            if isinstance(item, (str, bytes)):
                yield item
                return

            # Try to iterate over item if it is iterable (list, tuple, etc.)
            if isinstance(item, Iterable):
                # For iterables other than string/bytes, flatten each element reversed
                # but skip flattening for empty iterables or None
                try:
                    iter_list = list(item)
                except TypeError:
                    yield item
                    return

                if len(iter_list) == 0:
                    # Empty iterable yields nothing
                    return

                for elem in reversed(iter_list):
                    yield from _flatten(elem, current_depth + 1)
                return

            # If not iterable, yield item directly
            yield item

        # Start flattening from the linked list itself, reversed order
        return _flatten(self.to_plain_list())

