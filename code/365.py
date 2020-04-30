"""
365. 水壶问题
有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。
你允许：
装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
示例 1: (From the famous "Die Hard" example)
输入: x = 3, y = 5, z = 4
输出: True

我的思想：

优解思想：
找到a, b的整数解满足ax + by = z，求解运用了贝祖定理

收获：

"""

def solution(x, y, z):
    pass
    
def excellent(x, y, z):
    # x: int, y: int, z: int
    if x + y < z:
        return False
    if x == 0 or y == 0:
        return z == 0 or x + y == z
    return z % math.gcd(x, y) == 0

if __name__ == '__main__':
    
    print(solution())
