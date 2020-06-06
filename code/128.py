"""
128. 最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。
要求算法的时间复杂度为 O(n)。
示例:
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

我的思想：
遍历每个数，用hash表记录是否访问。找到序列开始的数字，然后找连续的数字是否在数组中

优解思想：

收获：

"""

def solution(nums):
    # nums: int
    res = 0
    hash_map = {}
    for num in nums:
        hash_map[num] = False
    for key in hash_map:
        if hash_map[key]:
            continue
        if key - 1 not in hash_map:
            cur_len = 1
            cur_num = key
            hash_map[cur_num] = True
            while cur_num + 1 in hash_map:
                cur_num += 1
                cur_len += 1
                hash_map[cur_num] = True
            res = max(res, cur_len)
    return res
    
def excellent():
    pass

if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    print(solution(nums))
