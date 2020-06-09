"""
面试题46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

我的思想：
动态规划
dp[i]表示前i个数字能翻译的种类数量，若后两位能一起翻译，则dp[i] = dp[i-1] + dp[i-2]，若不能，则dp[i] = dp[i-1]。dp[0] = dp[1] = 1

优解思想：
思想相同，优化代码
这个问题有对称性，从左到右和从右到左是一样的结果

收获：

"""

def solution(num):
    # num: int
    num = str(num)
    n = len(num)
    dp = [1] * (n + 1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2] * int('10' <= num[i-2: i] <= '25')
    return dp[n]

    
def excellent(num):
    # 字符串操作
    # s = str(num)
    # a = b = 1
    # for i in range(2, len(s)+1):
    #     a, b = (a + b if '10' <= s[i-2: i] <= '25' else a), a
    # return a

    # 数字求余
    a = b = 1
    y = num % 10
    while num != 0:
        num //= 10
        x = num % 10
        a, b = (a + b if 10 <= 10 * x + y <= 25 else a), a
        y = x
    return a

if __name__ == '__main__':
    num = 12258
    print(solution(num))
