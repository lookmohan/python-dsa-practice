class Node:
    def __init__(self,data):
        self.data = data
        self.next = None    # next represents a pointer

class SinglyLinkedList:
    def __init__(self):
        self.head = None # By denoting head is none , the Node is now empty.

    def traverse(self):
        if self.head is None:
            print('List is empty')
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next

    def del_head(self):
        if self.head is None:
            print("Head is empty")
        else :
            deleted_value = self.head.data
            self.head = self.head.next
            return deleted_value

node1 = Node(10)
sll = SinglyLinkedList()
sll.head = node1

node2 = Node(20)
node1.next = node2

node3 = Node(30)
node2.next = node3

node4 = Node(40)
node3.next = node4

sll.traverse()
print("\nAfter Deleting head node :")

# storing the data so that the value for my reference and see the value of node
deleted = sll.del_head()
print(f'Deleted value : {deleted}')
sll.traverse()
