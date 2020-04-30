"""
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

我的思想：
深度优先搜索。res_t记录当前的结果，nums_t记录当前的可遍历数组

优解思想：
也是使用的深度优先。没有使用更多的空间，原地交换数组元素

收获：
nums和nums[:]的值虽然是一样的，但是其意义不一样。nums是浅复制，原数组改变其值也会变

"""

def solution(nums):
    # nums: List[int]
    res = []
    def dfs(res_t, nums_t):
        if not nums_t:
            res.append(res_t)
        for i, num in enumerate(nums_t):
            dfs(res_t + [num], nums_t[:i] + nums_t[i+1:])
    dfs([], nums)

    return res

    
def excellent(nums):
    n = len(nums)
    res = []

    def backtrack(first = 0):
        if first == n:
            # 这里不能写nums
            res.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]
    
    backtrack()
    return res

if __name__ == '__main__':
    nums = [1,2,3]
    # print(solution(nums))
    print(excellent(nums))
