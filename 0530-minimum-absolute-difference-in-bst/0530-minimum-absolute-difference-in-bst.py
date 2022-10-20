# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root, low, high):
            
            if root == None:
                return high - low
            
            left = traverse(root.left, low, root.val)
            right = traverse(root.right, root.val, high)
            
            return min(left, right)
        
        return traverse(root, float('-inf'), float('inf'))