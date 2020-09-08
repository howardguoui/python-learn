class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node3
node2.next = node4
##以下代码中以node2为头结点的链表有几个节点？ 3


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
##现在需要在node1和node2中间插入一个值为3的节点，下列代码正确的是？

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
## 现在要将链表的node2和node3引用的节点交换，下列代码正确的是？交换node2和node3所引用的节点对象，需要将node3连接在node1后，将node2连接在node3后，node4连接到node2后。
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3