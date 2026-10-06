# Lab exercies 3: Linked List - starter file

# Keep every name exactly as written. A renamed class or method counts as a
# missing answer, even if the code inside it is correct.

# Put your own experiments inside the `if __name__ == "__main__":` block at the
# bottom. Code at the top level of this file runs when your work is marked, so
# a stray print() or input() up there will show up in your feedback.




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def printLinkedList(self):
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return result

    # TODO a: remove the FIRST node and return its data (not the Node).
    # If the list is empty, return None.
    def remove_beginning(self):
        if self.head:
            removed_data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return removed_data
        else:
            return None

    # TODO b: remove the LAST node and return its data (not the Node).
    # If the list is empty, return None.
    def remove_at_end(self):
        if self.head:
            if self.head == self.tail:
                removed_data = self.tail.data
                self.tail = None
                self.head = None
                return removed_data

            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            removed_data = self.tail.data
            current_node.next = None
            self.tail = current_node
            return removed_data
        else:
            return None

    # TODO c: remove the first node holding `data` and return its data.
    # If no node holds `data`, return None and leave the list unchanged.
    def remove_at(self, data):
        if self.head:
            if self.head.data == data:
                return self.remove_beginning()
            
            current_node = self.head
            while current_node.next:
                if current_node.next.data == data:
                    removed_data = current_node.next.data
                    if current_node.next == self.tail:
                        self.tail = current_node
                    current_node.next = current_node.next.next
                    return removed_data
                current_node = current_node.next
                
        else:
            return None

    def clear_all(self):
        if self.head:
            self.head = None
            self.tail = None

        return None

    # TODO d: insert a new node holding `data` right after the first node
    # holding `nodedata`.
    # If no node holds `nodedata`, return None and leave the list unchanged.
    def insert_after(self, nodedata, data):
        current_node = self.head

        while current_node:
            if current_node.data == nodedata:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                if current_node == self.tail:
                    self.tail = new_node
                return
            current_node = current_node.next


if __name__ == "__main__":
    ll = LinkedList()
    for value in [10, 20, 30]:
        ll.insert_at_end(value)
    ll.printLinkedList()