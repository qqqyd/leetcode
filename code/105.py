"""
105. 从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。
注意:
你可以假设树中没有重复的元素。
例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7

我的思想：
别人的思想
分治的思想不断构建子树

优解思想：

收获：
二叉树的操作大多是分治思想，一般要定义一个新函数来处理

"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None
            
            # 前序遍历的第一个为root
            preorder_root = preorder_left
            # 定位中序遍历中的root
            inorder_root = index[preorder[preorder_root]]
            
            root = TreeNode(preorder[preorder_root])
            size_left_subtree = inorder_root - inorder_left
            # 构建左子树
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 构建右子树
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root
        
        n = len(preorder)
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)

    
def excellent():
    pass

if __name__ == '__main__':
    
    print(solution())
