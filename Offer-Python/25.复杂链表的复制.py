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
        pRoot = pHead
        
        # 复制结点
        while pHead:
            copy_node= RandomListNode(pHead.label)
            copy_node.next = pHead.next
            pHead.next = copy_node
            pHead = pHead.next.next
        
        # 调整随机指针
        pHead = pRoot
        while pHead.random: # random 指针存在时才需要调整
            try:
                pHead.next.random = pHead.random.next
                pHead = pHead.next.next
            except:
                break
        
        # 连接新结点
        pHead = pRoot
        while pHead:
            try:
                pHead.next.next = pHead.next.next.next
                pHead = pHead.next.next
            except:
                break
        return pRoot.next

if __name__ == "__main__":
    # make test data, len = 3
    dataHead = RandomListNode(1)
    nextNode = RandomListNode(2)
    dataHead.next = nextNode
    dataHead.random = nextNode
    nnextNode = RandomListNode(3)
    nextNode.next = nnextNode
    nextNode.random = nextNode
    s = Solution()
    resultHead = s.Clone(dataHead)
    while resultHead:
        print(resultHead.label)
        resultHead = resultHead.next
