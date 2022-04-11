"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        output = []
        flag,temp = 0,0
        def postOrder(root,level):
            nonlocal output,flag,temp
            if root:
                if flag == 0 and level>temp:
                    root.next = Node('#')
                    temp = level
                if root.right or root.left:
                    flag = 0
                else:
                    flag = 1
                postOrder(root.right,level+1)
                postOrder(root.left,level+1)
        postOrder(root,1) 
        
        def levelOrder(root):
            nonlocal output
            if root is None:
                return
            queue = []

            queue.append(root)

            while(len(queue) > 0):
                
                output.append(queue[0])
                node = queue.pop(0)
            
                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)
                
        levelOrder(root)
        for i in range(len(output)):
            if output[i].next:
                if output[i].next.val == '#':
                    output[i].next = None
            else:
                output[i].next = output[i+1]

        return root
        
        
        
        
        