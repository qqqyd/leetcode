"""
面试题62. 圆圈中最后剩下的数字
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
示例 1：
输入: n = 5, m = 3
输出: 3

我的思想：
约瑟夫环

优解思想：
知道最后一轮剩下的位置必为0，然后向前反推在前一轮这个数的位置

收获：

"""

def solution(n, m):
    # n: int, m: int
    nums = [0] * n
    length = n
    i = 0
    count = 0
    while length > 1:    
        if nums[i] == 0:
            count += 1
            if count == m:
                nums[i] = 1
                count = 0
                length -= 1
                # print(i)
        i = (i + 1) % n
    for i in range(n):
        if nums[i] == 0:
            return i
    
def excellent(n, m):
    f = 0
    for i in range(2, n + 1):
        f = (f + m) % i
    return f

if __name__ == '__main__':
    n = 5
    m = 3
    # print(solution(n, m))
    print(excellent(n, m))
