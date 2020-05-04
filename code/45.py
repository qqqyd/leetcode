"""
45. 跳跃游戏 II
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
示例:
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:
假设你总是可以到达数组的最后一个位置。

我的思想：
记录到达每个点的最小值

优解思想：
记录当前能到达的最远位置，作为更新跳跃次数的边界位置，在走到当前最远位置之前，不断更新最远位置

收获：
我的方法相当于是动态规划，最终会超时，这里用贪心算法

"""

def solution(nums):
    # nums: List[int]
    n = len(nums)
    res = [999999] * n
    res[0] = 0
    for idx, val in enumerate(nums):
        for i in range(idx + 1, min(idx + val + 1, n)):
            res[i] = min(res[idx] + 1, res[i])

    return res[n-1]
    
def excellent(nums):
    n = len(nums)
    maxPos = 0
    broad = 0
    res = 0
    for i in range(n - 1):
        maxPos = max(maxPos, i + nums[i])
        if i == broad:
            broad = maxPos
            res += 1
        print(maxPos, broad, res)
    return res

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    print(solution(nums))
    print(excellent(nums))
