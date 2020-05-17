"""
210. 课程表 II
现在你总共有 n 门课需要选，记为 0 到 n-1。
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。
可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。
示例 1:
输入: 2, [[1,0]] 
输出: [0,1]
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
示例 2:
输入: 4, [[1,0],[2,0],[3,1],[3,2]]
输出: [0,1,2,3] or [0,2,1,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
     因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。

我的思想：
别人的思想
深度优先搜索，

优解思想：

收获：
可以用字典来记录图，key表示节点，值表示边

"""

def solution(numCourses, prerequisites):
    # numCourses: int, prerequisites: List[List[int]]
    # 记录图的边
    edges = collections.defaultdict(list)
    # 标记每个节点的状态：0=未搜索，1=搜索中，2=已完成
    visited = [0] * numCourses
    # 用数组来模拟栈，下标 0 为栈底，n-1 为栈顶
    res = []
    # 判断有向图中是否有环
    invalid = False

    for info in prerequisites:
        edges[info[1]].append(info[0])
    
    def dfs(u):
        nonlocal invalid
        visited[u] = 1
        # 搜索相邻节点，有环就停止
        for v in edges[u]:
            if visited[v] == 0:
                dfs(v)
                if invalid:
                    return
            # 找到了环
            elif visited[v] == 1:
                invalid = True
                return
        # 搜索完成
        visited[u] = 2
        res.append(u)
    
    # 每次挑选一个「未搜索」的节点，开始进行深度优先搜索
    for i in range(numCourses):
        if not invalid and not visited[i]:
            dfs(i)

    return [] if invalid else res[::-1] 
    
def excellent():
    pass

if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(solution(numCourses, prerequisites))
