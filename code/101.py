"""


我的思想：
层序遍历

优解思想：
递归判断左右子树是否都为镜像

收获：
二叉树的问题很多都是递归判断的，这种问题可以多往递归上想
取数组倒数第n个元素可以直接用a[~n]
队列的操作可以在外层循环用range(len(queue))，这样就不用再建一个临时队列了
"""

def solution(root):
    # root: TreeNode
    if not root:
        return True

    def check(a):
        for i in range(len(a) // 2):
            if a[i] != a[~i]:
                return False
        return True

    from collections import deque
    q = deque([root])
    while q:
        t = []
        for _ in range(len(q)):
            node = q.popleft()
            if node:
                t.append(node.val)
                q.extend([node.left, node.right])
            else:
                t.append("")
        if not check(t):
            return False
    return True
    
    
def excellent():
    def Sym_Tree(a, b):
        if not a and not b: return True
        if not a or not b: return False
        return a.val == b.val and Sym_Tree(a.left, b.right) and Sym_Tree(a.right, b.left)

    if not root:
        return True
    return Sym_Tree(root.left, root.right)

if __name__ == '__main__':
    
    print(solution())
