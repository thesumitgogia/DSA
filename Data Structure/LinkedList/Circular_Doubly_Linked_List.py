class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class CircularDoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insertAtBeginning(self, value):
        node = Node(None, value)
        if not self.head:
            self.head = node
            self.tail = node
            node.next = node
            node.prev = node
        self.head.prev = node
        node.next = self.head
        node.prev = self.tail
        self.head = node
        self.head.prev = self.tail
        self.tail.next = node

    def insertAtTail(self, value):
        node = Node(None, value)
        if not self.head:
            self.head = node
            self.tail = node
            node.next = node
            node.prev = node

        self.tail.next = node
        self.head.prev = node
        node.prev = self.tail
        node.next = self.head
        self.tail = node

    def insertAfterNode(self, node, value):
        if not self.head:
            print('List is empty')
            return
        if self.head.data == node:
            self.insertAtBeginning(value)
        if self.tail.data == node:
            self.insertAtTail(value)
        temp = self.head
        new_node = Node(None, value)
        while temp != self.tail:
            if temp.data == node:
                new_node.next = temp.next
                temp.next.prev = new_node
                temp.next = new_node
                new_node.prev = temp

            temp = temp.next


