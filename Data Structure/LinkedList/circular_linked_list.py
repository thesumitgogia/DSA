import timeit


class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self, tail=None, head=None):
        self.tail = tail
        self.head = head

    def insertAtBeginning(self, value):
        new_node = Node(value)
        if not self.tail:
            new_node.prev = new_node
            new_node.next = new_node
            self.tail = new_node
        new_node.next = self.tail.next
        new_node.prev = self.head.prev
        self.head = new_node
        self.tail.next = new_node

    # def insertAtTail(self, value):
    #     # print(self.tail.next.data)
    #     new_node = Node(value, self.tail.next)
    #     self.tail = new_node


cll = CircularLinkedList()

# elapsed_time = timeit.timeit(lambda: cll.insertAtBeginning(20), number=1)
cll.insertAtBeginning(2)
cll.insertAtBeginning(3)
cll.insertAtBeginning(4)
# elapsed_time = timeit.timeit(lambda: cll.insertAtBeginning(20), number=10000)
# print(cll.tail.data)
# cll.insertAtTail(20)
# print(cll.tail.data)

# print(cll.head.next.next.next.next.data)


print(cll.head.data)