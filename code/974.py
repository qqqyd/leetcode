"""
974. 和可被 K 整除的子数组
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
示例：
输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

我的思想：
记录每个前缀和对K求余出现的次数

优解思想：
大体思想相同，只是第一遍遍历数组的时候仅记录hashmap，然后用排列组合的思想得到最终结果

收获：
与子数组相关的问题很多要用到前缀和的思想

"""

def solution(A, K):
    # A: List[int], K: int
    record = {0: 1}
    _sum, res = 0, 0
    for num in A:
        _sum += num
        remain = _sum % K
        cnt = record.get(remain, 0)
        res += cnt
        record[remain] = cnt + 1
    return res

    
def excellent():
    record = {0: 1}
    _sum = 0
    for num in A:
        _sum += num
        remain = _sum % K
        record[remain] = record.get(remain, 0) + 1
    
    res = 0
    for x, cx in record.items():
        res += cx * (cx - 1) // 2
    return res

if __name__ == '__main__':
    A = [4,5,0,-2,-3,1]
    K = 5
    print(solution(A, K))
    print(excellent(A, K))
