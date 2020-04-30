"""
322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1

我的思想：
这就是经典的动态规划问题，可以尝试深度/广度优先的算法
完全背包问题，但是我没搞太清楚
代码也是人家的代码
dp(n)=  0,n=0
        −1,n<0
        min(dp(n−coin)+1∣coin∈coins),n>0

加入备忘录记录已经计算过的dp(n)可以适当减少


优解思想：
DFS+剪枝

收获：
递归太不熟悉了
对于递归的操作，要先找出递推关系式

"""

def solution(coins, amount):
    # coins: List[int], amount: int
    # 对于amount的价值，最少需要dp(amount)个硬币
    def dp(n):
        if n ==0:
            return 0
        elif n < 0:
            return -1
        res = amount + 1
        for coin in coins:
            temp = dp(n - coin)
            if temp == -1:
                continue
            res = min(res, temp + 1)

        return -1 if res == amount + 1 else res


    return dp(amount)
    
def excellent(coins, amount):
    from math import ceil
    coins = sorted(coins, reverse = True)
    # res即为最小硬币数
    res = amount + 1

    def dfs(index, target, count):
        nonlocal res
        this_coin = coins[index]
        # 先丢最大的硬币
        if count + ceil(target / this_coin) >= res:
            return
        # 用当前最大的硬币组成
        if target % this_coin == 0:
            res = count + target // this_coin

        if index == len(coins) - 1:
            return
        # 遍历搜索
        for i in range(target // this_coin, -1 , -1):
            dfs(index + 1, target - i * this_coin, count + i)
    
    dfs(0, amount, 0)
    return -1 if res == amount + 1 else res

if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11
    # print(solution(coins, amount))
    print(excellent(coins, amount))
