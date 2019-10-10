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

import copy


# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        # 分治思想：左边数组中的逆序对的数量 + 右边数组中逆序对的数量 + 左右结合成新的顺序数组时
        # 中出现的逆序对的数量
        if not data:
            return 0
        data_copy = copy.deepcopy(data)
        count = self.mergeSort(data, data_copy, 0, len(data) - 1)
        return count%1000000007
       
    def mergeSort(self, data, data_copy, low, high):
        '''归并排序并统计逆序对
        '''
        if low == high:
            data_copy[low] = data[low]
            return 0

        mid = int((low + high) / 2)
        left = self.mergeSort(data_copy, data, low, mid)
        right = self.mergeSort(data_copy, data, mid+1, high)
           
        count = 0
        i = mid
        j = high
        copy_index = high
        while i >= low and j >= mid + 1:
            if data[i] > data[j]:
                data_copy[copy_index] = data[i]
                i -= 1
                copy_index -= 1
                count += j - mid
            else:
                data_copy[copy_index] = data[j]
                j -= 1
                copy_index -= 1
        
        while i >= low:
            data_copy[copy_index] = data[i]
            i -= 1
            copy_index -= 1
        
        while j >= mid + 1:
            data_copy[copy_index] = data[j]
            j -= 1
            copy_index -= 1

        return count + left + right


if __name__ == "__main__":
    test_data = [1,2,3,4,5,6,7,0]
    s = Solution()
    c = s.InversePairs(test_data)
    print(c)