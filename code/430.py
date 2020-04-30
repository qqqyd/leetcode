"""
430. 扁平化多级双向链表
您将获得一个双向链表，除了下一个和前一个指针之外，它还有一个子指针，可能指向单独的双向链表。这些子列表可能有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。
扁平化列表，使所有结点出现在单级双链表中。您将获得列表第一级的头部。
示例:
输入:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
输出:
1-2-3-7-8-11-12-9-10-4-5-6-NULL

我的思想：
先正常往后走，如果碰到有子节点的，就把子节点所有加到主串来，不断往后

优解思想：
使用栈的思想，每次压进去一个新的结电，然后依次出来

收获：
要多使用堆栈的东西来搞算法

"""

def solution(head):
    # head: 'Node'
    cur = head
    while cur:
        if cur.child:
            cur.child.prev = cur

            temp = cur.child
            while temp.next:
                temp = temp.next
            if cur.next:
                cur.next.prev = temp
                temp.next = cur.next
                
            cur.next = cur.child
            cur.child = None
        cur = cur.next
    return head
    
    
def excellent(head):
    # head: 'Node'
    if not head:
        return

    pseudoHead = Node(None,None,head,None)
    prev = pseudoHead

    stack = []
    stack.append(head)

    while stack:
        curr = stack.pop()

        prev.next = curr
        curr.prev = prev

        if curr.next:
            stack.append(curr.next)
        if curr.child:
            stack.append(curr.child)
            curr.child = None
        prev = curr

    pseudoHead.next.prev = None
    return pseudoHead.next

if __name__ == '__main__':
    solution()
