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

    def test_flatten_reverse_nested_lists(self):
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

    def test_flatten_reverse_all_nested(self):
        a = LinkedList()
        a.add(1)
        b = LinkedList()
        b.add(a)
        c = LinkedList()
        c.add(b)
        self.assertEqual(c.flatten_reverse(), [1])

if __name__ == "__main__":
    unittest.main()
