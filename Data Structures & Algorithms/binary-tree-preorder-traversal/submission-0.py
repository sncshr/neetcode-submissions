# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        retArr=[]
        curr=root
        stck=[]
        while stck or curr:
            if curr:
                retArr.append(curr.val)
                stck.append(curr.right)
                curr=curr.left
            else:
                curr=stck.pop()
        return retArr

        