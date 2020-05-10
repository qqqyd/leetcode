"""
69. x 的平方根
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。

我的思想：
二分查找

优解思想：
1. sqrt(x) = exp(1/2 * ln x)
2. 牛顿迭代。 y = x ^ 2 - C的零点

收获：

"""

def solution(x):
    # x: int
    l, r = 0, x
    while l <= r:
        mid = (l + r) // 2
        if mid ** 2 <= x:
            l = mid + 1
        else:
            r = mid - 1 
    return l - 1

    
def excellent(x):
    # 1
    if x == 0:
        return 0
    ans = int(math.exp(0.5 * math.log(x)))
    return ans + 1 if (ans + 1) ** 2 <= x else ans

    # 2
    if x == 0:
        return 0
    
    C, x0 = float(x), float(x)
    while True:
        xi = 0.5 * (x0 + C / x0)
        if abs(x0 - xi) < 1e-7:
            break
        x0 = xi
    return int(x0)


if __name__ == '__main__':
    x = 8
    print(solution(x))
