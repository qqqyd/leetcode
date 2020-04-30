"""
312. 戳气球
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
求所能获得硬币的最大数量。
说明:
你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:
输入: [3,1,5,8]
输出: 167 

我的思想：

优解思想：
dp(nums, begin, end)表示nums[begin:end]能得到的最大值，不包含begin和end

收获：

"""

class Solution:
    def solution(self, nums):
        # nums: List[int]
        nums = [1] + nums + [1]
        n = len(nums)
        self.cache = [[0] * n for _ in range(n)]
        return self.dp(nums, 0, n-1)

    def dp(self, nums, begin, end):
        if begin == end - 1:
            return 0
        if self.cache[begin][end] != 0:
            return self.cache[begin][end]
        result = 0
        for i in range(begin+1, end):
            result = max(result, self.dp(nums, begin, i) + self.dp(nums, i, end) + nums[begin] * nums[i] * nums[end])
        self.cache[begin][end] = result
        return result

class Excellent():
    # 同Solution解法，代码简化
    def solution(self, nums):
        # nums: List[int]
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-2, -1, -1):
        # 这里i必须要反序来，相当于先走递归的底层的
            for j in range(i+2, n):
                max_coins = 0
                for k in range(i + 1, j):
                    max_coins = max(max_coins, dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
                dp[i][j] = max_coins

        return dp[0][n - 1]

if __name__ == '__main__':
    nums = [3,1,5,8]
    nums = [3,4,5,6,7,5,7,8,5,3,2,5]
    temp = Solution()
    print(temp.solution(nums))
    temp = Excellent()
    print(temp.solution(nums))
