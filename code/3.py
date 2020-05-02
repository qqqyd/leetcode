"""
3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

我的思想：
使用前后指针，保证两个指针间的字符串无重复，记录最大值

优解思想：
思想相同，循环变量作为左指针

收获：

"""

def solution(s):
    # s: str
    res = 0
    pre = 0
    i = 0
    while i < len(s):
        if i == pre:
            i += 1
        elif s[i] in s[pre:i]:
            pre += 1
        else:
            i += 1
        res = max(res, i - pre)
    return res
    
def excellent(s):
    res = 0
    rp = 0
    n = len(s)
    chars = set()
    for lp in range(n):
        if lp:
            chars.remove(s[lp - 1])
        while rp < n and s[rp] not in chars:
            chars.add(s[rp])
            rp += 1
        res = max(res, rp - lp)
    return res 

if __name__ == '__main__':
    s = "abcabcbb"
    s = "pwwkew"
    s = "aaa"
    print(solution(s))
    print(excellent(s))
