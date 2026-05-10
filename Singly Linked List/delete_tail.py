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

    
    def del_tail(self):
        if self.head is None :
            deleted = self.head.data
            return deleted
        else:
            temp = self.head
            while temp.next.next is not None :
                temp = temp.next
            
            deleted_value = temp.next.data
            temp.next = None

            return deleted_value

# ----------- Creating Linked List -----------
sll = SinglyLinkedList()

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

sll.head = node1
node1.next = node2
node2.next = node3
node3.next = node4

# ----------- Before Deletion -----------
print("Before Deletion:")
sll.traverse()

# ----------- Deleting Head -----------
deleted = sll.del_tail()
print("\nDeleted value:", deleted)

# ----------- After Deletion -----------
print("After Deletion:")
sll.traverse()