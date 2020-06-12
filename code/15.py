"""
15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

我的思想：
排序，双指针
这个代码有问题，不能消除重复的元素

优解思想：
也是双指针，加入了对重复元素的处理

收获：

"""

def solution(nums):
    # nums: List[int]
    n = len(nums)
    res = []
    nums.sort()
    i, j = 0, n-1
    while i < j - 1:
        temp = nums[i] + nums[j]
        if temp + nums[i+1] == 0:
            res.append([nums[i], nums[i+1], nums[j]])
            i += 1
            continue
        if temp + nums[j-1] == 0:
            res.append([nums[i], nums[j-1], nums[j]])
            j -= 1
            continue
        if temp + nums[i+1] < 0:
            i += 1
        else:
            j -= 1
    return res
    
def excellent():
    nums.sort()
    n = len(nums)
    res = []

    for k in range(n - 2):
        if nums[k] > 0:
            return res
        if k > 0 and nums[k] == nums[k - 1]:
            continue

        i, j = k + 1, n - 1
        while i < j:
            s = nums[k] + nums[i] + nums[j]
            if s < 0:
                i += 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
            elif s > 0:
                j -= 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
            else:
                res.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
    return res

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(solution(nums))
