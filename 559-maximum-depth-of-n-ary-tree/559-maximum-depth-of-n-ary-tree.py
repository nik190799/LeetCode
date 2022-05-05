"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        max = 0
        def levelOrder(root,depth):
            nonlocal max 
            if root is None:
                return
            
            depth += 1
            if depth > max:
                max = depth
            i = 0
            while(i< len(root.children)):
                
                levelOrder(root.children[i],depth)
                i += 1
        levelOrder(root,depth)
                
            
        
        return max