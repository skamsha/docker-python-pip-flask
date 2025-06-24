import unittest
from LinkedList import LinkedList
from LinkedList import Node

class UnitTests(unittest.TestCase):
    # Keep the original non-flatten tests unchanged:
    def test_insert_beginning(self):
        ll = LinkedList()
        ll.add(13)
        ll.add(81)
        ll.insert(2, 0)
        self.assertEqual(ll.to_plain_list(), [2, 13, 81])

    def test_reverse_three_elements(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        ll.reverse()
        self.assertEqual(ll.to_plain_list(), [3, 2, 1])

    def test_contains_true_and_false(self):
        ll = LinkedList()
        ll.add("head")
        ll.add("node")
        self.assertTrue(ll.contains("head"))
        self.assertFalse(ll.contains("tails"))

    # -------- Flatten reverse thorough tests start here --------

    def test_flatten_reverse_flat_list(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        self.assertEqual(ll.flatten_reverse(), [3, 2, 1])

    def test_flatten_reverse_nested_linkedlists(self):
        inner = LinkedList()
        inner.add("a")
        inner.add("b")
        outer = LinkedList()
        outer.add(1)
        outer.add(inner)
        outer.add(2)
        self.assertEqual(outer.flatten_reverse(), [2, "b", "a", 1])

    def test_flatten_reverse_deeply_nested(self):
        ll3 = LinkedList()
        ll3.add("z")
        ll2 = LinkedList()
        ll2.add("y")
        ll2.add(ll3)
        ll1 = LinkedList()
        ll1.add("x")
        ll1.add(ll2)
        self.assertEqual(ll1.flatten_reverse(), ["z", "y", "x"])

    def test_flatten_reverse_empty(self):
        ll = LinkedList()
        self.assertEqual(ll.flatten_reverse(), [])

    def test_flatten_reverse_empty_nested(self):
        empty_nested = LinkedList()  # empty LinkedList nested
        ll = LinkedList()
        ll.add(1)
        ll.add(empty_nested)
        ll.add(2)
        self.assertEqual(ll.flatten_reverse(), [2, 1])

    def test_flatten_reverse_with_non_linkedlist_data(self):
        ll = LinkedList()
        ll.add([1, 2])  # Python list, not LinkedList
        ll.add(3)
        self.assertEqual(ll.flatten_reverse(), [3, [1, 2]])

    def test_flatten_reverse_with_none_data(self):
        ll = LinkedList()
        ll.add(None)
        ll.add(5)
        self.assertEqual(ll.flatten_reverse(), [5, None])

    def test_flatten_reverse_with_malformed_node_next(self):
        # Manually create a malformed linked list where next is not a Node or None
        ll = LinkedList()
        n1 = Node("a")
        n1.next = "not a node"  # Malformed next pointer
        ll._head = n1
        with self.assertRaises(AttributeError):
            ll.flatten_reverse()

    def test_flatten_reverse_shared_nested_list(self):
        shared = LinkedList()
        shared.add("z")

        a = LinkedList()
        a.add("x")
        a.add(shared)

        b = LinkedList()
        b.add("y")
        b.add(shared)

        top = LinkedList()
        top.add(a)
        top.add(b)

        # Shared nested list 'z' appears twice in flattening
        self.assertEqual(top.flatten_reverse(), ["z", "y", "z", "x"])

    def test_flatten_reverse_mixed_valid_and_invalid_nesting(self):
        ll = LinkedList()
        valid_nested = LinkedList()
        valid_nested.add(1)
        ll.add(valid_nested)
        ll.add({"bad": "structure"})  # not a LinkedList
        ll.add(2)
        self.assertEqual(ll.flatten_reverse(), [2, {"bad": "structure"}, 1])

    def test_flatten_reverse_cyclic_nested(self):
        a = LinkedList()
        b = LinkedList()
        a.add(1)
        a.add(b)
        b.add(2)
        b.add(a)  # Creates a cycle
        with self.assertRaises(RecursionError):
            a.flatten_reverse()

    def test_flatten_reverse_with_embedded_python_list(self):
        ll = LinkedList()
        ll.add(1)
        ll.add([2, 3])  # Python list, not LinkedList
        ll.add(4)
        self.assertEqual(ll.flatten_reverse(), [4, [2, 3], 1])

    def test_flatten_reverse_order_consistency(self):
        # Complex nesting to test order precisely
        ll1 = LinkedList()
        ll1.add("a")
        ll2 = LinkedList()
        ll2.add("b")
        ll2.add(ll1)
        ll3 = LinkedList()
        ll3.add("c")
        ll3.add(ll2)
        self.assertEqual(ll3.flatten_reverse(), ["a", "b", "c"])

if __name__ == "__main__":
    unittest.main()
