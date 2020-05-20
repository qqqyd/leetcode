"""
1371. 每个元音包含偶数次的最长子字符串
给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。
示例 1：
输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
示例 2：
输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。

我的思想：
别人的思想
因为有5个元音，所以用5位二进制数来记录表示。哪一位为1就表示哪个字母出现奇数次，00000表示全部出现偶数次，共32个状态。
初始各状态为-1，每次记录当前前缀字符串中的元音状态，有两次状态一样时，即该状态之前出现过的时候，两次状态之间的即为解。
pos数组下标为状态，共32个，元素值为该状态第一次出现的坐标位置

优解思想：

收获：
偶数次出现的问题都可以考虑一下二进制异或操作

"""

def solution(s):
    # s: str
    ans, status = 0, 0
    pos = [0] + [-1] * 31

    for i, letter in enumerate(s):
        if letter in 'aeiou':
            status ^= 1 << 'aeiou'.index(letter)

        if pos[status] == -1:
            pos[status] = i + 1
        else:
            ans = max(ans, i + 1 - pos[status])

    return ans

    
def excellent():
    pass

if __name__ == '__main__':
    s = "eleetminicoworoep"
    print(solution(s))
