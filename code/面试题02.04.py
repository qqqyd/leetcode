"""
面试题02.04. 分割链表
编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。
示例:
输入: head = 3->5->8->5->10->2->1, x = 5
输出: 3->1->2->10->5->5->8

我的思想：

优解思想：
维护两个链表

收获：
我总在考虑头指针的处理操作，看头指针到底是属于大值还是小值，就感觉太复杂了，就可以借鉴优解的，两个新链表第一个元素都为None就好了

"""

def solution():
    pass
    
def excellent(head, x):
    # head: ListNode, x: int
    low = ListNode(None)
    high = ListNode(None)
    low_head = low
    high_head = high
    while head:
        if head.val < x:
            low.next = head
            low = low.next
        else:
            high.next = head
            high = high.next
        head = head.next
    low.next = high_head.next
    high.next = None
    return low_head.next

if __name__ == '__main__':
    solution()
