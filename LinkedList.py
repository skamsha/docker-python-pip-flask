from collections.abc import Iterable

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def add(self, value):
        """Add value to the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, value, index):
        """Insert value at a given index."""
        new_node = Node(value)
        if index <= 0 or not self.head:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        pos = 0
        while current.next and pos < index - 1:
            current = current.next
            pos += 1
        new_node.next = current.next
        current.next = new_node

    def contains(self, value):
        """Check if value exists in list."""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def reverse(self):
        """Reverse the list in place."""
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def to_plain_list(self):
        """Return list of values."""
        return list(self)

    def flatten_reverse(self, max_depth=None):
        """Lazy generator that yields elements in reverse order, flattening nested iterables up to max_depth."""
        def _flatten_reverse(value, depth):
            if max_depth is not None and depth == max_depth:
                # flatten exactly one more level without recursion
                if isinstance(value, LinkedList):
                    vals = []
                    current = value.head
                    while current:
                        vals.append(current.value)
                        current = current.next
                    for v in reversed(vals):
                        yield v
                    return
                elif isinstance(value, Iterable) and not isinstance(value, str):
                    vals = list(value)
                    for v in reversed(vals):
                        yield v
                    return
                else:
                    yield value
                    return

            if max_depth is not None and depth > max_depth:
                yield value
                return

            if value is None:
                yield None
                return

            if isinstance(value, str):
                yield value
                return

            if isinstance(value, LinkedList):
                vals = []
                current = value.head
                while current:
                    vals.append(current.value)
                    current = current.next
                for v in reversed(vals):
                    yield from _flatten_reverse(v, depth + 1)
                return

            if isinstance(value, Iterable):
                vals = list(value)
                for v in reversed(vals):
                    yield from _flatten_reverse(v, depth + 1)
                return

            yield value

        return _flatten_reverse(self, 0)
