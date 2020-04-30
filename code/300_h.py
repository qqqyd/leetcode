"""
300. 最长上升子序列
给定一个无序的整数数组，找到其中最长上升子序列的长度。
示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

我的思想：
找到目前为止最大的值，新元素和每个之前的元素比

优解思想：
动态规划 + 二分查找
tails[k]的值代表长度为k+1子序列的尾部元素值。

收获：

"""

def solution(nums):
    # nums: List[int]
    candidate = {i: 1 for i in nums}
    for i in range(len(nums)):
        for j in range(i):
            num = nums[i]
            key = nums[j]
            if num > key:
                candidate[num] = max(candidate[key] + 1, candidate[num])

    return max(candidate.values()) if nums else 0



def excellent(nums):
    # nums: List[int]
    tails, res = [0] * len(nums), 0
    for num in nums:
        i, j = 0, res
        while i < j:
            m = (i + j) // 2
            if tails[m] < num:
                i = m + 1
            else:
                j = m
        tails[i] = num
        if j == res:
            res += 1
    return res


if __name__ == '__main__':
    # nums = [10,9,2,5,3,7,101,18]
    nums = [1,3,6,7,9,4,10,5,6]
    # nums = [3,2,1]
    print(solution(nums))
