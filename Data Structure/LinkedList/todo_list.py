from playsound import playsound


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = nexts


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insertAtBeginning(self, value):
        node = Node(value, self.head)
        self.head = node

    def insertAtEnd(self, value):
        if not self.head:
            self.insertAtBeginning(value)
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(value)
        return

    def insertAfterNode(self, node, value):
        pass


if __name__ == '__main__':
    ll = LinkedList()
    text = "Enter Task:\n"
    # ll.insertAtEnd(input(text))
    # ll.insertAtEnd(input(text))
    # ll.insertAtEnd(input(text))
    # print(ll.head.data)


import os
from playsound import playsound

file_path = os.path.abspath("./song.mp3")
# playsound('E:\Sumit-Gogia\Work\Programming\DSA\Data Structure\LinkedList\Songs\_Ram Siya Ram_64(PagalWorld.com.pe).mp3')



