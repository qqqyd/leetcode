"""
892. 三维形体的表面积
在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
请你返回最终形体的表面积。
示例 1：
输入：[[2]]
输出：10
示例 2：
输入：[[1,2],[3,4]]
输出：34

我的思想：
遍历每个点，然后下一个点来的时候计算与i-1和j-1的重叠量

优解思想：
代码更简洁

收获：

"""

def solution(grid):
    # grid: List[List[int]]
    N = len(grid)
    res = 0
    for i in range(N):
        for j in range(N):
            res += 4 * grid[i][j] + 2 if grid[i][j] != 0 else 0
            if j > 0:
                res -= min(grid[i][j], grid[i][j-1]) * 2
            if i > 0:
                res -= min(grid[i][j], grid[i-1][j]) * 2
    return res

    
def excellent(grid):
    # grid: List[List[int]]
    N = len(grid)
    res = 0
    for i in range(N):
        res += sum([4 * num + 2 if num > 0 else 0 for num in grid[i]])
        res -= 2 * sum([min(grid[i][j], grid[i][j - 1]) for j in range(1, N)])
        if i:
            res -= 2 * sum([min(grid[i - 1][j], grid[i][j]) for j in range(N)])
    return res

if __name__ == '__main__':
    grid = [[1,2],[3,4]]
    # grid = [[1,0],[0,2]]

    print(solution(grid))
    print('---------------------')
    print(excellent(grid))
