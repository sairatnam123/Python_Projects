class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# Floyd’s Tortoise & Hare Algorithm
def has_cycle(head):
    slow=head
    fast=head
    while slow.next is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        if slow == fast:
            return  "true"
    return "false"

node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)
node.next.next.next.next.next = node.next.next

has_cycle(node)
