# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        stck=[root]
        visit=set()
        parents={root: None}
        while stck:
            node=stck.pop()
            if not node.left and not node.right:
                if node.val==target:
                    p=parents[node]
                    if not p:
                        return None
                    if p.left==node:
                        p.left=None
                    if p.right==node:
                        p.right=None
            elif node not in visit:
                visit.add(node)
                stck.append(node)
                if node.left:
                    stck.append(node.left)
                    parents[node.left]=node
                if node.right:
                    stck.append(node.right)
                    parents[node.right]=node
        return root
        