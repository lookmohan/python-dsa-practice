class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None :
            print("Linked List is Empty")
        else :
            temp = self.head
            while temp is not None :
                print(temp.data, end = " -> ")
                temp = temp.next
# n : Node
n1 = Node(10)
sll = SinglyLinkedList()
sll.head = n1

n2  = Node(20)
n1.next = n2

n3  = Node(30)
n2.next = n3

n4  = Node(40)
n3.next = n4

sll.traverse()
