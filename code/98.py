"""
98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:
输入:
    2
   / \
  1   3
输出: true

我的思想：
设置上下界，然后递归判断子树

优解思想：
中序遍历，当前访问的节点的值是不能<=上一个访问的节点的

收获：
对于二叉搜索树，中序遍历访问时，上一个访问节点值肯定大于当前节点值

"""

class Solution:
    def isValid(self, node: TreeNode, val_low, val_high):
        if not node:
            return True
        val = node.val
        if val <= val_low or val >= val_high:
            return False
        if not self.isValid(node.left, val_low, val):
            return False
        if not self.isValid(node.right, val, val_high):
            return False
        return True
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, float('-inf'), float('inf'))
    
def excellent(root):
    stack = []
    pre = float('-inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val <= pre:
            return False
        pre = root.val
        root = root.right
    return True

if __name__ == '__main__':
    
    print(solution())
