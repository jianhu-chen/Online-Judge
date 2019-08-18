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

# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        # 分治思想：左边数组中的逆序对的数量 + 右边数组中逆序对的数量 + 左右结合成新的顺序数组时
        # 中出现的逆序对的数量
        if not data:
            return 0
        

# # -*- coding:utf-8 -*-
# class Solution:
#     def InversePairs(self, data):
#         # write code here
#         if not data:
#             return 0
#         temp = [i for i in data]
#         return self.mergeSort(temp, data, 0, len(data)-1) % 1000000007
       
#     def mergeSort(self, temp, data, low, high):
#         if low >= high:
#             temp[low] = data[low]
#             return 0
#         mid = (low + high) / 2
#         left = self.mergeSort(data, temp, low, mid)
#         right = self.mergeSort(data, temp, mid+1, high)
           
#         count = 0
#         i = low
#         j = mid+1
#         index = low
#         while i <= mid and j <= high:
#             if data[i] <= data[j]:
#                 temp[index] = data[i]
#                 i += 1
#             else:
#                 temp[index] = data[j]
#                 count += mid-i+1
#                 j += 1
#             index += 1
#         while i <= mid:
#             temp[index] = data[i]
#             i += 1
#             index += 1
#         while j <= high:
#             temp[index] = data[j]
#             j += 1
#             index += 1
#         return count + left + right