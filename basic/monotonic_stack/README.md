## 单调栈

对于数组中每个元素, 求离它最近的大于它的值时, 使用**单调递减栈**, 否则使用**单调递增栈**.

代码块 (以**单调递增栈**为例):

- 严格左右边界

    ```python
    left, right = [None] * n, [None] * n

    stack: List[int] = []
    for i in range(n):
        while stack and heights[i] <= heights[stack[-1]]:
            stack.pop()
        left[i] = stack[-1] if stack else None
        stack.append(i)

    stack: List[int] = []
    for i in range(n - 1, -1, -1):  # 从右往左遍历
        while stack and heights[i] <= heights[stack[-1]]:
            stack.pop()
        right[i] = stack[-1] if stack else None
        stack.append(i)
    ```

- 左严格, 右不严格
  
    ```python
    left, right = [None] * n, [None] * n
    stack: List[int] = []
    for i in range(n):
        while stack and heights[i] <= heights[stack[-1]]:
            top = stack.pop()
            right[top] = i  # 非严格
        # 准备入栈前记录i下标的左侧边界
        left[i] = stack[-1] if stack else None
        stack.append(i)
    ```

## 相关题目

- [接雨水](trapping_rain_water.py)

- [柱状图中最大的矩形](largest_rectangle_in_histogram.py)

- [子数组最小乘积的最大值](maximum_subarray_min_product.py)


