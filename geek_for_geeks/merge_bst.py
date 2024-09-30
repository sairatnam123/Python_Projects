# Corrected inorder traversal function
def inorder_traverser(root, result):
    if root is None:
        return
    inorder_traverser(root.left, result)
    result.append(root.data)
    inorder_traverser(root.right, result)

# Function to merge two sorted lists
def merge_lists(list1, list2):
    i = 0
    j = 0
    merge_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merge_list.append(list1[i])
            i += 1
        else:
            merge_list.append(list2[j])
            j += 1
    # Add remaining elements from list1 and list2
    while i < len(list1):
        merge_list.append(list1[i])
        i += 1
    while j < len(list2):
        merge_list.append(list2[j])
        j += 1
    return merge_list

# Solution class with merge function
class Solution:
    def merge(self, root1, root2):
        elements_root1 = []
        elements_root2 = []
        inorder_traverser(root1, elements_root1)
        inorder_traverser(root2, elements_root2)
        merge_result_list = merge_lists(elements_root1, elements_root2)
        return merge_result_list  # No need to call sorted() since the list is already sorted

# Example of TreeNode definition (ensure this exists in your code)
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example trees:
# First BST
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(6)
root1.left.left = TreeNode(2)
root1.left.right = TreeNode(4)

# Second BST
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.right.right = TreeNode(7)
root2.right.right.left = TreeNode(6)

# Create a solution object and merge the BSTs
sol = Solution()
result = sol.merge(root1, root2)
print(result)  # Output: [1, 2, 2, 3, 3, 4, 5, 6, 6, 7]
