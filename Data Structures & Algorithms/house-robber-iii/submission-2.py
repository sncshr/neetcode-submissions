# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stck=[(root, False)]
        dp={None:(0,0)}
        while stck:
            node, visited = stck.pop()
            if not node:
                continue
            if visited:
                left_rob, left_skip=dp[node.left]
                right_rob, right_skip=dp[node.right]
                rob_curr= node.val+left_skip+right_skip
                skip_curr=(max(left_rob,left_skip)+max(right_rob,right_skip))
                dp[node]=(rob_curr,skip_curr)
            else:
                stck.append((node, True))
                stck.append((node.left, False))
                stck.append((node.right, False))
        return max(dp[root])

        