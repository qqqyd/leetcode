"""
面试题56 - I. 数组中数字出现的次数
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
示例 1：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

我的思想：
建立hashmap来存储

优解思想：
对所有数做异或，可以得到出现一次的两个数异或的结果。随便找为1的一位，讲所有数分两组，对两组中的所有数做异或，得到最终结果。

收获：


"""

def solution(nums):
    # nums: List[int]
    hashmap = {}
    for item in nums:
        if item in hashmap:
            hashmap.pop(item)
        else:
            hashmap[item] = 1
    return list(hashmap.keys())

    
def excellent(nums):
    import functools
    ret = functools.reduce(lambda x, y: x ^ y, nums)
    print(ret)
    div = 1
    while div & ret == 0:
        div <<= 1
    print(div)
    a, b = 0, 0
    for n in nums:
        if n & div:
            a ^= n
        else:
            b ^= n
    return [a, b]

if __name__ == '__main__':
    nums = [4,1,4,6]
    print(solution(nums))
    print('-' * 30)
    print(excellent(nums))
