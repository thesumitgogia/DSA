class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self, data):
        # print(self.head)
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ''
        # print(itr.next.data)

        while itr:
            llstr += str(itr.data) + ' -> '
            itr = itr.next

        print(llstr)

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, values):
        # self.head = None
        for data in values:
            self.insertAtEnd(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.insertAtBeginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1



        if self.head == None:
            return
        if self.head.data == data_after:
            node = Node(data_to_insert, self.head.next)
            self.head.next = node
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

        print("value not exist")




    def remove_by_value(self, data):
        if self.head == None:
            print("List is Empty")
            return
        if self.head.data == data:
            print("Data founded at 1")
        itr = self.head
        count = 1
        while itr.next != None:
            if itr.next.data == data:
                print(f"Data founded at {count}")
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

        # print(self.head == None)
    # Remove first node that contains data


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtBegining(5)
    ll.insertAtBegining(75)
    ll.insertAtBegining(65)
    ll.insertAtBegining(56)
    ll.insertAtBegining(76)
    ll.insertAtBegining(86)
    ll.insertAtBegining(64)
    # ll.insertAtEnd(59)
    # ll.insertAtBegining(89)
    # ll.insertAtEnd(69)
    # ll.insertAtEnd(79)

    # ll.insert_values(["Banana", "Apple", "Orange", "Grapes", "Mango"])
    # print(ll.get_length())
    # ll.print()
    # ll.remove_at(-20)
    # ll.insert_at(3, 5)

    # ll.remove_by_value(56)
    # ll.insert_after_value(60, 20)
    # print(ll.head.data)
    # print(ll.head.next.data)
    # print(ll.head.next.next.data)
    # print(ll.head.next.next.next.data)
    # print(ll.head.next.next.next.next.data)
    # print(ll.head.next.next.next.next.next.data)
    # print(ll.head.next.next.next.next.next.next.data)
    # print(ll.head.next.next.next.next.next.next.next)

    ll.print()


    
# Methods to add
    # insertAtBeginning(value)
    # insertAtEnd(value)
    # insertAfterNode(node, value)

# Methods to delete
    # deleteNodeByKey(key)
    # deleteNodeByPosition(position)

# Search and Access Methods
    # searchByKey(key)
    # getAtPosition(position)
    # getLength()

# Traversal and Display Methods
    # printList()
    # reverseList()

# Other Methods
    # isEmpty()
    # clear()