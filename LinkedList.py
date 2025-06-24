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

    # Your original insert method (unchanged)
    def insert(self, value, position):
        node = Node(value)
        if position == 0:
            node.next = self.head
            self.head = node
            if self.tail is None:
                self.tail = node
            return
        current = self.head
        idx = 0
        while current.next and idx < position - 1:
            current = current.next
            idx += 1
        node.next = current.next
        current.next = node
        if node.next is None:
            self.tail = node

    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_plain_list(self):
        lst = []
        current = self.head
        while current:
            lst.append(current.value)
            current = current.next
        return lst

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def flatten_reverse(self, max_depth=None):
        def _flatten(value, depth):
            if max_depth is not None and depth >= max_depth:
                yield value
                return
            if value is None:
                yield None
            elif isinstance(value, LinkedList):
                # Yield its elements in reverse flattened order
                current_nodes = []
                current = value.head
                while current:
                    current_nodes.append(current.value)
                    current = current.next
                for v in reversed(current_nodes):
                    yield from _flatten(v, depth + 1)
            elif isinstance(value, (list, tuple)) and not isinstance(value, (str, bytes)):
                for v in reversed(value):
                    yield from _flatten(v, depth + 1)
            else:
                yield value

        # Collect all values of this linked list into a list to reverse order (to avoid mutation)
        nodes = []
        current = self.head
        while current:
            nodes.append(current.value)
            current = current.next

        for val in reversed(nodes):
            yield from _flatten(val, 0)
