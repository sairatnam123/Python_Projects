"""Given elements as nodes of the two singly linked lists. The task is to multiply these two linked lists, say L1 and L2.

Note: The output could be large take modulo 10^9+7.

Examples :

Input: LinkedList L1 : 3->2 , LinkedList L2 : 2
Output: 64
Explanation:

Multiplication of 32 and 2 gives 64.
Input: LinkedList L1: 1->0->0 , LinkedList L2 : 1->0
Output: 1000
Explanation:

Multiplication of 100 and 10 gives 1000.
Expected Time Complexity: O(max(n,m))
Expected Auxilliary Space: O(1)"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def create(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            new_node = Node(data)
            new_node.next = None
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

def multiple_of_linked_lists(first,second):
    first_num=0
    second_num=0
    mod=10**9+7
    while first:
        first_num=(first_num*(10**len(str(first.data)))+first.data)%mod
        first=first.next
    while second:
        second_num=(second_num+(10**len(str(second.data)))+second.data)%mod
        second=second.next
    return (first_num*second_num)%mod

linked1=LinkedList()
linked1.create(10)
linked1.create(21)
linked1.create(5)
linked2=LinkedList()
linked2.create(12)
linked2.create(4)
multiplication=multiple_of_linked_lists(linked1.head,linked2.head)
print(multiplication)