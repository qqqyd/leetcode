"""
11. 盛最多水的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
示例：
输入：[1,8,6,2,5,4,8,3,7]
输出：49

我的思想：
双指针找就行了

优解思想：

收获：

"""

def solution(height):
    # height: List[int]
    l, r = 0, len(height) - 1
    res = 0
    while l < r:
        res = max(res, min(height[l], height[r]) * (r - l))
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return res


    
def excellent():
    pass

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(solution(height))
