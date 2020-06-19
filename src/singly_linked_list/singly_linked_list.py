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

    def get_max(self):
        if self.head is None:
            return None
        max_val = 0
        current_node = self.head
        while current_node is not None:
            if current_node.value > max_val:
                max_val = current_node.value
            current_node = current_node.next_node
        return max_val
