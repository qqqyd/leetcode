"""
面试题57 - II. 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
示例 1：
输入：target = 9
输出：[[2,3,4],[4,5]]

我的思想：
先找出最大的项数，然后根据等差数列求和公式求出该项数下的首项，判断是否为整

优解思想：

收获：

"""

def solution(target):
    res = []
    for n in range(int((2*target+0.25)**0.5-0.5), 1, -1):
        a = target / n + (1 - n) * 0.5
        if int(a) == a:
            res.append(list(range(int(a), int(a)+n)))
    return res

def excellent(target):


if __name__ == '__main__':
    target = 3
    print(solution(target))