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


# ===================== WORKFLOW =====================
# Building a Singly Linked List:
# 1. Node class: each node holds data and a next pointer (None by default)
# 2. SinglyLinkedList class: head starts as None (empty list)
# 3. Nodes are created and linked manually:
#    node1(10) -> node2(20) -> node3(30) -> node4(40) -> None
# 4. sll.head is set to node1 (entry point of the list)
#
# traverse() method:
# 1. If head is None -> print 'List is empty'
# 2. Else start at head, print data with " -> " separator
# 3. Move to next node until None is reached
#
# Output: 10 -> 20 -> 30 -> 40 ->
# Time Complexity : O(n) | Space Complexity : O(n)
# =====================================================