"""
面试题 01.07. 旋转矩阵
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
不占用额外内存空间能否做到？
示例 1:
给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

我的思想：
找到4个点最初的位置，然后旋转交换

优解思想：
水平翻转 + 主对角线翻转

收获：

"""

def solution(matrix):
    # matrix: List[List[int]]
    N = len(matrix)
    for i in range(N // 2):
        for j in range(i, N-1-i):
            matrix[i][j], matrix[j][N-i-1], matrix[N-i-1][N-j-1], matrix[N-j-1][i] = matrix[N-j-1][i], matrix[i][j], matrix[j][N-i-1], matrix[N-i-1][N-j-1]
    
def excellent(matrix):
    N = len(matrix)
    for i in range(N // 2):
        for j in range(N):
            matrix[i][j], matrix[N-i-1][j] = matrix[N-i-1][j], matrix[i][j]
    for i in range(N):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print(solution(matrix))
