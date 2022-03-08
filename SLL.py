class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def create_linked_list(self, list):
        for item in list:
            self.append(item)
        return

    def print_linked_list(self):
        node_holder = []
        current_node = self.head

        while current_node:
            node_holder.append(current_node.data)
            current_node = current_node.next
        print(node_holder)

