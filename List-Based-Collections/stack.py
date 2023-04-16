from linked_list import LinkedList


class Stack:
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_value):
        self.ll.append_left(new_value)

    def pop(self):
        return self.ll.pop_left()
