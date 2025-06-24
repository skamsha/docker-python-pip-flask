import unittest
from LinkedList import LinkedList, Node

class UnitTests(unittest.TestCase):
    def test_insert_beginning(self):
        ll = LinkedList()
        ll.add(10)
        ll.add(20)
        ll.insert(5, 0)
        self.assertEqual(ll.to_plain_list(), [5, 10, 20])

    def test_reverse_basic(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        ll.reverse()
        self.assertEqual(ll.to_plain_list(), [3, 2, 1])

    def test_contains_true_and_false(self):
        ll = LinkedList()
        ll.add("10")
        ll.add("12")
        self.assertTrue(ll.contains("10"))
        self.assertFalse(ll.contains("21"))

    # Flatten_reverse tests based on prompt:
    def test_flatten_reverse_simple_flat(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        self.assertEqual(ll.flatten_reverse(), [3, 2, 1])

    def test_flatten_reverse_nested_lists(self):
        inner = LinkedList()
        inner.add("a")
        inner.add("b")
        outer = LinkedList()
        outer.add(1)
        outer.add(inner)
        outer.add(2)
        # reversed flattened: [2, 'b', 'a', 1]
        self.assertEqual(outer.flatten_reverse(), [2, "b", "a", 1])

    def test_flatten_reverse_with_max_depth(self):
        # Assuming flatten_reverse accepts max_depth arg and obeys it
        inner = LinkedList()
        inner.add("x")
        inner.add("y")
        outer = LinkedList()
        outer.add(1)
        outer.add(inner)
        outer.add(2)
        # flatten with max_depth=1 means do not recurse into inner list
        self.assertEqual(outer.flatten_reverse(max_depth=1), [2, inner, 1])

    def test_flatten_reverse_handles_cycles(self):
        a = LinkedList()
        b = LinkedList()
        a.add(1)
        a.add(b)
        b.add(2)
        b.add(a)  # cycle

        # Should not raise infinite recursion or crash
        result = a.flatten_reverse()
        # Result includes 2 and 1; no infinite loop
        self.assertIn(1, result)
        self.assertIn(2, result)
        self.assertTrue(len(result) >= 2)  # At least these two flattened values

    def test_flatten_reverse_empty(self):
        ll = LinkedList()
        self.assertEqual(ll.flatten_reverse(), [])

    def test_flatten_reverse_with_non_linkedlist_data(self):
        ll = LinkedList()
        ll.add([1, 2])  # regular python list - treated as data, not flattened
        ll.add(3)
        self.assertEqual(ll.flatten_reverse(), [3, [1, 2]])

    def test_flatten_reverse_does_not_modify_original(self):
        ll = LinkedList()
        ll.add(1)
        nested = LinkedList()
        nested.add(2)
        ll.add(nested)
        before = ll.to_plain_list()
        _ = ll.flatten_reverse()
        after = ll.to_plain_list()
        self.assertEqual(before, after)

if __name__ == "__main__":
    unittest.main()
