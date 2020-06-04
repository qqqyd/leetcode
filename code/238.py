"""
238. 除自身以外数组的乘积
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
示例:
输入: [1,2,3,4]
输出: [24,12,8,6]

我的思想：
维护两个数组，分别表示从左到右和从右到左的乘积

优解思想：
空间复杂度优化

收获：

"""

def solution(nums):
    # nums: List[int]
    n = len(nums)
    l, r = [1] * n, [1] * n
    for i in range(1, n):
        l[i] = l[i-1] * nums[i-1]
        r[~i] = r[~i+1] * nums[~i+1]
    return [l[i] * r[i] for i in range(n)]
    
def excellent(nums):
    n = len(nums)
    res = [1] * n
    for i in range(1, n):
        res[i] = res[i-1] * nums[i-1]
    r = 1
    for i in range(n-1, -1, -1):
        res[i] *= r
        r *= nums[i]
    return res

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(solution(nums))
    print(excellent(nums))
