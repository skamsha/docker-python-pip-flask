import unittest
from LinkedList import LinkedList

class UnitTests(unittest.TestCase):

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.add(13)
        ll.add(81)
        ll.insert(2, 0)
        self.assertEqual(ll.to_plain_list(), [2, 13, 81])

    def test_insert_middle(self):
        ll = LinkedList()
        ll.add(13)
        ll.add(81)
        ll.insert(2, 1)
        self.assertEqual(ll.to_plain_list(), [13, 2, 81])

    def test_insert_end(self):
        ll = LinkedList()
        ll.add(13)
        ll.add(81)
        ll.insert(2, 2)
        self.assertEqual(ll.to_plain_list(), [13, 81, 2])

    def test_insert_beyond_end(self):
        ll = LinkedList()
        ll.add(13)
        ll.add(81)
        ll.insert(2, 5)  # Should still append
        self.assertEqual(ll.to_plain_list(), [13, 81, 2])

    def test_insert_into_empty(self):
        ll = LinkedList()
        ll.insert(3, 3)  # Should just insert as the first node
        self.assertEqual(ll.to_plain_list(), [3])

    def test_reverse_multiple(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        ll.reverse()
        self.assertEqual(ll.to_plain_list(), [3, 2, 1])

    def test_reverse_single(self):
        ll = LinkedList()
        ll.add(17)
        ll.reverse()
        self.assertEqual(ll.to_plain_list(), [17])

    def test_contains_true_false(self):
        ll = LinkedList()
        ll.add("head")
        ll.add("node")
        self.assertTrue(ll.contains("head"))
        self.assertFalse(ll.contains("tails"))

if __name__ == "__main__":
    unittest.main()
