"""
239. 滑动窗口最大值
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。
示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 

我的思想：
暴力求解

优解思想：
双向操作，将原数组分成若干个长度为k的block。
全在一个block时，直接从左到右，就得到了最大的值
从左到右操作时，可以得到该block中，到目前位置最大的值，同理从右到左就得到到目前位置最大的值，两者取最大值就行

收获：

"""

def solution(nums, k):
    #  nums: List[int], k: int
    if nums:
        return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]
    return []

def excellent():
    n = len(nums)
    if n * k == 0:
        return []
    if k == 1:
        return nums
    
    left = [0] * n
    left[0] = nums[0]
    right = [0] * n
    right[n - 1] = nums[n - 1]
    for i in range(1, n):
        # 从左到右
        if i % k == 0:
            left[i] = nums[i]
        else:
            left[i] = max(left[i - 1], nums[i])
        # 从右到左
        j = n - i - 1
        if (j + 1) % k == 0:
            right[j] = nums[j]
        else:
            right[j] = max(right[j + 1], nums[j])
    
    output = []
    for i in range(n - k + 1):
        output.append(max(left[i + k - 1], right[i]))
        
    return output

if __name__ == '__main__':
    solution()
