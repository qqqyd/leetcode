"""
136. 只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,1]
输出: 1

我的思想：
所有数做异或，即可得到最终答案

优解思想：
思想相同，代码更简单

收获：

"""

def solution(nums):
    # nums: List[int]
    res = 0
    for num in nums:
        res ^= num
    return res
    
def excellent(nums):
    return reduce(lambda x, y: x ^ y, nums)

if __name__ == '__main__':
    nums = [4,1,2,1,2]
    print(solution(nums))
