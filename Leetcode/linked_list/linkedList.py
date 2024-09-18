class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self,data):
        new_node=Node(data)
        new_node.next=None
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    def insert_at_position(self,data,position):
        new_node=Node(data)
        position_node=self.head
        count=0
        previous_node=self.head
        while position_node:
            count=count+1
            previous_node = position_node
            position_node = position_node.next
            if position==count:
                break
        previous_node.next=new_node
        new_node.next=position_node
    def delete_at_beginning(self):
        if self.head is None:
            return ''
        head=self.head.next
        self.head.next=None
        self.head=head
    def delete_at_position(self,position):
        if self.head is None:
            return ''
        current_node=self.head
        previous_node=self.head
        count=0
        while current_node is not None:
            count=count+1
            previous_node=current_node
            current_node=current_node.next
            if count==position-1:
                break
        previous_node.next=current_node.next
        current_node.next=None
    def deletion_at_ending(self):
        if self.head is None:
            return ''
        current_node=self.head
        while current_node.next.next is not None:
            current_node=current_node.next
        current_node.next=None
    def traversal(self):
        traversal=self.head
        while traversal:
            print(traversal.data,end=" ")
            traversal=traversal.next
    def reverse_traverse(self):
        current_position=self.head
        prev_position=None
        while current_position is not None:
            next_node=current_position.next
            current_position.next=prev_position
            prev_position=current_position
            current_position=next_node
        self.head=prev_position
obj=LinkedList()
obj.insert_at_beginning(2)
obj.insert_at_beginning(3)
obj.insert_at_end(4)
obj.insert_at_beginning(11)
obj.insert_at_end(12)
obj.insert_at_beginning(13)
obj.insert_at_end(14)
obj.insert_at_position(6,1)
obj.traversal()
print("\n")
obj.delete_at_beginning()
obj.traversal()
print("\n")
obj.deletion_at_ending()
obj.traversal()
print("\n")
obj.delete_at_position(2)
obj.traversal()
print("\n")
obj.reverse_traverse()
obj.traversal()



