"""
面试题59-II. 队列的最大值
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1
示例 1：
输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]

我的思想：
用list完成

优解思想：
用一个辅助队列来记录最大值，因为是要O(1)时间复杂度

收获：

"""

class solution:
    def __init__(self):
        self.queue = []

    def max_value(self) -> int:
        value = -1
        for num in self.queue:
            if num > value:
                value = num
        return value

    def push_back(self, value: int) -> None:
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        return self.queue.pop(0)
    
class excellent:
    def __init__(self):
        self.queue = []
        self.deque = []
        
    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.deque and value > self.deque[-1]:
            self.deque.pop(-1)
        self.deque.append(value)

    def pop_front(self) -> int:
        front = self.queue and self.queue.pop(0)
        if self.deque and self.deque[0] == front:
            self.deque.pop(0)
        return front or -1

if __name__ == '__main__':
    # solution()
