"""
1071. 字符串的最大公因子
对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

示例 1：
输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"

我的思想：

优解思想：
先判断str1+str2==str2+str1?是否有解
然后找两个字符串长度的gcd就是了

收获：

"""

def solution(str1, str2):
    pass

def excellent(str1, str2):
    # str1: str, str2: str
    import math
    if str1 + str2 != str2 + str1:
        return ''
    return str1[: math.gcd(len(str1), len(str2))]

if __name__ == '__main__':
    str1 = "ABCABC"
    str2 = "ABC"
    print(solution(str1, str2))
