"""
983. 最低票价
在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到 365 的整数。
火车票有三种不同的销售方式：
一张为期一天的通行证售价为 costs[0] 美元；
一张为期七天的通行证售价为 costs[1] 美元；
一张为期三十天的通行证售价为 costs[2] 美元。
通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张为期 7 天的通行证，那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第 5 天、第 6 天、第 7 天和第 8 天。
返回你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费。
示例 1：
输入：days = [1,4,6,7,8,20], costs = [2,7,15]
输出：11

我的思想：
动态规划，前面留30天的缓冲区，res[30]表示第1天，记录当前天的最便宜票价

优解思想：

收获：

"""

def solution(days, costs):
    # days: List[int], costs: List[int]
    res = [0] * (days[-1] + 30)
    dayset = set(days)
    for i in range(30, len(res)):
        res[i] = min(res[i-1]+costs[0], res[i-7]+costs[1], res[i-30]+costs[2]) if i-29 in dayset else res[i-1]

    return res[-1]

def excellent(days, costs):
    from functools import lru_cache
    dayset = set(days)
    durations = [1, 7, 30]

    @lru_cache(None)
    def dp(i):
        if i > 365:
            return 0
        elif i in dayset:
            return min(dp(i + d) + c for c, d in zip(costs, durations))
        else:
            return dp(i + 1)

    return dp(1)

if __name__ == '__main__':
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    print(solution(days, costs))
    print(excellent(days, costs))
