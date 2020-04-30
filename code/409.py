"""
409. 最长回文串
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
注意:
假设字符串的长度不会超过 1010。
示例 1:
输入:
"abccccdd"
输出:
7

我的思想：
统计每个字符出现的次数，偶数直接加，只要有一种字符为奇数次，则总长度加1

优解思想：


收获：

"""

def solution(s):
    # s: str
    hashmap = {}
    result = 0
    for char in s:
        if char not in hashmap:
            hashmap[char] = 0
        hashmap[char] += 1
    for key in hashmap:
        result += hashmap[key] // 2 * 2
    return result + int(not result == len(s))
    
def excellent():

if __name__ == '__main__':
    s = "abccccdd"
    print(solution(s))
