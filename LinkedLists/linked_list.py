from node import Node


class LinkedList:
    def __init__(self, value=None):
        if value is None:
            self.head = None
        else:
            self.head = Node(value)

    @classmethod
    def from_list(cls, values: list):
        ll = cls()
        for value in values[::-1]:
            ll.appendLeft(value)
        return ll

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self}"

    def get_last_node(self):
        if self.head is None:
            return None
        node = self.head
        while node.next is not None:
            node = node.next
        return node

    def append(self, new_value):
        new_node = Node(new_value)
        last_node = self.get_last_node()
        if last_node is not None:
            last_node.next = new_node
        else:
            self.head = new_node

    def appendLeft(self, new_value):
        new_node = Node(new_value)
        previous_head = self.head
        new_node.next = previous_head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        node = self.head
        previous_node = None
        while node.next is not None:
            previous_node = node
            node = node.next
        previous_node.next = None
        return node.value

    def popLeft(self):
        if self.head is None:
            return None
        pop_value = self.head.value
        self.head = self.head.next
        return pop_value

    def get_node_at(self, position):
        if position == -1:
            return self.get_last_node()
        elif position < -1:
            raise IndexError
        node = self.head
        for _ in range(position):
            if node.next is None:
                raise IndexError
            node = node.next
        return node

    def get_element_at(self, position):
        node = self.get_node_at(position)
        if node is None:
            return None
        return node.value

    def insert_element_at(self, value, position):
        if position == 0:
            self.appendLeft(value)
            return
        new_node = Node(value)
        previous_node = self.get_node_at(position-1)
        new_node.next = previous_node.next
        previous_node.next = new_node
