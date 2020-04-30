"""
229. 求众数 II
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例:
输入: [1,1,1,3,3,2,2,2]
输出: [1,2]

我的思想：
创建一个hashmap统计每个元素出现的次数，找出大于n/3的元素

优解思想：
摩尔投票算法，感觉也不一定更优，因为有一个nums.count，这个如果要自己实现，也是要遍历一遍数组的

收获：

"""

def solution(nums):
    # nums: List[int]
    n = len(nums)/3
    hashmap = {}
    result = []
    for num in nums:
        if num in result:
            continue
        if num not in hashmap:
            hashmap[num] = 0
        hashmap[num] += 1
        if hashmap[num] > n:
            result.append(num)
            if len(result) == 2:
                    return result
    return result
    
def excellent(nums):
    # nums: List[int]
    # 调用现成的函数，但可以运行很快
    # N = len(nums)
    # ans = []
    # for num in set(nums):
    #     if nums.count(num) > N//3:
    #         ans.append(num)
    #         if len(ans) == 2:
    #             return ans
    # return ans
    n1 = n2 = None
    c1 = c2 = 0
    for num in nums:
        if num == n1:
            c1 += 1
        elif num == n2:
            c2 += 1
        elif c2 == 0:
            n2 , c2 = num ,1
        elif c1 == 0:
            n1 , c1 = num ,1
        else:
            c1 , c2 = c1-1 , c2-1
    
    return [n for n in (n1, n2) if nums.count(n) > len(nums)/3]


if __name__ == '__main__':
    nums = [1,1,1,3,3,2,2,2,2,2,2,2]
    print(excellent(nums))
