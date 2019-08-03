# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not popV or len(pushV) != len(popV):
            return False
        stack = []
        for e in pushV:
            stack.append(e)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        return True

if __name__ == "__main__":
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 5, 3, 2, 1]
    s = Solution()
    result = s.IsPopOrder(pushV, popV)
    print(result)
