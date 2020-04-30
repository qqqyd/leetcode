"""
1013. 将数组分成和相等的三个部分
给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。
示例 1：
输出：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

我的思想：
先找出平均数，三部分的和应该都为这个平均数，如果平均数非整，直接false
然后从第一部分开始往后遍历找，和为平均数再找下一部分

优解思想：
我有考虑第一部分在第一次和为ave的时候，后面的部分可能组不成有效解的情况，但实际情况是，只要第一部分的和为ave，就可以确认他肯定是其中之一了
这样做可以减少一些临时变量

收获：

"""

def solution(A):
    n = len(A)
    ave = sum(A) / 3
    if int(ave) != ave:
        return False

    sum1 = 0
    for i in range(n-2):
        sum1 += A[i]
        if sum1 != ave:
            continue
        sum2 = 0
        for j in range(i+1, n-1):
            sum2 += A[j]
            if sum2 != ave:
                continue
            return True
    return False
    
def excellent(A):
    ave = sum(A) / 3
    if int(ave) != ave:
        return False
    tot = 0
    k = 0
    for num in A:
        tot += num
        if tot == ave:
            tot = 0
            k += 1
            if k == 3:
                return True
    return False

if __name__ == '__main__':
    A = [0,2,1,-6,6,-7,9,1,2,0,1]
    # print(solution(A))
    print(excellent(A))
