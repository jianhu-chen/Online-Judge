# 第 102 场双周赛

> 企业: 力扣

## 6333.查询网格图中每一列的宽度

[打开力扣](https://leetcode.cn/problems/find-the-width-of-columns-of-a-grid) [我的代码](6333.find_the_width_of_columns_of_a_grid.py)

给你一个下标从 <strong>0</strong>开始的<code>m x n</code>整数矩阵<code>grid</code>。矩阵中某一列的宽度是这一列数字的最大 <strong>字符串长度</strong>。

<ul>
	<li>比方说，如果<code>grid = [[-10], [3], [12]]</code>，那么唯一一列的宽度是<code>3</code>，因为<code>-10</code>的字符串长度为<code>3</code>。</li>
</ul>

请你返回一个大小为 <code>n</code>的整数数组<code>ans</code>，其中<code>ans[i]</code>是第<code>i</code>列的宽度。

一个有 <code>len</code>个数位的整数 <code>x</code>，如果是非负数，那么<strong>字符串</strong><strong>长度</strong>为<code>len</code>，否则为<code>len + 1</code>。



<strong>示例 1：</strong>

<pre><b>输入：</b>grid = [[1],[22],[333]]
<b>输出：</b>[3]
<b>解释：</b>第 0 列中，333 字符串长度为 3 。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>grid = [[-15,1,3],[15,7,12],[5,6,-2]]
<b>输出：</b>[3,1,2]
<b>解释：</b>
第 0 列中，只有 -15 字符串长度为 3 。
第 1 列中，所有整数的字符串长度都是 1 。
第 2 列中，12 和 -2 的字符串长度都为 2 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 <= m, n <= 100 </code></li>
	<li><code>-10<sup>9</sup> <= grid[r][c] <= 10<sup>9</sup></code></li>
</ul>

## 6334.一个数组所有前缀的分数

[打开力扣](https://leetcode.cn/problems/find-the-score-of-all-prefixes-of-an-array) [我的代码](6334.find_the_score_of_all_prefixes_of_an_array.py)

定义一个数组 <code>arr</code>的 <strong>转换数组</strong><code>conver</code>为：

<ul>
	<li><code>conver[i] = arr[i] + max(arr[0..i])</code>，其中<code>max(arr[0..i])</code>是满足 <code>0 <= j <= i</code>的所有<code>arr[j]</code>中的最大值。</li>
</ul>

定义一个数组 <code>arr</code>的 <strong>分数</strong>为 <code>arr</code>转换数组中所有元素的和。

给你一个下标从 <strong>0</strong>开始长度为 <code>n</code>的整数数组<code>nums</code>，请你返回一个长度为 <code>n</code>的数组<em></em><code>ans</code>，其中<code>ans[i]</code>是前缀<code>nums[0..i]</code>的分数。



<strong>示例 1：</strong>

<pre><b>输入：</b>nums = [2,3,7,5,10]
<b>输出：</b>[4,10,24,36,56]
<b>解释：</b>
对于前缀 [2] ，转换数组为 [4] ，所以分数为 4 。
对于前缀 [2, 3] ，转换数组为 [4, 6] ，所以分数为 10 。
对于前缀 [2, 3, 7] ，转换数组为 [4, 6, 14] ，所以分数为 24 。
对于前缀 [2, 3, 7, 5] ，转换数组为 [4, 6, 14, 12] ，所以分数为 36 。
对于前缀 [2, 3, 7, 5, 10] ，转换数组为 [4, 6, 14, 12, 20] ，所以分数为 56 。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>nums = [1,1,2,4,8,16]
<b>输出：</b>[2,4,8,16,32,64]
<b>解释：</b>
对于前缀 [1] ，转换数组为 [2] ，所以分数为 2 。
对于前缀 [1, 1]，转换数组为 [2, 2] ，所以分数为 4 。
对于前缀 [1, 1, 2]，转换数组为 [2, 2, 4] ，所以分数为 8 。
对于前缀 [1, 1, 2, 4]，转换数组为 [2, 2, 4, 8] ，所以分数为 16 。
对于前缀 [1, 1, 2, 4, 8]，转换数组为 [2, 2, 4, 8, 16] ，所以分数为 32 。
对于前缀 [1, 1, 2, 4, 8, 16]，转换数组为 [2, 2, 4, 8, 16, 32] ，所以分数为 64 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i] <= 10<sup>9</sup></code></li>
</ul>

## 6335.二叉树的堂兄弟节点 II

[打开力扣](https://leetcode.cn/problems/cousins-in-binary-tree-ii) [我的代码](6335.cousins_in_binary_tree_ii.py)

给你一棵二叉树的根<code>root</code>，请你将每个节点的值替换成该节点的所有 <strong>堂兄弟节点值的和</strong>。

如果两个节点在树中有相同的深度且它们的父节点不同，那么它们互为 <strong>堂兄弟</strong>。

请你返回修改值之后，树的根<em></em><code>root</code><em></em>。

<strong>注意</strong>，一个节点的深度指的是从树根节点到这个节点经过的边数。



<strong>示例 1：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2023/01/11/example11.png" style="width: 571px; height: 151px;" />

<pre>
<b>输入：</b>root = [5,4,9,1,10,null,7]
<b>输出：</b>[0,0,0,7,7,null,11]
<b>解释：</b>上图展示了初始的二叉树和修改每个节点的值之后的二叉树。
- 值为 5 的节点没有堂兄弟，所以值修改为 0 。
- 值为 4 的节点没有堂兄弟，所以值修改为 0 。
- 值为 9 的节点没有堂兄弟，所以值修改为 0 。
- 值为 1 的节点有一个堂兄弟，值为 7 ，所以值修改为 7 。
- 值为 10 的节点有一个堂兄弟，值为 7 ，所以值修改为 7 。
- 值为 7 的节点有两个堂兄弟，值分别为 1 和 10 ，所以值修改为 11 。
</pre>

<strong>示例 2：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2023/01/11/diagram33.png" style="width: 481px; height: 91px;" />

<pre>
<b>输入：</b>root = [3,1,2]
<b>输出：</b>[0,0,0]
<b>解释：</b>上图展示了初始的二叉树和修改每个节点的值之后的二叉树。
- 值为 3 的节点没有堂兄弟，所以值修改为 0 。
- 值为 1 的节点没有堂兄弟，所以值修改为 0 。
- 值为 2 的节点没有堂兄弟，所以值修改为 0 。
</pre>



<strong>提示：</strong>

<ul>
	<li>树中节点数目的范围是<code>[1, 10<sup>5</sup>]</code> 。</li>
	<li><code>1 <= Node.val <= 10<sup>4</sup></code></li>
</ul>

## 2642.设计可以求最短路径的图类

[打开力扣](https://leetcode.cn/problems/design-graph-with-shortest-path-calculator) [我的代码](2642.design_graph_with_shortest_path_calculator.py)

给你一个有<code>n</code>个节点的<strong>有向带权</strong>图，节点编号为<code>0</code>到<code>n - 1</code>。图中的初始边用数组<code>edges</code>表示，其中<code>edges[i] = [from<sub>i</sub>, to<sub>i</sub>, edgeCost<sub>i</sub>]</code>表示从<code>from<sub>i</sub></code>到<code>to<sub>i</sub></code>有一条代价为<code>edgeCost<sub>i</sub></code>的边。

请你实现一个<code>Graph</code>类：

<ul>
	<li><code>Graph(int n, int[][] edges)</code>初始化图有<code>n</code>个节点，并输入初始边。</li>
	<li><code>addEdge(int[] edge)</code>向边集中添加一条边，其中<strong></strong><code>edge = [from, to, edgeCost]</code>。数据保证添加这条边之前对应的两个节点之间没有有向边。</li>
	<li><code>int shortestPath(int node1, int node2)</code>返回从节点<code>node1</code>到<code>node2</code>的路径<strong>最小</strong>代价。如果路径不存在，返回<code>-1</code>。一条路径的代价是路径中所有边代价之和。</li>
</ul>



<strong>示例 1：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2023/01/11/graph3drawio-2.png" style="width: 621px; height: 191px;">

<pre><strong>输入：</strong>
["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
[[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
<b>输出：</b>
[null, 6, -1, null, 6]

<strong>解释：</strong>
Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
g.shortestPath(3, 2); // 返回 6 。从 3 到 2 的最短路径如第一幅图所示：3 -> 0 -> 1 -> 2 ，总代价为 3 + 2 + 1 = 6 。
g.shortestPath(0, 3); // 返回 -1 。没有从 0 到 3 的路径。
g.addEdge([1, 3, 4]); // 添加一条节点 1 到节点 3 的边，得到第二幅图。
g.shortestPath(0, 3); // 返回 6 。从 0 到 3 的最短路径为 0 -> 1 -> 3 ，总代价为 2 + 4 = 6 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= n <= 100</code></li>
	<li><code>0 <= edges.length <= n * (n - 1)</code></li>
	<li><code>edges[i].length == edge.length == 3</code></li>
	<li><code>0 <= from<sub>i</sub>, to<sub>i</sub>, from, to, node1, node2 <= n - 1</code></li>
	<li><code>1 <= edgeCost<sub>i</sub>, edgeCost <= 10<sup>6</sup></code></li>
	<li>图中任何时候都不会有重边和自环。</li>
	<li>调用 <code>addEdge</code>至多<code>100</code>次。</li>
	<li>调用 <code>shortestPath</code>至多<code>100</code>次。</li>
</ul>
