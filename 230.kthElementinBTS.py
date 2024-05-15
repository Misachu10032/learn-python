
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    array=[]
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      
        self.inorder(root)
        return self.array[k-1]
        
    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        self.array.append(root.val)
        self.inorder(root.right)

