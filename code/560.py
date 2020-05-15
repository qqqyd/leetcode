"""
560. 和为K的子数组
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
示例 1 :
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

我的思想：
每次都记录当前前缀和，并在hashmap中查找是否有与k的差的前缀和

优解思想：

收获：

"""

def solution(nums, k):
    # nums: List[int], k: int
    hashmap = collections.defaultdict(int)
    hashmap[0] = 1
    cur_sum = 0
    res = 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        if cur_sum - k in hashmap:
            res += hashmap[cur_sum - k]
        hashmap[cur_sum] += 1
    return res
    
def excellent():
    pass

if __name__ == '__main__':
    nums = [1,1,1]
    k = 2
    print(solution(nums, k))
