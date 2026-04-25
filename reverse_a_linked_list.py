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
    
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

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
# Reversing a Singly Linked List (In-Place):
# Initial list : 10 -> 20 -> 30 -> 40 -> None
#
# reverse() method:
# 1. Initialize prev = None, current = head
# 2. For each node:
#    a. Save next_node = current.next  (don't lose the rest of the list)
#    b. Flip the pointer: current.next = prev
#    c. Advance prev = current
#    d. Advance current = next_node
# 3. After loop, set head = prev (new head of reversed list)
# 4. call traverse() to print the reversed list
#
# Example:
#   Before : 10 -> 20 -> 30 -> 40 -> None
#   After  : 40 -> 30 -> 20 -> 10 -> None
# Time Complexity : O(n) | Space Complexity : O(1)
# =====================================================
print()
print("after reverse")
sll.reverse()

sll.traverse()