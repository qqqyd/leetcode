"""
169. 多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1:
输入: [3,2,3]
输出: 3

我的思想：
创建一个hashmap统计每个元素出现的次数，其中有一个元素大于n/2时就返回

优解思想：
排序后中间的数一定为众数，也不好说这个方法一定更优

收获：

"""

def solution(nums):
    # nums: List[int]
    n = len(nums)/2
    hashmap = {}
    for num in nums:
        if num not in hashmap:
            hashmap[num] = 0
        hashmap[num] += 1
        if hashmap[num] > n:
            return num
    
def excellent(nums):
    # nums: List[int]
    nums.sort()
    return nums[len(nums) // 2]


if __name__ == '__main__':
    nums = [2,2,1,1,1,2,2]
    print(solution(nums))
