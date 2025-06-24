from collections.abc import Iterable

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, value, index):
        if index < 0:
            raise IndexError("Index cannot be negative")
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        prev = None
        i = 0
        while current and i < index:
            prev = current
            current = current.next
            i += 1
        if i != index:
            raise IndexError("Index out of range")
        prev.next = new_node
        new_node.next = current

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
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def to_plain_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def flatten_reverse(self, max_depth=None):
        def _flatten_reverse(value, depth):
            # Stop flattening beyond max_depth
            if max_depth is not None and depth > max_depth:
                yield value
                return

            # Treat None and strings as atomic
            if value is None or isinstance(value, str):
                yield value
                return

            # If value is LinkedList, flatten it recursively
            if isinstance(value, LinkedList):
                vals = []
                current = value.head
                while current:
                    vals.append(current.value)
                    current = current.next
                for v in reversed(vals):
                    yield from _flatten_reverse(v, depth + 1)
                return

            # If value is other iterable (list, tuple, etc.), flatten recursively
            if isinstance(value, Iterable):
                vals = list(value)
                for v in reversed(vals):
                    yield from _flatten_reverse(v, depth + 1)
                return

            # Base case: yield atomic value
            yield value

        return _flatten_reverse(self, 0)
