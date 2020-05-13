"""
102. 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[[3],[9,20],[15,7]]

我的思想：
使用队列，每次加入该层所有结点

优解思想：

收获：

"""

def solution(root):
    # root: TreeNode
    res = []
    queue = [root]
    while True:
        sub_res = []
        next_queue = []
        while queue:
            node = queue.pop(0)
            if not node:
                continue
            sub_res.append(node.val)
            next_queue.append(node.left)
            next_queue.append(node.right)
        if not next_queue:
            return res
        res.append(sub_res)
        queue = next_queue
    
def excellent():
    pass

if __name__ == '__main__':
    
    print(solution())
