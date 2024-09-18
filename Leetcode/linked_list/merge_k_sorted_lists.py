class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
    def print(self):
        current=self.head
        while current:
            print(current.data,end="- >")
            current=current.next
        print("None")

def merge_linked_k_linkedList(linked_lists):
    elements=[]
    for linked_list in linked_lists:
        current = linked_list.head
        while current:
            elements.append(current.data)
            current=current.next
    elements.sort()
    create_linked_link=LinkedList()
    for  data in elements:
        create_linked_link.append(data)
    return create_linked_link

linked1=LinkedList()
linked1.append(1)
linked1.append(4)
linked1.append(5)
linked2=LinkedList()
linked2.append(1)
linked2.append(3)
linked2.append(4)
linked3=LinkedList()
linked3.append(2)
linked3.append(6)

lists=[linked1,linked2,linked3]
merge_sort=merge_linked_k_linkedList(lists)
merge_sort.print()






