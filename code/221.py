"""
221. 最大正方形
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
示例:
输入: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
输出: 4

我的思想：
别人的解法
动态规划，主要是要找到dp公式，在这里dp[i][j]表示以(i, j)为右下角的最大正方形边长，dp公式为
dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

优解思想：

收获：

"""

def solution(matrix):
    # matrix: List[List[str]]
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    row, col = len(matrix), len(matrix[0])
    res = 0
    dp = [[0] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                res = max(res, dp[i][j])

    return res ** 2
    
def excellent():
    pass

if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(solution(matrix))
