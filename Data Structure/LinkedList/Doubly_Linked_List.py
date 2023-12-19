class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def isEmpty(self):
        return self.head is None

    def insertAtBeginning(self, value):
        node = Node(None, value, self.head)
        if not self.isEmpty():
            self.head.prev = node
        self.head = node

    def size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def print(self):

        prev = self.head
        print("Previous: None --> ", end='')
        for i in range(self.size() - 1):
            prev = prev.next
            print(prev.prev.data, end='')
            if i == self.size() - 2:
                break
            print(" --> ", end='')

        current = self.head
        next = ''
        print("\nData: \t " + " ", end='')
        while current:
            next += str(current.data) + ' --> '
            current = current.next
        print(next, end=' None')
        print()

        previous = self.head.next
        next_data = ''
        print("Next: \t " + ' ' + ' ', end='')
        while previous:
            next_data += str(previous.data) + ' --> '
            previous = previous.next
        print(next_data, end=' None')
        print()

    def addAtAfter(self, value, after_value):
        if self.head == None:
            print("List is Empty")
            return

        temp = self.head
        while temp:
            if temp.data == after_value:
                node = Node(temp, value, temp.next)
                temp.next.prev = node
                temp.next = node
                tem = node

            temp = temp.next

    def printBackward():
        pass

    def removeAt(self, index):
        pass
        # if self.head == None:
        #     print("The list is empty.")

        # itr = 0
        # while itr < self.size():
        #     if itr == index:
        #         if (itr == 0 and self.head.next == None):
        #             self.head = None
        #             break
        #         else:


ll = LinkedList()

ll.insertAtBeginning(2)
ll.insertAtBeginning(4)
ll.insertAtBeginning(3)
ll.insertAtBeginning(45)
ll.insertAtBeginning(6)
ll.insertAtBeginning(4)
ll.insertAtBeginning(3)
ll.insertAtBeginning(25)
ll.insertAtBeginning(10)
ll.insertAtBeginning(8)
ll.insertAtBeginning(21)
ll.addAtAfter(20, 45)
# print(ll.size())
ll.print()

# ll.printBackward()
