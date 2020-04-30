"""
面试题51. 数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
示例 1:
输入: [7,5,6,4]
输出: 5

我的思想：
暴力求解

优解思想：

收获：

"""

def solution(nums):
    # nums: List[int]
    n = len(nums)
    res = 0
    for i in range(n-1):
        key = nums[i]
        for j in range(i+1, n):
            res += int(key > nums[j])
    return res

    
def excellent():
    pass

if __name__ == '__main__':
    
    print(solution())
