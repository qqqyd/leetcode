"""
面试题13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
示例 1：
输入：m = 2, n = 3, k = 1
输出：3

我的思想：
BFS

优解思想：

收获：

"""

def solution(m, n, k):
    # m: int, n: int, k: int
    def digitsum(n):
        ans = 0
        while n:
            ans += n % 10
            n //= 10
    return ans

    from queue import Queue
    q = Queue()
    q.put((0, 0))
    s = set()
    while not q.empty():
        x, y = q.get()
        if (x, y) not in s and 0 <= x < m and 0 <= y < n and digitsum(x) + digitsum(y) <= k:
            s.add((x, y))
            for nx, ny in [(x + 1, y), (x, y + 1)]:
                q.put((nx, ny))
    return len(s)

    
def excellent(m, n, k):
    num = 0
    for i in range(m // 10 + 1):
        if k-7-i > 0: # 跟右边的块也连通了
            range_n = k-7-i 
        else: # i==0表示是第一块，不为0说明是后面的块，此时未连通
            range_n = 1 if i == 0 else 0
        for j in range(range_n):
            now_k = k - (i + j)
            for p in range(min(m, i * 10 + 10) - i * 10):
                for q in range(min(n, j * 10 + 10) - j * 10):
                    if p + q <= now_k:
                        print(p, q, i, j)
                        num += 1
    return num

if __name__ == '__main__':
    m = 8
    n = 14
    k = 14
    # print(solution(m, n, k))
    print(excellent(m, n, k))
