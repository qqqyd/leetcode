"""
990. 等式方程的可满足性
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 
示例 1：
输入：["a==b","b!=a"]
输出：false
解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
示例 2：
输出：["b==a","a==b"]
输入：true
解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。
示例 3：
输入：["a==b","b==c","a==c"]
输出：true
示例 4：
输入：["a==b","b!=c","c==a"]
输出：false
示例 5：
输入：["c==c","b==d","x!=z"]
输出：true

我的思想：
创建多跳数组保存关系

优解思想：

收获：

"""

def solution(equations):
    # equations: List[str]
    char_store = list(range(0, 26))
    for equation in equations:
        if equation[1] == '=':
            val1 = ord(equation[0]) - ord('a')
            while char_store[val1] != val1:
                val1 = char_store[val1]
            val2 = ord(equation[3]) - ord('a')
            while char_store[val2] != val2:
                val2 = char_store[val2]
            if char_store[val1] != char_store[val2]:
                char_store[val2] = char_store[val1]
    for equation in equations:
        if equation[1] == '!':
            val1 = ord(equation[0]) - ord('a')
            while char_store[val1] != val1:
                val1 = char_store[val1]
            val2 = ord(equation[3]) - ord('a')
            while char_store[val2] != val2:
                val2 = char_store[val2]
            if val1 == val2:
                return False
    return True
    
def excellent():
    pass

if __name__ == '__main__':
    equations = ["c==c","b==d","x!=z"]
    equations = ["c==c","f!=a","f==b","b==c"]
    print(solution(equations))
