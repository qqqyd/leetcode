"""
199. 二叉树的右视图
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
示例:
输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

我的思想：
对树进行遍历，可以选择深度或者广度遍历，分别对应栈和队列，然后记录每一层最右边的就行

优解思想：

收获：

"""

def solution(root):
    # root
    rightmost_value_at_depth = {}
    max_depth = -1

    stack = [(root, 0)]
    while stack:
        node, depth = stack.pop()

        if node is not None:
            max_depth = max(max_depth, depth)
            rightmost_value_at_depth.setdefault(depth, node.val)
            # 队列情况，因为是最后才访问最右的
            # rightmost_value_at_depth[depth] = node.val
            stack.append((node.left, depth+1))
            stack.append((node.right, depth+1))

    return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]
    
def excellent():
    pass

if __name__ == '__main__':
    
    print(solution())
