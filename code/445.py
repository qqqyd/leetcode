"""
445. 两数相加 II
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。
进阶：
如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
示例：
输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7

我的思想：
使用栈来完成相加

优解思想：

收获：

"""

def solution(l1, l2):
    # l1: ListNode, l2: ListNode
    s1, s2 = [], []
    while l1:
        s1.append(l1.val)
        l1 = l1.next
    while l2:
        s2.append(l2.val)
        l2 = l2.next
    res = None
    carry = 0
    while s1 or s2 or carry != 0:
        a = 0 if not s1 else s1.pop()
        b = 0 if not s2 else s2.pop()
        cur = a + b + carry
        carry = cur // 10
        cur %= 10
        curnode = ListNode(cur)
        curnode.next = res
        res = curnode
    return res

    
def excellent():
    pass

if __name__ == '__main__':
    
    print(solution())
