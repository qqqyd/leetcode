"""
945. 使数组唯一的最小增量
给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
返回使 A 中的每个值都是唯一的最少操作次数。
示例 1:
输入：[1,2,2]
输出：1
解释：经过一次 move 操作，数组将变为 [1, 2, 3]。

我的思想：
统计出每个数出现的次数，放入list，两个指针，第一个找要增量的，第二个找目标数，然后他们的差加到结果
要考虑第二个指针超出list范围的情况

优解思想：
直接先找出最终结果的目标list，然后对于排序好的list找每个值的差值

收获：

"""
import collections

def solution(A):
    # A: List[int]result = 0
    if len(A) == len(set(A)):
        return 0
    result = 0
    min_val, max_val = min(A), max(A)
    length = max_val - min_val + 1
    count_table = [0] * length
    for num in A:
        count_table[num-min_val] += 1
    
    j = 0
    for i in range(length):
        while count_table[i] > 1:
            j = max(i, j)
            while j < length and count_table[j] != 0:
                j += 1
            result += j - i
            j += 1
            count_table[i] -= 1
    return result


    
def excellent(A):
    if not A:
        return 0
    A.sort()
    res = 0
    target = 0
    for i in range(len(A)):
        if A[i] < target:
            res += target - A[i]
            target += 1
        else:
            target = A[i] + 1
    return res

if __name__ == '__main__':
    A = [1,2,2]
    A = [3,2,1,2,1,7]
    A = [0, 2, 2]
    A = [13,4,12,5,3,16,11,6,11,0,2,7,19,10,1,15,15,15,11,13]
    
    print(solution(A))
