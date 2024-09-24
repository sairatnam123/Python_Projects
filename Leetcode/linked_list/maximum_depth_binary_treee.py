"""
 Given the root of a binary tree, return its maximum depth.
 A binary tree's maximum depth is the number of nodes along the
 longest path from the root node down to the farthest leaf node.
"""

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
def depth_of_tree(node):
    if node is None:
        return 0
    else:
        left_depth=depth_of_tree(node.left)
        right_depth=depth_of_tree(node.right)
        return max(left_depth,right_depth)+1

node1=Binary_tree()
node1.insert_element(5)
node1.insert_element(10)
node1.insert_element(3)
node1.insert_element(8)
node1.insert_element(12)
node1.pre_order_traversal(node1.root)

print("\nmaximum depth of a tree",depth_of_tree(node1.root))