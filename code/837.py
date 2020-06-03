"""
837. 新21点
爱丽丝参与一个大致基于纸牌游戏 “21点” 规则的游戏，描述如下：
爱丽丝以 0 分开始，并在她的得分少于 K 分时抽取数字。 抽取时，她从 [1, W] 的范围中随机获得一个整数作为分数进行累计，其中 W 是整数。 每次抽取都是独立的，其结果具有相同的概率。
当爱丽丝获得不少于 K 分时，她就停止抽取数字。 爱丽丝的分数不超过 N 的概率是多少？
示例 1：
输入：N = 10, K = 1, W = 10
输出：1.00000
说明：爱丽丝得到一张卡，然后停止。
示例 2：
输入：N = 6, K = 1, W = 10
输出：0.60000
说明：爱丽丝得到一张卡，然后停止。
在 W = 10 的 6 种可能下，她的得分不超过 N = 6 分。
示例 3：
输入：N = 21, K = 17, W = 10
输出：0.73278

我的思想：
动态规划
dp[x]表示得分为x时获胜的概率，dp[x] = sum(dp[x+1] + ... + dp[x+W]) / W

优解思想：
优化状态转移方程
dp[x] = dp[x+1] - (dp[x+W+1] - dp[x+1]) / W, 0 <= x < K-1
dp[K-1] = sum(dp[K] + ... + dp[K+W-1]) / W

收获：

"""

def solution(N, K, W):
    # N: int, K: int, W: int
    if K == 0:
        return 1.0
    dp = [0.0] * (K + W)
    for i in range(K, min(N, K + W - 1) + 1):
        dp[i] = 1.0
    for i in range(K - 1, -1, -1):
        for j in range(1, W + 1):
            dp[i] += dp[i + j] / W
    return dp[0]
    
def excellent(N, K, W):
    if K == 0:
        return 1.0
    dp = [0.0] * (K + W)
    for i in range(K, min(N, K + W - 1) + 1):
        dp[i] = 1.0
    dp[K - 1] = float(min(N - K + 1, W)) / W
    for i in range(K - 2, -1, -1):
        dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
    return dp[0]

if __name__ == '__main__':
    N = 21
    K = 17
    W = 10
    print(solution(N, K, W))
    print(excellent(N, K, W))
