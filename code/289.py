"""
289. 生命游戏
根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
示例：
输入： 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
输出：
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]

我的思想：
硬解，类似于3x3卷积

优解思想：
用不止0 1的新状态来填充board，最后再更新，达到原地更新

收获：

"""

def solution(board):
    # board: List[List[int]]
    import numpy as np
    r, c = len(board), len(board[0])
    board_exp = np.zeros((r + 2, c + 2))
    board_exp[1: 1 + r, 1: 1 + c] = np.array(board)
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    for i in range(1, 1 + r):
        for j in range(1 , 1 + c):
            temp_sum = np.sum(kernel * board_exp[i-1: i+2, j-1: j+2])
            if board_exp[i,j] == 1 and (temp_sum < 2 or temp_sum > 3):
                board[i-1][j-1] = 0
            if board_exp[i,j] == 0 and temp_sum == 3:
                board[i-1][j-1] = 1
    
def excellent(board):
    neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

    rows = len(board)
    cols = len(board[0])

    for row in range(rows):
        for col in range(cols):
            live_neighbors = 0
            for neighbor in neighbors:
                r = (row + neighbor[0])
                c = (col + neighbor[1])

                if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                    live_neighbors += 1

            if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                # -1 代表这个细胞过去是活的现在死了
                board[row][col] = -1
            if board[row][col] == 0 and live_neighbors == 3:
                # 2 代表这个细胞过去是死的现在活了
                board[row][col] = 2

    for row in range(rows):
        for col in range(cols):
            if board[row][col] > 0:
                board[row][col] = 1
            else:
                board[row][col] = 0

if __name__ == '__main__':
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    print(solution(board))
    # print(excellent(board))
