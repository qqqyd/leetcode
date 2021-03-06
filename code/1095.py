"""
1095. 山脉数组中查找目标值
（这是一个 交互式问题 ）
给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index 值。
如果不存在这样的下标 index，就请返回 -1。
何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：
首先，A.length >= 3
其次，在 0 < i < A.length - 1 条件下，存在 i 使得：
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
你将 不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：
MountainArray.get(k) - 会返回数组中索引为k 的元素（下标从 0 开始）
MountainArray.length() - 会返回该数组的长度
注意：
对 MountainArray.get 发起超过 100 次调用的提交将被视为错误答案。此外，任何试图规避判题系统的解决方案都将会导致比赛资格被取消。
为了帮助大家更好地理解交互式问题，我们准备了一个样例 “答案”：https://leetcode-cn.com/playground/RKhe3ave，请注意这 不是一个正确答案。
示例 1：
输入：array = [1,2,3,4,5,3,1], target = 3
输出：2
解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2

我的思想：
先找到峰值，然后对两个区间分别二分查找

优解思想：
思想相同，但在做二分查找的时候代码更优化

收获：

"""

def solution(target, mountain_arr):
    # target: int, mountain_arr: 'MountainArray'
    n = mountain_arr.length()
    l, r = 0, n-1
    while l < r:
        peak = (l+r)//2
        temp = mountain_arr.get(peak)
        lval, rval = mountain_arr.get(peak-1), mountain_arr.get(peak+1)
        if lval < temp and rval < temp:
            break
        elif lval > temp:
            r = peak
        else:
            l = peak

    region = [(0, peak), (peak, n-1)]
    for i, (l, r) in enumerate(region):
        while l < r:
            mid = (l+r)//2
            temp = mountain_arr.get(mid)
            if temp == target:
                return mid
            if target < temp ^ i == 0:
                r = mid
            else:
                l = mid
    return -1
    
def excellent(target, mountain_arr):
    def binary_search(mountain, target, l, r, key=lambda x: x):
        target = key(target)
        while l <= r:
            mid = (l + r) // 2
            cur = key(mountain.get(mid))
            if cur == target:
                return mid
            elif cur < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
        
    n = mountain_arr.length()
    l, r = 0, n-1
    while l < r:
        mid = (l+r) >> 1
        if mountain_arr.get(mid) < mountain_arr.get(mid+1):
            l = mid + 1
        else:
            r = mid
    peak = l
    index = binary_search(mountain_arr, target, 0, peak)
    if index != -1:
        return index
    index = binary_search(mountain_arr, target, peak + 1, mountain_arr.length() - 1, lambda x: -x)
    return index

if __name__ == '__main__':
    
    print(solution())
