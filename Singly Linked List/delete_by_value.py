# Here the K is given will be the position of the node that needs to delete

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

    def del_specific_value(self, element):
        if self.head is None:
            return "List is empty"

        temp = self.head
        prev = None
        # Delete first node (head)
        if temp.data == element:
            deleted_value = self.head.data
            self.head = self.head.next
            return deleted_value
        
        while temp is not None :
            if temp.data == element :
                prev.next = prev.next.next
                break
            prev = temp
            temp = temp.next

        return prev.next.data

sll = SinglyLinkedList()

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

sll.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

sll.traverse()
sll.del_specific_value(20)
sll.traverse()
