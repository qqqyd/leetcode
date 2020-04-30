"""
202. 快乐数
编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 True ；不是，则返回 False 。
示例：
输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

我的思想：
用hashmap来索引

优解思想：
快慢指针的方法，慢指针一次进一格，快指针一次进两格

收获：

"""

def solution(n):
    # n: int
    hashmap = {}
    while n not in hashmap:
        hashmap[n] = 1
        sum = 0
        while n:
            sum += (n % 10) ** 2
            n //= 10
        if sum == 1:
            return True
        n = sum

    return False
    
def excellent(n):
    def get_next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    slow_runner = n
    fast_runner = get_next(n)
    while fast_runner != 1 and slow_runner != fast_runner:
        slow_runner = get_next(slow_runner)
        fast_runner = get_next(get_next(fast_runner))
    return fast_runner == 1

if __name__ == '__main__':
    n = 19
    n = 2
    # print(solution(n))
    print(excellent(n))
