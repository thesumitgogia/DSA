class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularSinglyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insertAtBeginning(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            node.next = node
            self.tail = node
        node.next = self.head
        self.head = node
        self.tail.next = self.head

    def insertAtTail(self, value):
        node = Node(value)
        if not self.tail:
            self.tail = node
            node.next = self.tail
            self.head = node
        node.next = self.head
        self.tail.next = node
        self.tail = node

    def insertAfterNode(self, node, value):
        if not self.head:
            print("List is empty")
            return
        if self.tail.data == node:
            self.insertAtTail(value)
        if self.head.data == node:
            self.insertAtBeginning(value)
        temp = self.head
        new_node = Node(value)
        while temp != self.tail:
            if node == temp.data:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next


cll = CircularSinglyLinkedList()
cll.insertAtBeginning(40)
cll.insertAtBeginning(30)
cll.insertAtBeginning(20)
cll.insertAtBeginning(50)
cll.insertAtTail(80)
cll.insertAfterNode(30, 90)
print(cll.head.next.next.next.next.next.next.data)
