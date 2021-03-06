"""
1160. 拼写单词
给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
注意：每次拼写时，chars 中的每个字母都只能用一次。
返回词汇表 words 中你掌握的所有单词的 长度之和。
示例 1：
输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释： 
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。

我的思想：
做两个hashmap，依次比较就行了

优解思想：
思想一样，代码简洁

收获：
for else的使用，对于跳出多层循环很有用；只有正常结束时，才会执行else
"""

def solution(words, chars):
    # words: List[str], chars: str
    char_map = {}
    for char in chars:
        if char not in char_map:
            char_map[char] = 0
        char_map[char] += 1

    result = 0
    for word in words:
        flag = True
        word_map = {}
        for w in word:
            if w not in char_map:
                break
            if w not in word_map:
                word_map[w] = 0
            word_map[w] += 1
            if word_map[w] > char_map[w]:
                break
        else:
            result += len(word)
    return result
    
def excellent(words, chars):
    # words: List[str], chars: str
    result = 0
    for word in words:
        for w in word:
            if word.count(i) > chars.count(i):
                break
        else:
            result += len(word)
    return result

if __name__ == '__main__':
    words = ["cat","bt","hat","tree"]
    chars = "atach"
    print(solution(words, chars))
