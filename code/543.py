"""
543. 二叉树的直径
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能不穿过根结点。
示例 :
给定二叉树
          1
         / \
        2   3
       / \     
      4   5    
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

我的思想：
求出每个结点的深度，然后求出当前的最大直径

优解思想：

收获：
self.dia比nonlocal dia快
self.depth比在函数内定义占用空间更少

"""

def solution(root: TreeNode):
    # root: TreeNode
    self.dia = 0
    def depth(root):
        if not root:
            return 0
        left = depth(root.left)
        right = depth(root.right)
        self.dia = max(self.dia, left+right)
        return max(left, right) + 1
    depth(root)
    return self.dia
    
def excellent():
    pass

if __name__ == '__main__':
    solution()
