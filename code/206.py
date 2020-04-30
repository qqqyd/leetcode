"""
206. 反转链表
反转一个单链表。
示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

我的思想：
用cur和pre指针依次遍历链表，用temp指针来储存cur.next

优解思想：
同

收获：
优解的代码更简洁，但思想是一样的，避免使用了临时变量，且他对于头指针的操作
也一起放进循环里做了

"""

def solution(head):
    # head: ListNode
    if head == None or head.next == None:
        return head
    pre = head
    cur = head.next
    head.next = None
    while cur is not None:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre
    

def excellent():
    if not head:
        return None
    pre = None
    cur = head
    while cur:
        cur.next, pre, cur = pre, cur, cur.next
    return prev

if __name__ == '__main__':
    solution()
