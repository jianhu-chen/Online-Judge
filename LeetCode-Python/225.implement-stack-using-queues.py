# -*- encoding: utf-8 -*-
'''
@File    :   225.implement-stack-using-queues.py
@Time    :   2020/01/31 16:48:19
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=225 lang=python
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = list()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue.insert(0, x)
        for i in range(len(self.queue)-1):
            self.queue.insert(0, self.queue.pop())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queue.pop()
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

