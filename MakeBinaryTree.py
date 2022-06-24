# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def insert(self, data):
        if self.val is None:
            self.val=data
            return
        if self.left is None:
            if self.left:
                self.left.insert(data)
            else:
                self.left=TreeNode(data)
        elif self.right is None:
            if self.right:
                self.right.insert(data)
            else:
                self.right=TreeNode(data)
            
            
    #     if self.val:           
    #         if self.left is None:
    #             self.left = TreeNode(data)
    #         elif self.right is None:
    #             self.right = TreeNode(data)
    #         else:
    #             self.left.insert(data)
    #     else:
    #         self.val = data
    # def PrintTree(self):
    #     if self.left:
    #         self.left.PrintTree()
    #     print(self.val),
    #     if self.right:
    #         self.right.PrintTree()
#%%
# Driver code
root = TreeNode(7)
root.insert(4)
root.insert(3)
root.insert(6)


# root.PrintTree()