"""
21. 合并两个有序链表
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

我的思想：
简单合并

优解思想：

收获：

"""

def solution(l1, l2):
    # l1: ListNode, l2: ListNode
    head = ListNode(0)
        cur = head
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 if l1 else l2
    return head.next
    
def excellent():
    pass

if __name__ == '__main__':
    print(solution())
