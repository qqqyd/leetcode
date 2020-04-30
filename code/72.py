"""
72. 编辑距离
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符

示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

我的思想：
动态规划，关键就是dp推导式
dp[i][j]表示A的前i个和B的前j个的距离
若A, B最后一个字符相同 D[i][j] = min(D[i][j−1] + 1, D[i−1][j] + 1, D[i−1][j−1])
若不同 D[i][j] = min(D[i][j−1] + 1, D[i−1][j] + 1, D[i−1][j−1] + 1)

优解思想：
算过的值存进set，d表示到当前w1和w2经过的操作数，两者相等时结束

收获：

"""

def solution(word1, word2):
    # word1: str, word2: str
    n = len(word1)
    m = len(word2)
    if n * m == 0:
        return n + m
    
    D = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            left = D[i - 1][j] + 1
            down = D[i][j - 1] + 1
            left_down = D[i - 1][j - 1] 
            if word1[i - 1] != word2[j - 1]:
                left_down += 1
            D[i][j] = min(left, down, left_down)
    
    return D[n][m]

    
def excellent(word1, word2):
    from collections import deque
    visit, dq = set(), deque([(word1, word2, 0)])
    while True:
        w1, w2, d = dq.popleft()
        if (w1, w2) not in visit:
            if w1 == w2:
                return d
            visit.add((w1, w2))
            while w1 and w2 and w1[0] == w2[0]:
                w1, w2 = w1[1:], w2[1:]
            d += 1
            dq.extend([(w1[1:], w2[1:], d), (w1, w2[1:], d), (w1[1:], w2, d)])

if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    # print(solution(word1, word2))
    print(excellent(word1, word2))
