"""
680. 验证回文字符串 Ⅱ
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
示例 1:
输入: "aba"
输出: True
示例 2:
输入: "abca"
输出: True
解释: 你可以删除c字符。

我的思想：
暴力求解，判断是否为回文序列时采用双指针

优解思想：
贪心算法

收获：

"""

def solution(s):
    # s: str
    def check_str(ss):
        i, j = 0, len(ss) - 1
        while i < j:
            if ss[i] != ss[j]:
                return False
            i += 1
            j -= 1
        return True
    if check_str(s):
        return True
    for i in range(len(s)):
        ss = s[:i] + s[i+1:]
        if check_str(ss):
            return True
    return False
    
def excellent(s):
    def checkPalindrome(low, high):
        i, j = low, high
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    low, high = 0, len(s) - 1
    while low < high:
        if s[low] == s[high]: 
            low += 1
            high -= 1
        else:
            return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
    return True


if __name__ == '__main__':
    s = "abca"
    print(solution(s))
