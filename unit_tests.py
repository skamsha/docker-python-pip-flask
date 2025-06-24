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

    def test_reversed_plain_list_basic(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        reversed_list = ll.reversed_plain_list()
        self.assertEqual(reversed_list, [3, 2, 1])
        self.assertEqual(ll.to_plain_list(), [1, 2, 3])  # Ensure original unchanged

    def test_reversed_plain_list_empty(self):
        ll = LinkedList()
        self.assertEqual(ll.reversed_plain_list(), [])

    def test_reversed_plain_list_one_element(self):
        ll = LinkedList()
        ll.add("x")
        self.assertEqual(ll.reversed_plain_list(), ["x"])
        self.assertEqual(ll.to_plain_list(), ["x"])

    def test_reversed_plain_list_with_duplicates(self):
        ll = LinkedList()
        ll.add("x")
        ll.add("y")
        ll.add("x")
        ll.add("z")
        self.assertEqual(ll.reversed_plain_list(), ["z", "x", "y", "x"])
        self.assertEqual(ll.to_plain_list(), ["x", "y", "x", "z"])
if __name__ == "__main__":
    unittest.main()
