"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.insert(0, value)

    def pop(self):
        if len(self.storage) >= 1:
            val = self.storage[0]
            self.storage.pop(0)
            return val
        else:
            return None


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        if self.head is None and self.tail is None:
            return None
        if self.head.next_node is None:
            head_value = self.head.value
            self.tail = None
            self.head = None
            return head_value
        else:
            head_value = self.head.value
            self.head = self.head.next_node
            return head_value

    def contains(self, value):
        if self.head is None:
            return False
        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True

            current_node = current_node.next_node
        return False


linked_list = LinkedList()

linked_list.add_to_head(0)
linked_list.add_to_tail(1)
print(f'does our LL contain 0? {linked_list.contains(0)}')
print(f'does our LL contain 1? {linked_list.contains(1)}')
print(f'does our LL contain 2? {linked_list.contains(2)}')

linked_list.add_to_head(2)
print(f'the start of the list is {linked_list.head.value}')
linked_list.add_to_head(5)
print(f'the start of the list is {linked_list.head.value}')
linked_list.remove_head()
print(f'the start of the list is {linked_list.head.value}')
