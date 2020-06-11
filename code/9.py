"""
9. 回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
示例 1:
输入: 121
输出: true
示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:
你能不将整数转为字符串来解决这个问题吗？

我的思想：
转换成字符串来判断

优解思想：
不用字符串，就用整数来解决

收获：

"""

def solution(x):
    # x: int
    s = str(x)
    for i in range(len(s)//2):
        if s[i] != s[~i]:
            return False
    return True
    
def excellent(x):
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    revert_num = 0
    while(x > revert_num):
        revert_num = 10 * revert_num + x % 10
        x //= 10
    return x == revert_num or x == revert_num // 10

if __name__ == '__main__':
    x = 121
    print(solution(x))
