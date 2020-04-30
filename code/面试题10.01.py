"""
面试题10.01. 合并排序的数组
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
初始化 A 和 B 的元素数量分别为 m 和 n。
示例:
输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]

我的思想：
先找出A中各个元素需要后退的距离，然后直接移动，再将B按对应方式插入进去
但插入的过程有些太麻烦，下标的具体值有点费劲，太麻烦了，就没写了
这种方法的好处是A，B数组都只查看一遍，之后移动A的位置，再插入B，一遍完成

优解思想：
直接从后往前找，将两者的大值放到A数组最后

收获：
数组移位的操作肯定得从后往前走

"""

def solution():
    pass
    
def excellent():
    while m > 0 and n > 0:
        if A[m - 1] > B[n - 1]:
            A[m + n - 1] = A[m - 1]
            m -= 1
        else:
            A[m + n - 1] = B[n - 1]
            n -= 1
    if n > 0:
        A[0:n] = B[0:n]

if __name__ == '__main__':
    solution()
