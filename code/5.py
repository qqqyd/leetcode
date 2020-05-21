"""
5. 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

我的思想：
别人的思想
遍历字符串的每个位置，以这些位置为中心向外扩展

优解思想：
Manacher算法
i用来遍历，right记录当前中心扩散的最右下标
i >= right时，以i为中心扩散
i < right时，考虑i_sym
  arm_len[i_sym] < right - i，则arm_len[i] = arm_len[i_sym]
  arm_len[i_sym] == right - i，则arm_len[i]至少等于right - i，需要从right开始扩散
  arm_len[i_sym] > right - i，则arm_len[i] = right - i
综合可得arm_len[i_sym] = min(arm_len[i_sym], right - i)，再尝试中心扩散

收获：

"""

def solution(s):
    # s: str
    def expandAroundCenter(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
        
    start, end = 0, 0
    for i in range(len(s)):
        left1, right1 = expandAroundCenter(s, i, i)
        left2, right2 = expandAroundCenter(s, i, i + 1)
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2
    return s[start: end + 1]

    
class Excellent:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]

if __name__ == '__main__':
    s = "babad"
    print(solution(s))
