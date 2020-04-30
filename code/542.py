"""
542. 01 矩阵
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。
示例 1:
输入:
0 0 0
0 1 0
0 0 0
输出:
0 0 0
0 1 0
0 0 0

我的思想：
BFS搜索

优解思想：
动态规划，先一遍左上到右下，再右下到左上一遍

收获：

"""

def solution(matrix):
    # matrix: List[List[int]]
    row, col = len(matrix), len(matrix[0])
    queue = []
    direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    res = [[-1] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                queue.append((i, j))
                res[i][j] = 0
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direct:
            tx, ty = x + dx, y + dy
            if 0 <= tx < row and 0 <= ty < col and res[tx][ty] == -1:
                res[tx][ty] = res[x][y] + 1
                queue.append((tx, ty))

    return res
    
def excellent(matrix):
    m, n = len(matrix), len(matrix[0])
    dist = [[10**9] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                dist[i][j] = 0

    for i in range(m):
        for j in range(n):
            if i - 1 >= 0:
                dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
            if j - 1 >= 0:
                dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i + 1 < m:
                dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
            if j + 1 < n:
                dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
    return dist

if __name__ == '__main__':
    matrix = [[0,0,0],[0,1,0],[0,0,0]]
    matrix = [[0],[0],[0],[0],[0]]
    print(solution(matrix))
