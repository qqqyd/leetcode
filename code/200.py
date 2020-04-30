"""
200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
示例 1:
输入:
11110
11010
11000
00000
输出: 1

我的思想：
遍历数组，每碰到1都以其为源做一次WFS

优解思想：

收获：

"""

def solution(grid):
    # grid: List[List[str]]
    if not grid:
        return 0
    queue = []
    res = 0
    row, col = len(grid), len(grid[0])
    
    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1":
                res += 1
                queue.append((i, j))
                while queue:
                    x, y = queue.pop(0)
                    for tx, ty in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
                        if 0 <= tx < row and 0 <= ty < col and grid[tx][ty] == "1":
                            queue.append((tx, ty))
                            grid[tx][ty] = "0"
                
    return res
    
def excellent():
    pass

if __name__ == '__main__':
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(solution(grid))
