# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        node=root
        parent=None
        while node:
            if node.val==key:
                break
            elif node.val>key:
                parent=node
                node=node.left
            else:
                parent=node
                node=node.right
        if not node:
            return root


        if not node.left and not node.right:
            if not parent:
                return None
            if node==parent.left:
                parent.left=None
                del node
            else:
                parent.right=None
                del node
        elif not node.left or not node.right:
            child = node.left if node.left else node.right
            if not parent:
                return child
            if parent.left==node:
                parent.left=child
            else:
                parent.right=child
        else:
            succParent=node
            succ=node.right
            while succ.left:
                succParent=succ
                succ=succ.left
            node.val=succ.val
            child= succ.right
            if succParent.left==succ:
                succParent.left=child
            else:
                succParent.right=child
        return root


        
        