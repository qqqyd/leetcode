"""
236. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

我的思想：
别人的解法
递归往下找，子节点为所需的，即返回其值；无所需的返回空

优解思想：

收获：

"""

def solution(root, p, q):
    # root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    if not root or root == p or root == q:
        return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    if not left:
        return right
    if not right:
        return left
    return root
    
def excellent():
    pass

if __name__ == '__main__':
    
    print(solution())
