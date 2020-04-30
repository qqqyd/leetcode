"""
1162. 地图分析
你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。
我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。
如果我们的地图上只有陆地或者海洋，请返回 -1。
示例 1：
输入：[[1,0,1],[0,0,0],[1,0,1]]
输出：2

我的思想：
基本思想，但比较慢

优解思想：
把land加入队列，然后广度优先搜索，一个地方只要被访问一次就可以了

收获：

"""

def solution(grid):
    # grid: List[List[int]]
    N = len(grid)
    land = {(i, j) for i in range(N) for j in range(N) if grid[i][j]}
    res = -1

    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                continue
            temp = 3 * N
            for li, lj in land:
                temp = min(temp, abs(i - li) + abs(j - lj))
            res = max(res, temp) if temp != 3 * N else res
    return res

    
def excellent(grid):
    N = len(grid)
    res = -1
    queue = [(i, j) for i in range(N) for j in range(N) if grid[i][j]]
    direc = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    if len(queue) == 0 or len(queue) == N * N:
        return res
    while len(queue) > 0:
        for _ in range(len(queue)): 
            i, j = queue.pop(0)
            for di, dj in direc:
                ti, tj = i + di, j + dj
                if ti >= 0 and ti < N and tj >= 0 and tj < N and grid[ti][tj] == 0:
                    queue.append((ti, tj))
                    grid[ti][tj] = -1
        res += 1
        
    return res

if __name__ == '__main__':
    grid = [[1,0,1],[0,0,0],[1,0,1]]
    print(solution(grid))
    print(excellent(grid))
