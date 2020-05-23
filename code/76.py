"""
76. 最小覆盖子串
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
示例：
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：
如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

我的思想：
双指针去找，当前长度没有就右边加1，有的话就左边加1。l, r表示的是字符串的 [l, r)

优解思想：
大体思想差不多。但他是从目标字典入手的

收获：

"""

def solution(s, t):
    # s: str, t: str
    from collections import Counter
    from collections import defaultdict

    des_dict = Counter(t)
    des_len = len(t)
    ori_dict = defaultdict(int)
    l, r = 0, 0
    res = [0, 0]
    res_len = float("inf")
    
    while True:
        flag = True
        if r - l < des_len:
            flag = False
        else:
            for key in des_dict.keys():
                if ori_dict[key] < des_dict[key]:
                    flag = False
                    break

        if flag:
            if(r - l) < res_len:
                res_len = r - l
                res = [l, r]
            ori_dict[s[l]] -= 1
            l += 1
        else:
            if r >= len(s):
                break
            ori_dict[s[r]] += 1
            r += 1

    return s[res[0]: res[1]]


    
def excellent(s, t):
    from collections import defaultdict
    des_dict = defaultdict(int)
    for temp in t:
        des_dict[temp] += 1
    des_len = len(t)

    res_l, res_r = 0, len(s)
    l = 0

    for r, char in enumerate(s):
        if des_dict[char] > 0:
            des_len -= 1
        des_dict[char] -= 1

        if des_len == 0:
            while des_dict[s[l]] < 0:
                des_dict[s[l]] += 1
                l += 1

            if r - l < res_r - res_l:
                res_l, res_r = l, r

            des_dict[s[l]] += 1
            des_len += 1
            l += 1
    return '' if res_r == len(s) else s[res_l: res_r + 1]


if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    S = "a"
    T = "aa"
    print(solution(S, T))
