"""
739. 每日温度
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。
例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

我的思想：
就是找出数组中下一个大于该数的位置，用单调递减栈来完成

优解思想：

收获：
找数组中下一个符合某条件的数用单调栈来解决很好

"""

def solution(T):
    # T: List[int]
    n = len(T)
    res = [0] * n
    stack = []
    for i in range(n):
        while stack and T[i] > T[stack[-1]]:
            prev_index = stack.pop()
            res[prev_index] = i - prev_index
        stack.append(i)
    return res

def excellent():
    pass

if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(solution(T))
