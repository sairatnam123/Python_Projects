class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class binaryTree:
    def __init__(self):
        self.root=None
    def insert(self,value):
        if self.root is None:
            self.root=Node(value)
        else:
            self.insert_recursive(self.root,value)
    def insert_recursive(self,current,value):
        if value<current.data:
            if current.left is None:
                current.left=Node(value)
            else:
                self.insert_recursive(current.left,value)
        else:
            if current.right is None:
                current.right =Node(value)
            else:
                self.insert_recursive(current.right,value)
    def inorder_traversal(self,node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data,end="->")
            self.inorder_traversal(node.right)
    def pre_order_traversal(self,node):
        if node:
            print(node.data,end="->")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)
    def post_order_traversal(self,node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data,end="->")
    def find(self,value):
        if self.root:
            return self.find_(self.root,value)
    def find_(self,node,val):
        if node is None:
            return None
        if val==node.data:
            return node
        elif node.data>val:
            return self.find_(node.left,val)
        else:
            return self.find_(node.right,val)

tree=binaryTree()
arr=[10,2,13,40,50]
for i in arr:
    tree.insert(i)
tree.inorder_traversal(tree.root)
print()
tree.pre_order_traversal(tree.root)
print()
tree.post_order_traversal(tree.root)
val=tree.find(3)
print()
if val:
    print("value is found",val.data)
else:
    print(val)




