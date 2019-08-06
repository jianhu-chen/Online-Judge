## 题目描述
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

# 输入描述:
# >题目保证输入的数组中没有的相同的数字
# >
# >数据范围：
# >
# >	对于%50的数据,size<=10^4
# >
# >	对于%75的数据,size<=10^5
# >
# >	对于%100的数据,size<=2*10^5

class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0
        count=0
        for i in range(len(data)):
            for j in range(0,i):
                if data[j]>data[i]:
                    count += 1
        return count%1000000007
    def merge(self, l1, l2):