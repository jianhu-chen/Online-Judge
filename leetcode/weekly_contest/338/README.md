# 第 338 场周赛

> 企业: FNZ

## 6354.K 件物品的最大和

[打开力扣](https://leetcode.cn/problems/k-items-with-the-maximum-sum) [我的代码](6354.k_items_with_the_maximum_sum.py)

袋子中装有一些物品，每个物品上都标记着数字 <code>1</code> 、<code>0</code> 或 <code>-1</code> 。

给你四个非负整数 <code>numOnes</code> 、<code>numZeros</code> 、<code>numNegOnes</code> 和 <code>k</code> 。

袋子最初包含：

<ul>
	<li><code>numOnes</code> 件标记为 <code>1</code> 的物品。</li>
	<li><code>numZeroes</code> 件标记为 <code>0</code> 的物品。</li>
	<li><code>numNegOnes</code> 件标记为 <code>-1</code> 的物品。</li>
</ul>

现计划从这些物品中恰好选出 <code>k</code> 件物品。返回所有可行方案中，物品上所标记数字之和的最大值。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2
<strong>输出：</strong>2
<strong>解释：</strong>袋子中的物品分别标记为 {1, 1, 1, 0, 0} 。取 2 件标记为 1 的物品，得到的数字之和为 2 。
可以证明 2 是所有可行方案中的最大值。</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4
<strong>输出：</strong>3
<strong>解释：</strong>袋子中的物品分别标记为 {1, 1, 1, 0, 0} 。取 3 件标记为 1 的物品，1 件标记为 0 的物品，得到的数字之和为 3 。
可以证明 3 是所有可行方案中的最大值。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>0 <= numOnes, numZeros, numNegOnes <= 50</code></li>
	<li><code>0 <= k <= numOnes + numZeros + numNegOnes</code></li>
</ul>

## 6355.质数减法运算

[打开力扣](https://leetcode.cn/problems/prime-subtraction-operation) [我的代码](6355.prime_subtraction_operation.py)

给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> ，数组长度为 <code>n</code> 。

你可以执行无限次下述运算：

<ul>
	<li>选择一个之前未选过的下标 <code>i</code> ，并选择一个 <strong>严格小于</strong> <code>nums[i]</code> 的质数 <code>p</code> ，从 <code>nums[i]</code> 中减去 <code>p</code> 。</li>
</ul>

如果你能通过上述运算使得 <code>nums</code> 成为严格递增数组，则返回 <code>true</code> ；否则返回 <code>false</code> 。

<strong>严格递增数组</strong> 中的每个元素都严格大于其前面的元素。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>nums = [4,9,6,10]
<strong>输出：</strong>true
<strong>解释：</strong>
在第一次运算中：选择 i = 0 和 p = 3 ，然后从 nums[0] 减去 3 ，nums 变为 [1,9,6,10] 。
在第二次运算中：选择 i = 1 和 p = 7 ，然后从 nums[1] 减去 7 ，nums 变为 [1,2,6,10] 。
第二次运算后，nums 按严格递增顺序排序，因此答案为 true 。</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>nums = [6,8,11,12]
<strong>输出：</strong>true
<strong>解释：</strong>nums 从一开始就按严格递增顺序排序，因此不需要执行任何运算。</pre>

<strong>示例 3：</strong>

<pre>
<strong>输入：</strong>nums = [5,8,3]
<strong>输出：</strong>false
<strong>解释：</strong>可以证明，执行运算无法使 nums 按严格递增顺序排序，因此答案是 false 。</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 1000</code></li>
	<li><code>1 <= nums[i] <= 1000</code></li>
	<li><code>nums.length == n</code></li>
</ul>

## 6357.使数组元素全部相等的最少操作次数

[打开力扣](https://leetcode.cn/problems/minimum-operations-to-make-all-array-elements-equal) [我的代码](6357.minimum_operations_to_make_all_array_elements_equal.py)

给你一个正整数数组<code>nums</code>。

同时给你一个长度为 <code>m</code>的整数数组<code>queries</code>。第 <code>i</code>个查询中，你需要将 <code>nums</code>中所有元素变成<code>queries[i]</code>。你可以执行以下操作<strong>任意</strong>次：

<ul>
	<li>将数组里一个元素<strong>增大</strong>或者<strong>减小</strong><code>1</code>。</li>
</ul>

请你返回一个长度为 <code>m</code>的数组<em></em><code>answer</code>，其中<em></em><code>answer[i]</code>是将<code>nums</code>中所有元素变成<code>queries[i]</code>的<strong>最少</strong>操作次数。

<strong>注意</strong>，每次查询后，数组变回最开始的值。



<strong>示例 1：</strong>

<pre><b>输入：</b>nums = [3,1,6,8], queries = [1,5]
<b>输出：</b>[14,10]
<b>解释：</b>第一个查询，我们可以执行以下操作：
- 将 nums[0] 减小 2 次，nums = [1,1,6,8] 。
- 将 nums[2] 减小 5 次，nums = [1,1,1,8] 。
- 将 nums[3] 减小 7 次，nums = [1,1,1,1] 。
第一个查询的总操作次数为 2 + 5 + 7 = 14 。
第二个查询，我们可以执行以下操作：
- 将 nums[0] 增大 2 次，nums = [5,1,6,8] 。
- 将 nums[1] 增大 4 次，nums = [5,5,6,8] 。
- 将 nums[2] 减小 1 次，nums = [5,5,5,8] 。
- 将 nums[3] 减小 3 次，nums = [5,5,5,5] 。
第二个查询的总操作次数为 2 + 4 + 1 + 3 = 10 。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>nums = [2,9,6,3], queries = [10]
<b>输出：</b>[20]
<b>解释：</b>我们可以将数组中所有元素都增大到 10 ，总操作次数为 8 + 1 + 4 + 7 = 20 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>m == queries.length</code></li>
	<li><code>1 <= n, m <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i], queries[i] <= 10<sup>9</sup></code></li>
</ul>

## 6356.收集树中金币

[打开力扣](https://leetcode.cn/problems/collect-coins-in-a-tree) [我的代码](6356.collect_coins_in_a_tree.py)

给你一个 <code>n</code>个节点的无向无根树，节点编号从<code>0</code>到<code>n - 1</code>。给你整数<code>n</code>和一个长度为 <code>n - 1</code>的二维整数数组 <code>edges</code>，其中<code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>表示树中节点<code>a<sub>i</sub></code> 和<code>b<sub>i</sub></code>之间有一条边。再给你一个长度为 <code>n</code>的数组<code>coins</code>，其中<code>coins[i]</code> 可能为<code>0</code>也可能为<code>1</code>，<code>1</code>表示节点 <code>i</code>处有一个金币。

一开始，你需要选择树中任意一个节点出发。你可以执行下述操作任意次：

<ul>
	<li>收集距离当前节点距离为 <code>2</code>以内的所有金币，或者</li>
	<li>移动到树中一个相邻节点。</li>
</ul>

你需要收集树中所有的金币，并且回到出发节点，请你返回最少经过的边数。

如果你多次经过一条边，每一次经过都会给答案加一。



<strong>示例 1：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2023/03/01/graph-2.png" style="width: 522px; height: 522px;">

<pre><b>输入：</b>coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]
<b>输出：</b>2
<b>解释：</b>从节点 2 出发，收集节点 0 处的金币，移动到节点 3 ，收集节点 5 处的金币，然后移动回节点 2 。
</pre>

<strong>示例 2：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2023/03/02/graph-4.png" style="width: 522px; height: 522px;">

<pre><b>输入：</b>coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]
<b>输出：</b>2
<b>解释：</b>从节点 0 出发，收集节点 4 和 3 处的金币，移动到节点 2 处，收集节点 7 处的金币，移动回节点 0 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>n == coins.length</code></li>
	<li><code>1 <= n <= 3 * 10<sup>4</sup></code></li>
	<li><code>0 <= coins[i] <= 1</code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 <= a<sub>i</sub>, b<sub>i</sub> < n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>edges</code>表示一棵合法的树。</li>
</ul>
