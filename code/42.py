"""
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

我的思想：
从左至右，每次找到当前位置左边和右边的最大值，然后计算出当前点蓄水量

优解思想：
该位置蓄水量仅由左右的小值决定，用双指针，只移动较小那边的指针就行

收获：

"""

def solution(height):
    # height: List[int]
    if not height:
        return 0
    res = 0
    l = len(height)
    max_left = 0
    max_right = max(height)
    for i in range(1, l-1):
        if height[i-1] > max_left:
            max_left = height[i-1]
        if max_right == height[i-1]:
            max_right = max(height[i:])
        res += max(0, min(max_left, max_right) - height[i])
        # print(i, min(max_left, max_right) - height[i], max_left, max_right ,res)
    return res

    
def excellent(height):
    res = 0
    left = left_max = 0
    right = right_max = len(height) - 1
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                res += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                res += right_max - height[right]
            right -= 1
        # 另一种写法
        # if height[left] < height[right]:
        #     left_max = max(left_max, height[left])
        #     res += left_max - height[left]
        #     left += 1
        # else:
        #     right_max = max(right_max, height[right])
        #     res += right_max - height[right]
        #     right -= 1
    return res


if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [2, 0, 2]
    print(solution(height))
