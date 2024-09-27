"""Given the roots of two binary trees p and q, write a function to
 check if they are the same or not.
 Two binary trees are considered the same if they are structurally
 identical, and the nodes have the same value.
 Input: p = [1,2,3], q = [1,2,3]
 Output: true"""
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Binary_tree:
    def __init__(self):
        self.root=None
    def insert_element(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self.insert_(data,self.root)
    def insert_(self,value,node):
        if value<node.data:
            if node.left is None:
                node.left=Node(value)
            else:
                self.insert_(value,node.left)
        else:
            if node.right is None:
                node.right=Node(value)
            else:
                self.insert_(value,node.right)
    def pre_order_traversal(self,node):
        if node:
            print(node.data,end="->")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)


def are_same_trees(t1,t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t1.data !=t2.data:
        return False
    return are_same_trees(t1.left,t2.left) and are_same_trees(t1.right,t2.right)

tree1=Binary_tree()
tree2=Binary_tree()
tree1.insert_element(1)
tree2.insert_element(1)
tree1.insert_element(2)
tree2.insert_element(2)
tree1.insert_element(3)
tree2.insert_element(3)
print(are_same_trees(tree1.root,tree2.root))