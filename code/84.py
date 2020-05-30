"""
84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
示例:
输入: [2,1,5,6,2,3]
输出: 10

我的思想：
别人的思想
通过计算数组每个位置能构成的最大矩形面积，然后求最大值得到结果
left数组表示当前柱左侧第一个小于其高度的位置，right同理

优解思想：
通过减少一次遍历来确定left和right数组

收获：

"""

def solution(heights):
    # heights: List[int]
    n = len(heights)
    left, right = [0] * n, [0] * n

    mono_stack = list()
    for i in range(n):
        while mono_stack and heights[mono_stack[-1]] >= heights[i]:
            mono_stack.pop()
        left[i] = mono_stack[-1] if mono_stack else -1
        mono_stack.append(i)
    
    mono_stack = list()
    for i in range(n - 1, -1, -1):
        while mono_stack and heights[mono_stack[-1]] >= heights[i]:
            mono_stack.pop()
        right[i] = mono_stack[-1] if mono_stack else n
        mono_stack.append(i)
    
    ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
    return ans
    
def excellent(heights):
    n = len(heights)
    left, right = [0] * n, [n] * n

    mono_stack = list()
    for i in range(n):
        while mono_stack and heights[mono_stack[-1]] >= heights[i]:
            right[mono_stack[-1]] = i
            mono_stack.pop()
        left[i] = mono_stack[-1] if mono_stack else -1
        mono_stack.append(i)
    
    ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
    return ans

if __name__ == '__main__':
    
    print(solution())
