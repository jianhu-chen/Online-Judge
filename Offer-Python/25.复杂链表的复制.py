## 题目描述
# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
# 返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return pHead
        nodes = []
        while pHead:
            nodes.append(pHead)
            copy_node= RandomListNode(pHead.label)
            copy_node.next = pHead.next
            pHead.next = copy_node
            nodes.append(copy_node)
            pHead = pHead.next.next

        for i, node in enumerate(nodes):
            if i%2 == 0 and node.random:
                node.next.random = node.random.next
            
        for i, node in enumerate(nodes):
            if i%2 != 0 and node.next:
                node.next = node.next.next
        return nodes[1]


if __name__ == "__main__":
    # make test data, len = 3
    dataHead = RandomListNode(1)
    nextNode = RandomListNode(2)
    dataHead.next = nextNode
    dataHead.random = nextNode
    nnextNode = RandomListNode(3)
    nextNode.next = nnextNode
    nextNode.random = dataHead
    s = Solution()
    resultHead = s.Clone(dataHead)
    while resultHead:
        print(resultHead.label)
        resultHead = resultHead.next