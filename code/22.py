"""
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

我的思想：
别人的代码
第n组括号为()，则n-1组括号要么在里，要么在右
"(" + [i=p时所有括号的排列组合] + ")" + [i=q时所有括号的排列组合]，其中p+q = n-1

优解思想：
我精简了一下代码

收获：

"""

def solution(n):
    # n: int
    if n == 0:
        return []
    total_l = []
    total_l.append([None])    # 0组括号时记为None
    total_l.append(["()"])    # 1组括号只有一种情况
    for i in range(2,n+1):    # 开始计算i组括号时的括号组合
        l = []        
        for j in range(i):    # 开始遍历 p q ，其中p+q=i-1 , j 作为索引
            now_list1 = total_l[j]    # p = j 时的括号组合情况
            now_list2 = total_l[i-1-j]    # q = (i-1) - j 时的括号组合情况
            for k1 in now_list1:  
                for k2 in now_list2:
                    if k1 == None:
                        k1 = ""
                    if k2 == None:
                        k2 = ""
                    el = "(" + k1 + ")" + k2
                    l.append(el)    # 把所有可能的情况添加到 l 中
        total_l.append(l)    # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
    return total_l[n]
    
def excellent(n):
    if n == 0:
        return []
    total_l = [[""], ["()"]]
    for i in range(2, n + 1):
        total_l.append(["(" + k1 + ")" + k2 for j in range(i) for k2 in total_l[i-1-j] for k1 in total_l[j]] )
    return total_l[n]

if __name__ == '__main__':
    n = 3
    print(solution(n))
    print('-' * 30)
    print(excellent(n))
