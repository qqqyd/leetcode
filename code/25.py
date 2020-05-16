"""
25. K 个一组翻转链表
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
示例：
给你这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

我的思想：
从子链表翻转入手，翻转完子链表后再接入大链表里面

优解思想：

收获：
链表操作为了简便，可以自己申请一个单独的头空间

"""

class Solution:
    def reverse_sub(self, head: ListNode, tail: ListNode):
        pre = tail.next
        p = head
        while pre != tail:
            p.next, pre, p = pre, p, p.next
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next

            next_part_head = tail.next
            head, tail = self.reverse_sub(head, tail)
            
            pre.next = head
            pre = tail
            tail.next = next_part_head
            head = next_part_head

        return hair.next

    
def excellent():
    pass

if __name__ == '__main__':
    
    print(solution())
