class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class CircularDoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insertAtBeginning(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            node.next = node
            self.tail = node
            node.prev = node
        self.head.prev = node
        node.next = self.head
        node.prev = self.tail
        self.head = node
        self.tail.next = self.head

    def insertAtTail(self, value):
        if not self.tail:
            self.insertAtBeginning(value)
            return
        node = Node(value)
        node.next = self.tail.next
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.head.prev = node

    def insertAfterNode(self, node, value):
        if not self.head:
            print("List is empty")
            return
        if self.tail.data == node:
            self.insertAtTail(value)
            return
        temp = self.head
        new_node = Node(value)
        while temp != self.tail:
            if node == temp.data:
                new_node.next = temp.next
                new_node.prev = temp
                temp.next.prev = new_node
                temp.next = new_node
                return
            temp = temp.next

    def __iter__(self):
        current = self.head
        while current != self.tail:
            yield current.data
            current = current.next
        yield current.data


cll = CircularDoublyLinkedList()
# cll.insertAtBeginning(40)
# cll.insertAtBeginning(30)
# cll.insertAtBeginning(20)
# cll.insertAtBeginning(50)
# cll.insertAtTail(80)
# cll.insertAfterNode(30, 90)
# print(cll.head.next.next.next.next.next.next.data)
cll.insertAtBeginning(30)
cll.insertAtBeginning(40)
cll.insertAtBeginning(50)
cll.insertAtTail(80)
cll.insertAtTail(60)
# print(cll.tail.data)
cll.insertAfterNode(60, 90)
# print(cll.tail.data)
# print(cll.head.next.next.next.data)
cll.insertAfterNode(30, 120)
# print(cll.head.next.next.next.next.next.next.data)
# print(cll.head.next.data)
cll.insertAfterNode(50, 140)
# print(cll.head.next.data)
for element in cll:
    print(element)
