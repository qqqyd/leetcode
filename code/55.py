"""
55. 跳跃游戏
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。
示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

我的思想：
记录当前能到达的最大位置，然后遍历所有点，如果当前点位置大于最大位置则False，每次更新最大位置

优解思想：
优化代码

收获：

"""

def solution(nums):
    # nums: List[int]
    cur_max = 0
    for idx, val in enumerate(nums):
        if idx > cur_max:
            return False
        cur_max = max(cur_max, idx + val)
    return True
    
def excellent(nums):
    cur_max = 0

    for i, x in enumerate(nums):
        if i + x >= cur_max and i <= cur_max:
            cur_max = i + x
    return cur_max >= i

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    nums = [3,2,1,0,4]
    print(solution(nums))
