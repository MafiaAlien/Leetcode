# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # did not find the key value in tree
        # find the node value which equal to key value:
        #       leaf:
        #       parents: 
        #           1. left and not right -> parent point to left child;
        #           2. not left and right -> same method as above one;
        #           3. left and right -> both left and right child can be parent to previous parent 
        #           if selecting right child as new parent, then left pre parent point to right child 
        #           and put left child leaf to new parent node(pre right)'s left leaf's left as child
        #           to make sure that the value is on the right leaf node;
        #           4. not left and not right -> return None, which assign None value to previous node
        if not root:
            return None 
        
        if root.val == key:
            if not root.left and not root.right:
                return None 
            elif root.left and not root.right:
                return root.left  
            elif not root.left and root.right:
                return root.right 
            else:
                # pointer to current node 
                cur = root.right 
                while cur.left:
                    # find the value that closest to key value(smaller than) by iteration
                    cur = cur.left 
                else:
                    # if current node's left child is None, assign cur's left child by target node' left 
                    cur.left = root.left 
                return root.right 
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root 
        