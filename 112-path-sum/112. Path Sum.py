# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        currSum = targetSum - root.val
        ans = False

        if root.left == None and root.right == None and currSum == 0:
            return True

        if root.left:
            ans = ans or self.hasPathSum(root.left, currSum)
        if root.right:
            ans = ans or self.hasPathSum(root.right, currSum)
        
        return ans
            