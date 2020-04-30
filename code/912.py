"""
912. 排序数组
给定一个整数数组 nums，将该数组升序排列。
示例 1：
输入：[5,2,3,1]
输出：[1,2,3,5]

我的思想：
排序

优解思想：

收获：

"""
import random

def randomized_quicksort(nums, l, r):
    if r <= l:
        return
    mid = randomized_partition(nums, l, r)
    randomized_quicksort(nums, l, mid - 1)
    randomized_quicksort(nums, mid + 1, r)

def randomized_partition(nums, l, r):
    pivot = random.randint(l, r)
    nums[pivot], nums[r] = nums[r], nums[pivot]
    i = l
    for j in range(l, r):
        if nums[j] < nums[r]:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i

def solution(nums):
    # nums: List[int]
    randomized_quicksort(nums, 0, len(nums) - 1)
    return nums

    
def excellent():
    pass

if __name__ == '__main__':
    nums = [5,2,3,1]
    print(solution(nums))
