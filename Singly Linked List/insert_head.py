class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # pointer to next node


class SinglyLinkedList:
    def __init__(self):
        self.head = None   # initially empty list

    def traverse(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")
        
    def insertBeginning(self,new_data)

sll = SinglyLinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

sll.head = n1
n1.next = n2
n2.next = n3
n3.next = n4

sll.traverse()