"""
面试题 17.16. 按摩师
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。
注意：本题相对原题稍作改动
示例 1：
输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。

我的思想：
动态规划，dp0[i]是前i个不接第i个的最大值，dp1[i]是前i个接第i个的最大值
dp0[i] = max(dp0[i-1], dp1[i-1])
dp1[i] = dp0[i-1] + nums[i]

优解思想：

收获：

"""

def solution(nums):
    # nums: List[int]
    n = len(nums)
    if n == 0:
        return 0

    dp0, dp1 = 0, nums[0]
    for i in range(1, n):
        dp0, dp1 = max(dp0, dp1), dp0 + nums[i]
    
    return max(dp0, dp1)

    
def excellent():
    pass

if __name__ == '__main__':
    
    print(solution())
