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

    def flatten_reverse(value, depth):
        if max_depth is not None and depth == max_depth:
            # flatten one more level without recursion
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
                yield from flatten_reverse(v, depth + 1)
            return
    
        if isinstance(value, Iterable):
            vals = list(value)
            for v in reversed(vals):
                yield from flatten_reverse(v, depth + 1)
            return
    
        yield value
