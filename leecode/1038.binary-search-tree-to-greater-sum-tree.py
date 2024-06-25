#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0

        self.traverse(root)

        return root

    def traverse(self, node: TreeNode):
        if not node:
            return
        # Traverse the right subtree
        if node.right:
            self.traverse(node.right)

        # Update the value and the running sum
        self.sum += node.val
        node.val = self.sum

        # Traverse the left subtree

        if node.left:
            self.traverse(node.left)

        # @lc code=end
