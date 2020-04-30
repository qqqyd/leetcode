"""
914. 卡牌分组
给定一副牌，每张牌上都写着一个整数。
此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。
示例 1：
输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]

我的思想：

优解思想：

收获：
学习reduce用法，输入为函数和可迭代对象，对前两个结果求函数，然后结果与后项再求

"""

def solution(deck):
    # deck: List[int]
    import collections
    from fractions import gcd
    vals = collections.Counter(deck).values()
    return reduce(gcd, vals) >= 2

    
def excellent():
    pass

if __name__ == '__main__':
    deck = [1,2,3,4,4,3,2,1]
    print(solution(deck))
