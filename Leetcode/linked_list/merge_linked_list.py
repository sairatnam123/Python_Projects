class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next


def merge_linked_list(list1, list2):
    dummy = Node(0)
    current = dummy
    head1 = list1.head
    head2 = list2.head
    while head1 and head2:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    # Append the remaining elements of either list
    if head1:
        current.next = head1
    if head2:
        current.next = head2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list


linked1 = LinkedList()
linked1.append(1)
linked1.append(2)
linked1.append(4)


linked2 = LinkedList()
linked2.append(1)
linked2.append(3)
linked2.append(4)


merged_list = merge_linked_list(linked1, linked2)


merged_list.print_list()
