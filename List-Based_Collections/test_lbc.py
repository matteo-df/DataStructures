import unittest
from linked_list import LinkedList
from stack import Stack
from queue import Queue


class ListBasedCollTestCase(unittest.TestCase):
    def test_ll_str(self):
        ll1 = LinkedList()
        ll2 = LinkedList(5)
        ll3 = LinkedList.from_list([1, 3, 5])
        self.assertEqual(str(ll1), "None")
        self.assertEqual(str(ll2), "5 -> None")
        self.assertEqual(str(ll3), "1 -> 3 -> 5 -> None")

    def test_ll_append(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        self.assertEqual(str(ll), "10 -> 20 -> 30 -> None")

    def test_ll_append_left(self):
        ll = LinkedList()
        ll.append_left(30)
        ll.append_left(20)
        ll.append_left(10)
        self.assertEqual(str(ll), "10 -> 20 -> 30 -> None")

    def test_ll_pop(self):
        ll = LinkedList.from_list([10, 20, 30])
        popped_value = ll.pop()
        self.assertEqual(popped_value, 30)
        self.assertEqual(str(ll), "10 -> 20 -> None")
        ll = LinkedList()
        popped_value = ll.pop()
        self.assertEqual(popped_value, None)

    def test_ll_pop_left(self):
        ll = LinkedList.from_list([10, 20, 30])
        popped_value = ll.pop_left()
        self.assertEqual(popped_value, 10)
        self.assertEqual(str(ll), "20 -> 30 -> None")
        ll = LinkedList()
        popped_value = ll.pop_left()
        self.assertEqual(popped_value, None)

    def test_ll_get_element_at(self):
        ll = LinkedList.from_list([10, 20, 30])
        self.assertEqual(ll.get_element_at(0), 10)
        self.assertEqual(ll.get_element_at(1), 20)
        self.assertEqual(ll.get_element_at(2), 30)
        self.assertEqual(ll.get_element_at(-1), 30)
        with self.assertRaises(IndexError) as _:
            ll.get_element_at(3)
        ll = LinkedList()
        self.assertEqual(ll.get_element_at(0), None)

    def test_ll_insert_element_at(self):
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

    def test_stacks(self):
        # Set up a Stack
        stack = Stack(1)

        # Test stack functionality
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), None)
        stack.push(4)
        self.assertEqual(stack.pop(), 4)

    def test_queues(self):
        # Set up a queue
        q = Queue(1)
        q.enqueue(2)
        q.enqueue(3)

        # Test peek
        self.assertEqual(q.peek(), 1)

        # Test dequeue
        self.assertEqual(q.dequeue(), 1)

        # Test enqueue
        q.enqueue(4)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        q.enqueue(5)
        self.assertEqual(q.peek(), 5)


if __name__ == '__main__':
    unittest.main()
