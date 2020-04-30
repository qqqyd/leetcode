"""
面试题 01.06. 字符串压缩
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。
示例1:
 输入："aabcccccaaa"
 输出："a2b1c5a3"

我的思想：
最简单的思想，从头往后，碰见不同的值就换

优解思想：

收获：

"""

def solution(S):
    # S: str
    if not S:
        return ''
    ch = S[0]
    count = 0
    result = ''
    for c in S:
        if c == ch:
            count += 1
        else:
            result += ch + str(count)
            ch = c
            count = 1 
    result += ch + str(count)
    return result if len(result) < len(S) else S
    
def excellent():
    pass

if __name__ == '__main__':
    S = "aabcccccaaa"
    print(solution(S))
