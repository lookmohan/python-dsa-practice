"""
PROBLEM STATEMENT : 
Given the headd of a linked list , determinbe if the linkeed list has a cycle(loop) 
in it. Return True if there is a cycle. Otherwise return False. A cycle means some
node's next pointer points back to previous node in the list, creating an infinite loop

Example 1 : 3 -> 2 -> 0 ->4 -> 2(back to the node with value 2)
Output : True

Examplle 2 : 1 -> 2 -> None (No cycle)
Output : False

"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

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
        curr = self.head
        
        while curr is not None:
            next_node = curr.next 
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

node1 = Node(10)
sll = SinglyLinkedList()
sll.head = node1

node2 = Node(20)
node1.next = node2

node3 = Node(30)
node2.next = node3

node4 = Node(40)
node3.next = node4

print("Cycle exists?", sll.has_cycle())  # False

node4.next = node2  # create cycle

print("Cycle exists?", sll.has_cycle())  # True


# ===================== WORKFLOW =====================
# Floyd's Cycle Detection Algorithm (Tortoise & Hare)
# 1. Create two pointers: slow and fast, both start at head
# 2. slow moves 1 step at a time, fast moves 2 steps at a time
# 3. If fast or fast.next becomes None -> no cycle -> return False
# 4. If slow == fast at any point -> cycle detected -> return True
# Demo:
#   Nodes: 10 -> 20 -> 30 -> 40
#   First run  : no cycle  -> has_cycle() returns False
#   node4.next = node2 creates a loop: 40 -> 20 (cycle)
#   Second run : slow & fast will eventually meet -> returns True
# Time Complexity : O(n) | Space Complexity : O(1)
# =====================================================
