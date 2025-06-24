import unittest
from LinkedList import LinkedList

class UnitTests(unittest.TestCase):
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

    def test_flatten_reverse_flat_list(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        self.assertEqual(ll.flatten_reverse(), [3, 2, 1])

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
        # Manually construct a malformed linked list (next is not a Node or None)
        ll = LinkedList()
        n1 = Node("a")
        n1.next = "not a node"
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

        self.assertEqual(top.flatten_reverse(), ["z", "y", "z", "x"])

    def test_flatten_reverse_mixed_valid_and_invalid_nesting(self):
        ll = LinkedList()
        valid_nested = LinkedList()
        valid_nested.add(1)
        ll.add(valid_nested)
        ll.add({"bad": "structure"})  # not a LinkedList
        ll.add(2)
        self.assertEqual(ll.flatten_reverse(), [2, {"bad": "structure"}, 1])


if __name__ == "__main__":
    unittest.main()
