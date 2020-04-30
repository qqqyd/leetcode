"""
876. 链表的中间结点
给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。
示例 1：
输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.

我的思想：
维护两个指针，后面的指针一次进两个，前面的一次进一格，来完成找中间的操作

优解思想：
思想一样，代码简洁

收获：

"""

def solution(head):
    # head: ListNode
    tail = head
    while tail:
        if tail.next and tail.next.next:
            tail = tail.next.next
            head = head.next
        elif tail.next:
            return head.next
        else:
            return head

    
def excellent(head):
    # head: ListNode
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

if __name__ == '__main__':
    
    print(solution())
