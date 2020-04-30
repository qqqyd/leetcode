"""
面试题 08.11. 硬币
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)
示例1:
 输入: n = 5
 输出：2
 解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1
示例2:
 输入: n = 10
 输出：4
 解释: 有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1

我的思想：
动态规划

优解思想：
数学方法

收获：

"""

def solution(n):
    # n: int
    mod = 10**9 + 7
    coins = [25, 10, 5, 1]
    # n分面值有f[n]种表示方法
    f = [1] + [0] * n
    for coin in coins:
        for i in range(coin, n + 1):
            f[i] += f[i - coin]
    return f[n] % mod

    
def excellent(n):
    mod = 10**9 + 7

    ans = 0
    for i in range(n // 25 + 1):
        rest = n - i * 25
        a, b = rest // 10, rest % 10 // 5
        ans += (a + 1) * (a + b + 1)
    return ans % mod

if __name__ == '__main__':
    n = 5
    print(solution(n))
