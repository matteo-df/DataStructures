import unittest
from linked_list import LinkedList


class LinkedListTestCase(unittest.TestCase):
    def test_str(self):
        ll1 = LinkedList()
        ll2 = LinkedList(5)
        ll3 = LinkedList.from_list([1, 3, 5])
        self.assertEqual(str(ll1), "None")
        self.assertEqual(str(ll2), "5 -> None")
        self.assertEqual(str(ll3), "1 -> 3 -> 5 -> None")

    def test_append(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        self.assertEqual(str(ll), "10 -> 20 -> 30 -> None")

    def test_appendLeft(self):
        ll = LinkedList()
        ll.appendLeft(30)
        ll.appendLeft(20)
        ll.appendLeft(10)
        self.assertEqual(str(ll), "10 -> 20 -> 30 -> None")

    def test_pop(self):
        ll = LinkedList.from_list([10, 20, 30])
        popped_value = ll.pop()
        self.assertEqual(popped_value, 30)
        self.assertEqual(str(ll), "10 -> 20 -> None")
        ll = LinkedList()
        popped_value = ll.pop()
        self.assertEqual(popped_value, None)

    def test_popLeft(self):
        ll = LinkedList.from_list([10, 20, 30])
        popped_value = ll.popLeft()
        self.assertEqual(popped_value, 10)
        self.assertEqual(str(ll), "20 -> 30 -> None")
        ll = LinkedList()
        popped_value = ll.popLeft()
        self.assertEqual(popped_value, None)

    def test_get_element_at(self):
        ll = LinkedList.from_list([10, 20, 30])
        self.assertEqual(ll.get_element_at(0), 10)
        self.assertEqual(ll.get_element_at(1), 20)
        self.assertEqual(ll.get_element_at(2), 30)
        self.assertEqual(ll.get_element_at(-1), 30)
        with self.assertRaises(IndexError) as _:
            ll.get_element_at(3)
        ll = LinkedList()
        self.assertEqual(ll.get_element_at(0), None)

    def test_insert_element_at(self):
        ll = LinkedList.from_list([10, 20, 30])
        ll.insert_element_at(0, 0)
        self.assertEqual(str(ll), "0 -> 10 -> 20 -> 30 -> None")
        ll = LinkedList.from_list([10, 20, 30])
        ll.insert_element_at(100, 1)
        self.assertEqual(str(ll), "10 -> 100 -> 20 -> 30 -> None")
        ll = LinkedList.from_list([10, 20, 30])
        ll.insert_element_at(200, 2)
        self.assertEqual(str(ll), "10 -> 20 -> 200 -> 30 -> None")
        ll = LinkedList.from_list([10, 20, 30])
        ll.insert_element_at(300, 3)
        self.assertEqual(str(ll), "10 -> 20 -> 30 -> 300 -> None")


if __name__ == '__main__':
    unittest.main()
