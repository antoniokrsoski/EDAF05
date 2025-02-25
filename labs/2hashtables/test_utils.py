import unittest
from utils import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_insert(self):
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.head.next.value, 2)
        self.assertEqual(self.ll.head.next.next.value, 3)

    def test_delete(self):
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        self.ll.delete(2)
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.head.next.value, 3)
        self.ll.delete(1)
        self.assertEqual(self.ll.head.value, 3)
        self.ll.delete(3)
        self.assertIsNone(self.ll.head)

    def test_search(self):
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        self.assertTrue(self.ll.search(2))
        self.assertFalse(self.ll.search(4))

    def test_traverse(self):
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        self.assertEqual(self.ll.traverse(), [1, 2, 3])

    def test_sort(self):
        self.ll.insert(3)
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.sort()
        self.assertEqual(self.ll.traverse(), [1, 2, 3])

        self.ll = LinkedList()
        self.ll.insert(4)
        self.ll.insert(3)
        self.ll.insert(2)
        self.ll.insert(1)
        self.ll.sort()
        self.assertEqual(self.ll.traverse(), [1, 2, 3, 4])

        self.ll = LinkedList()
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        self.ll.insert(4)
        self.ll.sort()
        self.assertEqual(self.ll.traverse(), [1, 2, 3, 4])

        self.ll = LinkedList()
        self.ll.insert(4)
        self.ll.insert(1)
        self.ll.insert(3)
        self.ll.insert(2)
        self.ll.sort()
        self.assertEqual(self.ll.traverse(), [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()