import unittest
from LinkedList import LinkedList
from LinkedList import Node

class UnitTests(unittest.TestCase):

    # Original basic tests (not touching flatten_reverse)
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

    # New test that triggers infinite recursion due to cyclic nested LinkedLists
    def test_flatten_reverse_cyclic_nested(self):
        a = LinkedList()
        b = LinkedList()
        a.add(1)
        a.add(b)
        b.add(2)
        b.add(a)  # Create cycle: b contains a, a contains b
        
        # This should raise RecursionError, but it won't stop gracefully
        with self.assertRaises(RecursionError):
            a.flatten_reverse()

    # New test that triggers attribute errors with malformed node.next
    def test_flatten_reverse_malformed_next(self):
        ll = LinkedList()
        n1 = Node("a")
        n1.next = "not a node"  # malformed next pointer
        ll._head = n1

        with self.assertRaises(AttributeError):
            ll.flatten_reverse()

if __name__ == "__main__":
    unittest.main()
