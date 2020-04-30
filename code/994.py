"""
994. 腐烂的橘子
在给定的网格中，每个单元格可以有以下三个值之一：
值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

我的思想：
广度优先
用队列

优解思想：
使用集合，一个集合放腐烂的坐标，另一个放新鲜的坐标，腐烂集合每次扩张，然后新鲜集合减去腐烂集合

收获：
visit = [[True] * w] * h 这个*h是浅复制，改变第一个数组的值，几个数组的值都会同时改变
使用集合操作可以避免队列，集合是直接存储了所有腐烂和新鲜的位置，相对队列而言更占位置一些（微乎其微），但计算很快

改进：
腐烂集合每次都重新计算了所有腐烂的位置，并不是最外围的，我可以再维护一个visit集合，即为上一次的rotten集合
rotten, visit = {(i+di,j+dj) for i,j in rotten-visit for di,dj in direc if (i+di,j+dj) in fresh} + visit, rotten

"""

def solution(grid):
  h, w = len(grid), len(grid[0])
  visit = [[True] * w for j in range(h)]
  queue = []
  direc = [[-1,0],[0,-1],[0,1],[1,0]]
  minite = 0
  for i in range(h):
    for j in range(w):
      if grid[i][j] == 1:
        visit[i][j] = False
      elif grid[i][j] == 2:
        queue.append([i, j])

  while True:
    queue_next = []
    while queue:
      y, x = queue.pop(0)
      for dir_y, dir_x in direc:
        y_new, x_new = y + dir_y, x + dir_x
        if -1 < y_new < h and -1 < x_new < w and visit[y_new][x_new] == False:
          visit[y_new][x_new] = True
          if grid[y_new][x_new] == 1:
            queue_next.append([y_new, x_new])
    if not queue_next:
      break
    queue = queue_next
    minite += 1

  return -1 if not all([all(visit[y]) for y in range(h)]) else minite


def excellent(grid):
    row, col = len(grid), len(grid[0])
    rotten = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
    fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
    time = 0
    while fresh:
      if not rotten: return -1
      rotten = {(i + di, j + dj) for i, j in rotten for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)] if (i + di, j + dj) in fresh}
      fresh -= rotten
      time += 1
    return time

if __name__ == '__main__':
    grid = [[2,1,1],[1,1,0],[1,0,1]]
    print(solution(grid))
