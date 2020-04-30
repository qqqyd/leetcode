"""
480. 滑动窗口中位数
中位数是有序序列最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。
示例：
给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。
窗口位置                      中位数
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
 因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。

我的思想：
暴力求解

优解思想：
使用堆操作来做

收获：
heapq实现的都是小顶堆，所以要实现大顶堆的话，就在前面加负号

改进：
先维护一个hash表，只有堆顶元素在hash表中的时候，才删；下标为要删的数组，元素为这个数值的个数

"""

import heapq
from heapq import heappush, heappop

def solution(nums, k):
    # nums: List[int], k: int
    n = len(nums)
    ans = []
    idx = int(k/2)
    for i in range(n-k+1):
        temp = nums[i:i+k]
        temp.sort()
        if k%2 == 0:
            ans.append((temp[idx]+temp[idx-1])/2)
        else:
            ans.append(temp[idx])
    return ans
    
def excellent(nums, k):
    min_heap = [] # 小顶堆，存大元素
    max_heap = [] # 大顶堆，存小元素
    res = []

    for i in range(len(nums)):
        # 新元素加入堆中
        if not min_heap or nums[i] >= min_heap[0]:
            heappush(min_heap, nums[i])
        else:
            heappush(max_heap, -nums[i])

        # 保证两个堆的大小相等或相差1
        if len(min_heap) > len(max_heap) + 1:
            heapq.heappush(max_heap, -heappop(min_heap))
        if len(min_heap) < len(max_heap):
            heapq.heappush(min_heap, -heappop(max_heap))

        # 两个堆中加起来至少有k个元素了
        if i >= k - 1:
            if len(max_heap) + len(min_heap) & 1:
                res.append(min_heap[0])
            else:
                res.append((min_heap[0]-max_heap[0]) * 0.5)

            delete_num = nums[i-k+1]


            # 这里可以改进，先维护一个hash表，只有堆顶元素在hash表中的时候，才删；下标为要删的数组，元素为这个数值的个数
            if delete_num < min_heap[0]:
                heapdelete(max_heap, -delete_num)
            else:
                heapdelete(min_heap, delete_num)

            if len(min_heap) > len(max_heap) + 1:
                heapq.heappush(max_heap, -heappop(min_heap))
            if len(max_heap) > len(min_heap):
                heapq.heappush(min_heap, -heappop(max_heap))
    return res

def heapdelete(heap, value):  # 删除堆中指定元素
    if value == heap[-1]:
        return heap.pop()
    node_index = heap.index(value)
    heap[node_index] = heap[-1]
    heap.pop()
    heapq._siftup(heap, node_index) #不断和子节点比，让子节点上浮
    heapq._siftdown(heap, 0, node_index)  # 注意_siftdown是使父节点往下移动

if __name__ == '__main__':
    nums = [1,3,-2,-4,5,3,6,7,9]
    k = 6
    # solution()
    excellent2(nums, k)