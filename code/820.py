"""
820. 单词的压缩编码
给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。
对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
那么成功对给定单词列表进行编码的最小字符串长度是多少呢？
示例：
输入: words = ["time", "me", "bell"]
输出: 10
说明: S = "time#bell#" ， indexes = [0, 2, 5] 。

我的思想：
words变成集合，然后遍历所有单词的后缀从集合删除，返回最终集合长度

优解思想：
前缀树，代码没看懂

收获：

"""

def solution(words):
    # words: List[str]
    words_set = set(words)
    for word in words_set:
        for k in range(1, len(word)):
            words_set.discard(word[k:])

    return sum(len(word) + 1 for word in words_sets)

def excellent(words):
    import collections
    from functools import reduce
    words = list(set(words))
    print(words)
    Trie = lambda: collections.defaultdict(Trie)
    trie = Trie()

    nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]

    return sum(len(word) + 1
               for i, word in enumerate(words)
               if len(nodes[i]) == 0)

if __name__ == '__main__':
    words = ["time", "me", "bell"]
    print(excellent(words))
