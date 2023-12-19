class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


node = Node(20, None)
node2 = Node(30, node)
print(node2.data)
