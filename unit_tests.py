import unittest
from LinkedList import LinkedList, Node

class UnitTests(unittest.TestCase):
    def test_add_and_to_plain_list(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        self.assertEqual(ll.to_plain_list(), [1, 2, 3])

    def test_insert(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(3)
        ll.insert(2, 1)
        self.assertEqual(ll.to_plain_list(), [1, 2, 3])

    def test_contains(self):
        ll = LinkedList()
        ll.add("a")
        ll.add("b")
        self.assertTrue(ll.contains("a"))
        self.assertFalse(ll.contains("z"))

    def test_reverse(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        ll.reverse()
        self.assertEqual(ll.to_plain_list(), [3, 2, 1])

    def test_flatten_reverse_flat_list(self):
        ll = LinkedList()
        ll.add("a")
        ll.add("b")
        ll.add("c")
        self.assertEqual(list(ll.flatten_reverse()), ["c", "b", "a"])

    def test_flatten_reverse_with_nested_linkedlists(self):
        inner = LinkedList()
        inner.add(2)
        inner.add(3)
        outer = LinkedList()
        outer.add(1)
        outer.add(inner)
        outer.add(4)
        self.assertEqual(list(outer.flatten_reverse()), [4, 3, 2, 1])

    def test_flatten_reverse_with_mixed_iterables(self):
        ll = LinkedList()
        ll.add(1)
        ll.add([2, 3])
        ll.add((4, 5))
        ll.add(6)
        self.assertEqual(list(ll.flatten_reverse()), [6, 5, 4, 3, 2, 1])

    def test_flatten_reverse_ignores_strings(self):
        ll = LinkedList()
        ll.add("hello")
        ll.add(["world", "!"])
        self.assertEqual(list(ll.flatten_reverse()), ["!", "world", "hello"])

    def test_flatten_reverse_with_none_and_empty(self):
        ll = LinkedList()
        ll.add(None)
        ll.add([])
        ll.add(5)
        self.assertEqual(list(ll.flatten_reverse()), [5, None])

    def test_flatten_reverse_respects_max_depth(self):
        ll = LinkedList()
        nested = LinkedList()
        nested.add([1, 2])
        ll.add(nested)
        ll.add(3)
        self.assertEqual(list(ll.flatten_reverse(max_depth=1)), [3, [1, 2]])

    def test_flatten_reverse_max_depth_2(self):
        ll = LinkedList()
        level2 = LinkedList()
        level2.add([1, 2])
        level1 = LinkedList()
        level1.add(level2)
        ll.add(level1)
        ll.add(3)
        self.assertEqual(list(ll.flatten_reverse(max_depth=2)), [3, 2, 1])

    def test_flatten_reverse_shared_substructure(self):
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
        self.assertEqual(list(top.flatten_reverse()), ["z", "y", "z", "x"])

    def test_flatten_reverse_generator_type(self):
        ll = LinkedList()
        ll.add(1)
        out = ll.flatten_reverse()
        self.assertTrue(hasattr(out, '__iter__') and not isinstance(out, list))

    def test_flatten_reverse_does_not_mutate(self):
        ll = LinkedList()
        ll.add(1)
        ll.add([2, 3])
        _ = list(ll.flatten_reverse())
        self.assertEqual(ll.to_plain_list(), [1, [2, 3]])

    def test_flatten_reverse_empty_list(self):
        ll = LinkedList()
        self.assertEqual(list(ll.flatten_reverse()), [])

if __name__ == "__main__":
    unittest.main()
