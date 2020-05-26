"""
287. 寻找重复数
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
示例 1:
输入: [1,3,4,2,2]
输出: 2
示例 2:
输入: [3,1,3,4,2]
输出: 3

我的思想：
二分查找
因为数组是1到n均匀分布的，仅有一个数重复，所以找到哪个区间的值大于该数就可以

优解思想：
快慢指针
访问下标顺序为i -> nums[i]，快指针一次两格，慢指针一格，直到相遇。然后把慢指针移到0，再次相遇即为答案。

解释为什么要移到0了再相遇：
假设环长为L，从起点到环的入口的步数是a，从环的入口继续走b步到达相遇位置，从相遇位置继续走c步回到环的入口，有b+c=L。
相遇时，慢指针走了a+b步，快指针走了2(a+b)步，也为a+b+kL，即a = kL-b = (k-1)L+c。
从上述等式可知，慢指针从起点出发，快指针从相遇位置出发，每次两个指针都移动一步，则慢指针走了a步之后到达环的入口，
快指针在环里走了k−1圈之后又走了c步，由于从相遇位置继续走c步即可回到环的入口，因此快指针也到达环的入口。两个指针在环的入口相遇，相遇点就是答案。

收获：

"""

def solution(nums):
    # nums: List[int]
    l, r = 1, len(nums) - 1

    while l < r:
        # m = l + (r - l) // 2
        mid = (l + r) // 2

        cnt = 0
        for num in nums:
            cnt += int(num <= mid)

        if cnt > mid:
            r = mid
        else:
            l = mid + 1

    return l

    
def excellent(nums):
    fast, slow = 0, 0
    while True:
        fast = nums[nums[fast]]
        slow = nums[slow]
        if slow == fast:
            slow = 0
            while nums[fast] != nums[slow]:
                slow = nums[slow]
                fast = nums[fast]
            return nums[fast]

if __name__ == '__main__':
    nums = [1,3,4,2,2]
    print(solution(nums))
