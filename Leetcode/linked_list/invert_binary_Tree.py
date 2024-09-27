""" Invert Binary Tree
 Given the root of a binary tree, invert the tree, and return its root.
 Input: root = [4,2,7,1,3,6,9]
 Output: [4,7,2,9,6,3,1]"""
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def insert_(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self.insert_element(data,self.root)
    def insert_element(self,data,node):
        if node.data>data:
            if node.left is None:
                node.left=Node(data)
            else:
                self.insert_element(data,node.left)
        else:
            if node.right is None:
                node.right=Node(data)
            else:
                self.insert_element(data,node.right)
    def in_order(self,node):
        if node:
            self.in_order(node.left)
            print(node.data,end=" ")
            self.in_order(node.right)


def invert_tree(node):
    stack=[node]
    while stack:
        current=stack.pop()
        if  current.left and current.right:
            current.left,current.right=current.right,current.left
            stack.append(current.left)
            stack.append(current.right)
    return node

tree=BinaryTree()
tree.insert_(9)
tree.insert_(15)
tree.insert_(3)
tree.insert_(2)
tree.insert_(5)
tree.insert_(10)
tree.insert_(16)
tree.in_order(tree.root)
print()
print("invert Tree\n")
tree.root=invert_tree(tree.root)
tree.in_order(tree.root)
print()