"""
1103. 分糖果 II
排排坐，分糖果。
我们买了一些糖果 candies，打算把它们分给排好队的 n = num_people 个小朋友。
给第一个小朋友 1 颗糖果，第二个小朋友 2 颗，依此类推，直到给最后一个小朋友 n 颗糖果。
然后，我们再回到队伍的起点，给第一个小朋友 n + 1 颗糖果，第二个小朋友 n + 2 颗，依此类推，直到给最后一个小朋友 2 * n 颗糖果。
重复上述过程（每次都比上一次多给出一颗糖果，当到达队伍终点后再次从队伍起点开始），直到我们分完所有的糖果。注意，就算我们手中的剩下糖果数不够（不比前一次发出的糖果多），这些糖果也会全部发给当前的小朋友。
返回一个长度为 num_people、元素之和为 candies 的数组，以表示糖果的最终分发情况（即 ans[i] 表示第 i 个小朋友分到的糖果数）。

示例：
输入：candies = 7, num_people = 4
输出：[1,2,3,1]
解释：
第一次，ans[0] += 1，数组变为 [1,0,0,0]。
第二次，ans[1] += 2，数组变为 [1,2,0,0]。
第三次，ans[2] += 3，数组变为 [1,2,3,0]。
第四次，ans[3] += 1（因为此时只剩下 1 颗糖果），最终数组变为 [1,2,3,1]。


我的思想：
最简单的想法

优解思想：
使用等差数列，先算出来每人在完整轮数能拿到的所有礼物数，最后再加一个非完整轮数
感觉没必要

收获：

"""

def solution():
    ans = [0] * num_people
    i = 1
    while candies >= i:
        ans[(i-1)%num_people] += i
        candies -= i
        i += 1
    ans[(i-1)%num_people] += candies
    return ans

    
def excellent():
    p = int((2 * candies + 0.25)**0.5 - 0.5) # 可以完整发的礼物次数
    remaining = int(candies - (p + 1) * p * 0.5) # 最后一次剩的数
    rows, cols = p // num_people, p % num_people # rows为完整轮数，cols为最后一轮剩的
    
    ans = [0] * num_people
    for i in range(num_people):
        ans[i] = (i + 1) * rows + int(rows * (rows - 1) * 0.5) * num_people
        if i < cols:
            ans[i] += i + 1 + rows * num_people
    ans[cols] += remaining
    return ans

if __name__ == '__main__':
    solution()
