"""
695. 岛屿的最大面积
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)
示例 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

我的思想：
遍历数组，找到1的时候就往队列里面加入其四周的点，访问过的点设成0

优解思想：

收获：

"""

def solution(grid):
    # grid: List[List[int]]
    h, w = len(grid), len(grid[0])
    result = 0
    queue = []
    direc = [[-1,0],[0,-1],[0,1],[1,0]]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 0:
                continue
            temp = 0
            queue.append([i, j])
            while queue:
                y, x = queue.pop()
                if grid[y][x] == 0:
                    continue
                grid[y][x] = 0
                temp += 1
                for dir_y, dir_x in direc:
                    new_y, new_x = y + dir_y, x + dir_x
                    if -1 < new_y < h and -1 < new_x < w and grid[new_y][new_x] == 1:
                        queue.append([new_y, new_x])
            result = max(result, temp)
    return result
    
def excellent(grid):
    # grid: List[List[int]]
    pass

if __name__ == '__main__':
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    print(solution(grid))
    print(excellent(grid))
