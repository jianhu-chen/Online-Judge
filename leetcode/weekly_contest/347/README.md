# 第 347 场周赛

> 企业: 力扣

## 6457.移除字符串中的尾随零

[打开力扣](https://leetcode.cn/problems/remove-trailing-zeros-from-a-string) [我的代码](6457.remove_trailing_zeros_from_a_string.py)

给你一个用字符串表示的正整数 <code>num</code> ，请你以字符串形式返回不含尾随零的整数<em> </em><code>num</code><em> </em>。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>num = "51230100"
<strong>输出：</strong>"512301"
<strong>解释：</strong>整数 "51230100" 有 2 个尾随零，移除并返回整数 "512301" 。
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>num = "123"
<strong>输出：</strong>"123"
<strong>解释：</strong>整数 "123" 不含尾随零，返回整数 "123" 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= num.length <= 1000</code></li>
	<li><code>num</code> 仅由数字 <code>0</code> 到 <code>9</code> 组成</li>
	<li><code>num</code> 不含前导零</li>
</ul>

## 2711.对角线上不同值的数量差

[打开力扣](https://leetcode.cn/problems/difference-of-number-of-distinct-values-on-diagonals) [我的代码](2711.difference_of_number_of_distinct_values_on_diagonals.py)

给你一个下标从 <code>0</code> 开始、大小为 <code>m x n</code> 的二维矩阵 <code>grid</code> ，请你求解大小同样为 <code>m x n</code> 的答案矩阵 <code>answer</code> 。

矩阵 <code>answer</code> 中每个单元格 <code>(r, c)</code> 的值可以按下述方式进行计算：

<ul>
	<li>令 <code>topLeft[r][c]</code> 为矩阵 <code>grid</code> 中单元格 <code>(r, c)</code> 左上角对角线上 <strong>不同值</strong> 的数量。</li>
	<li>令 <code>bottomRight[r][c]</code> 为矩阵 <code>grid</code> 中单元格 <code>(r, c)</code> 右下角对角线上 <strong>不同值</strong> 的数量。</li>
</ul>

然后 <code>answer[r][c] = |topLeft[r][c] - bottomRight[r][c]|</code> 。

返回矩阵 <code>answer</code> 。

<strong>矩阵对角线</strong> 是从最顶行或最左列的某个单元格开始，向右下方向走到矩阵末尾的对角线。

如果单元格 <code>(r1, c1)</code> 和单元格 <code>(r, c) </code>属于同一条对角线且 <code>r1 < r</code> ，则单元格 <code>(r1, c1)</code> 属于单元格 <code>(r, c)</code> 的左上对角线。类似地，可以定义右下对角线。



<strong>示例 1：</strong>
<img alt="" src="https://assets.leetcode.com/uploads/2023/04/19/ex2.png" style="width: 786px; height: 121px;" />
<pre>
<strong>输入：</strong>grid = [[1,2,3],[3,1,5],[3,2,1]]
<strong>输出：</strong>[[1,1,0],[1,0,1],[0,1,1]]
<strong>解释：</strong>第 1 个图表示最初的矩阵 grid 。
第 2 个图表示对单元格 (0,0) 计算，其中蓝色单元格是位于右下对角线的单元格。
第 3 个图表示对单元格 (1,2) 计算，其中红色单元格是位于左上对角线的单元格。
第 4 个图表示对单元格 (1,1) 计算，其中蓝色单元格是位于右下对角线的单元格，红色单元格是位于左上对角线的单元格。
- 单元格 (0,0) 的右下对角线包含 [1,1] ，而左上对角线包含 [] 。对应答案是 |1 - 0| = 1 。
- 单元格 (1,2) 的右下对角线包含 [] ，而左上对角线包含 [2] 。对应答案是 |0 - 1| = 1 。
- 单元格 (1,1) 的右下对角线包含 [1] ，而左上对角线包含 [1] 。对应答案是 |1 - 1| = 0 。
其他单元格的对应答案也可以按照这样的流程进行计算。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>grid = [[1]]
<strong>输出：</strong>[[0]]
<strong>解释：</strong>- 单元格 (0,0) 的右下对角线包含 [] ，左上对角线包含 [] 。对应答案是 |0 - 0| = 0 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 <= m, n, grid[i][j] <= 50</code></li>
</ul>

## 6455.使所有字符相等的最小成本

[打开力扣](https://leetcode.cn/problems/minimum-cost-to-make-all-characters-equal) [我的代码](6455.minimum_cost_to_make_all_characters_equal.py)

给你一个下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的二进制字符串 <code>s</code> ，你可以对其执行两种操作：

<ul>
	<li>选中一个下标 <code>i</code> 并且反转从下标 <code>0</code> 到下标 <code>i</code>（包括下标 <code>0</code> 和下标 <code>i</code> ）的所有字符，成本为 <code>i + 1</code> 。</li>
	<li>选中一个下标 <code>i</code> 并且反转从下标 <code>i</code> 到下标 <code>n - 1</code>（包括下标 <code>i</code> 和下标 <code>n - 1</code> ）的所有字符，成本为 <code>n - i</code> 。</li>
</ul>

返回使字符串内所有字符 <strong>相等</strong> 需要的 <strong>最小成本</strong> 。

<strong>反转</strong> 字符意味着：如果原来的值是 '0' ，则反转后值变为 '1' ，反之亦然。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>s = "0011"
<strong>输出：</strong>2
<strong>解释：</strong>执行第二种操作，选中下标 <code>i = 2</code> ，可以得到 <code>s = "0000" ，成本为 2</code> 。可以证明 2 是使所有字符相等的最小成本。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>s = "010101"
<strong>输出：</strong>9
<strong>解释：</strong>执行第一种操作，选中下标 i = 2 ，可以得到 s = "101101" ，成本为 3 。
执行第一种操作，选中下标 i = 1 ，可以得到 s = "011101" ，成本为 2 。
执行第一种操作，选中下标 i = 0 ，可以得到 s = "111101" ，成本为 1 。
执行第二种操作，选中下标 i = 4 ，可以得到 s = "111110" ，成本为 2 。
执行第一种操作，选中下标 i = 5 ，可以得到 s = "111111" ，成本为 1 。
使所有字符相等的总成本等于 9 。可以证明 9 是使所有字符相等的最小成本。 </pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= s.length == n <= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>

## 6456.矩阵中严格递增的单元格数

[打开力扣](https://leetcode.cn/problems/maximum-strictly-increasing-cells-in-a-matrix) [我的代码](6456.maximum_strictly_increasing_cells_in_a_matrix.py)

给你一个下标从 <strong>1</strong> 开始、大小为 <code>m x n</code> 的整数矩阵 <code>mat</code>，你可以选择任一单元格作为 <strong>起始单元格</strong> 。

从起始单元格出发，你可以移动到 <strong>同一行或同一列</strong> 中的任何其他单元格，但前提是目标单元格的值<strong> 严格大于 </strong>当前单元格的值。

你可以多次重复这一过程，从一个单元格移动到另一个单元格，直到无法再进行任何移动。

请你找出从某个单元开始访问矩阵所能访问的 <strong>单元格的最大数量</strong> 。

返回一个表示可访问单元格最大数量的整数。



<strong>示例 1：</strong>

<strong><img alt="" src="https://assets.leetcode.com/uploads/2023/04/23/diag1drawio.png" style="width: 200px; height: 176px;"></strong>

<pre><strong>输入：</strong>mat = [[3,1],[3,4]]
<strong>输出：</strong>2
<strong>解释：</strong>上图展示了从第 1 行、第 2 列的单元格开始，可以访问 2 个单元格。可以证明，无论从哪个单元格开始，最多只能访问 2 个单元格，因此答案是 2 。 
</pre>

<strong>示例 2：</strong>

<strong><img alt="" src="https://assets.leetcode.com/uploads/2023/04/23/diag3drawio.png" style="width: 200px; height: 176px;"></strong>

<pre><strong>输入：</strong>mat = [[1,1],[1,1]]
<strong>输出：</strong>1
<strong>解释：</strong>由于目标单元格必须严格大于当前单元格，在本示例中只能访问 1 个单元格。 
</pre>

<strong>示例 3：</strong>

<strong><img alt="" src="https://assets.leetcode.com/uploads/2023/04/23/diag4drawio.png" style="width: 350px; height: 250px;"></strong>

<pre><strong>输入：</strong>mat = [[3,1,6],[-9,5,7]]
<strong>输出：</strong>4
<strong>解释：</strong>上图展示了从第 2 行、第 1 列的单元格开始，可以访问 4 个单元格。可以证明，无论从哪个单元格开始，最多只能访问 4 个单元格，因此答案是 4 。  
</pre>



<strong>提示：</strong>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 <= m, n <= 10<sup>5</sup></code></li>
	<li><code>1 <= m * n <= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup><= mat[i][j] <= 10<sup>5</sup></code></li>
</ul>
