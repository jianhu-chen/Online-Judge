# 第 341 场周赛

> 企业: 力扣

## 6376.一最多的行

[打开力扣](https://leetcode.cn/problems/row-with-maximum-ones) [我的代码](6376.row_with_maximum_ones.py)

给你一个大小为 <code>m x n</code> 的二进制矩阵 <code>mat</code> ，请你找出包含最多 <strong>1</strong> 的行的下标（从 <strong>0</strong> 开始）以及这一行中 <strong>1</strong> 的数目。

如果有多行包含最多的 1 ，只需要选择 <strong>行下标最小</strong> 的那一行。

返回一个由行下标和该行中 1 的数量组成的数组。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>mat = [[0,1],[1,0]]
<strong>输出：</strong>[0,1]
<strong>解释：</strong>两行中 1 的数量相同。所以返回下标最小的行，下标为 0 。该行 1 的数量为 1 。所以，答案为 [0,1] 。 
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>mat = [[0,0,0],[0,1,1]]
<strong>输出：</strong>[1,2]
<strong>解释：</strong>下标为 1 的行中 1 的数量最多<code>。</code>该行 1 的数量<code>为 2 。所以，答案为</code> [1,2] 。
</pre>

<strong>示例 3：</strong>

<pre>
<strong>输入：</strong>mat = [[0,0],[1,1],[0,0]]
<strong>输出：</strong>[1,2]
<strong>解释：</strong>下标为 1 的行中 1 的数量最多。该行 1 的数量<code>为 2 。所以，答案为</code> [1,2] 。</pre>



<strong>提示：</strong>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 <= m, n <= 100</code></li>
	<li><code>mat[i][j]</code> 为 <code>0</code> 或 <code>1</code></li>
</ul>

## 6350.找出可整除性得分最大的整数

[打开力扣](https://leetcode.cn/problems/find-the-maximum-divisibility-score) [我的代码](6350.find_the_maximum_divisibility_score.py)

给你两个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 和 <code>divisors</code> 。

<code>divisors[i]</code> 的 <strong>可整除性得分</strong> 等于满足 <code>nums[j]</code> 能被 <code>divisors[i]</code> 整除的下标 <code>j</code> 的数量。

返回 <strong>可整除性得分</strong> 最大的整数 <code>divisors[i]</code> 。如果有多个整数具有最大得分，则返回数值最小的一个。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>nums = [4,7,9,3,9], divisors = [5,2,3]
<strong>输出：</strong>3
<strong>解释：</strong>divisors 中每个元素的可整除性得分为：
divisors[0] 的可整除性得分为 0 ，因为 nums 中没有任何数字能被 5 整除。
divisors[1] 的可整除性得分为 1 ，因为 nums[0] 能被 2 整除。 
divisors[2] 的可整除性得分为 3 ，因为 nums[2]、nums[3] 和 nums[4] 都能被 3 整除。 
因此，返回 divisors[2] ，它的可整除性得分最大。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>nums = [20,14,21,10], divisors = [5,7,5]
<strong>输出：</strong>5
<strong>解释：</strong>divisors 中每个元素的可整除性得分为：
divisors[0] 的可整除性得分为 2 ，因为 nums[0] 和 nums[3] 都能被 5 整除。
divisors[1] 的可整除性得分为 2 ，因为 nums[1] 和 nums[2] 都能被 7 整除。
divisors[2] 的可整除性得分为 2 ，因为 nums[0] 和 nums[3] 都能被5整除。 
由于 divisors[0]、divisors[1] 和 divisors[2] 的可整除性得分都是最大的，因此，我们返回数值最小的一个，即 divisors[2] 。
</pre>

<strong>示例 3：</strong>

<pre>
<strong>输入：</strong>nums = [12], divisors = [10,16]
<strong>输出：</strong>10
<strong>解释：</strong>divisors 中每个元素的可整除性得分为：
divisors[0] 的可整除性得分为 0 ，因为 nums 中没有任何数字能被 10 整除。
divisors[1] 的可整除性得分为 0 ，因为 nums 中没有任何数字能被 16 整除。 
由于 divisors[0] 和 divisors[1] 的可整除性得分都是最大的，因此，我们返回数值最小的一个，即 divisors[0] 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length, divisors.length <= 1000</code></li>
	<li><code>1 <= nums[i], divisors[i] <= 10<sup>9</sup></code></li>
</ul>

## 6375.构造有效字符串的最少插入数

[打开力扣](https://leetcode.cn/problems/minimum-additions-to-make-valid-string) [我的代码](6375.minimum_additions_to_make_valid_string.py)

给你一个字符串 <code>word</code> ，你可以向其中任何位置插入 "a"、"b" 或 "c" 任意次，返回使 <code>word</code> <strong>有效</strong> 需要插入的最少字母数。

如果字符串可以由 "abc" 串联多次得到，则认为该字符串 <strong>有效</strong> 。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>word = "b"
<strong>输出：</strong>2
<strong>解释：</strong>在 "b" 之前插入 "a" ，在 "b" 之后插入 "c" 可以得到有效字符串 "<strong>a</strong>b<strong>c</strong>" 。
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>word = "aaa"
<strong>输出：</strong>6
<strong>解释：</strong>在每个 "a" 之后依次插入 "b" 和 "c" 可以得到有效字符串 "a<strong>bc</strong>a<strong>bc</strong>a<strong>bc</strong>" 。
</pre>

<strong>示例 3：</strong>

<pre><strong>输入：</strong>word = "abc"
<strong>输出：</strong>0
<strong>解释：</strong>word 已经是有效字符串，不需要进行修改。 
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= word.length <= 50</code></li>
	<li><code>word</code> 仅由字母 "a"、"b" 和 "c" 组成。</li>
</ul>

## 6378.最小化旅行的价格总和

[打开力扣](https://leetcode.cn/problems/minimize-the-total-price-of-the-trips) [我的代码](6378.minimize_the_total_price_of_the_trips.py)

现有一棵无向、无根的树，树中有 <code>n</code> 个节点，按从 <code>0</code> 到 <code>n - 1</code> 编号。给你一个整数 <code>n</code> 和一个长度为 <code>n - 1</code> 的二维整数数组 <code>edges</code> ，其中 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示树中节点 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 之间存在一条边。

每个节点都关联一个价格。给你一个整数数组 <code>price</code> ，其中 <code>price[i]</code> 是第 <code>i</code> 个节点的价格。

给定路径的 <strong>价格总和</strong> 是该路径上所有节点的价格之和。

另给你一个二维整数数组 <code>trips</code> ，其中 <code>trips[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> 表示您从节点 <code>start<sub>i</sub></code> 开始第 <code>i</code> 次旅行，并通过任何你喜欢的路径前往节点 <code>end<sub>i</sub></code> 。

在执行第一次旅行之前，你可以选择一些 <strong>非相邻节点</strong> 并将价格减半。

返回执行所有旅行的最小价格总和。



<strong>示例 1：</strong>
<img alt="" src="https://assets.leetcode.com/uploads/2023/03/16/diagram2.png" style="width: 541px; height: 181px;">
<pre><strong>输入：</strong>n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]
<strong>输出：</strong>23
<strong>解释：
</strong>上图表示将节点 2 视为根之后的树结构。第一个图表示初始树，第二个图表示选择节点 0 、2 和 3 并使其价格减半后的树。
第 1 次旅行，选择路径 [0,1,3] 。路径的价格总和为 1 + 2 + 3 = 6 。
第 2 次旅行，选择路径 [2,1] 。路径的价格总和为 2 + 5 = 7 。
第 3 次旅行，选择路径 [2,1,3] 。路径的价格总和为 5 + 2 + 3 = 10 。
所有旅行的价格总和为 6 + 7 + 10 = 23 。可以证明，23 是可以实现的最小答案。</pre>

<strong>示例 2：</strong>
<img alt="" src="https://assets.leetcode.com/uploads/2023/03/16/diagram3.png" style="width: 456px; height: 111px;">
<pre><strong>输入：</strong>n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]
<strong>输出：</strong>1
<strong>解释：</strong>
上图表示将节点 0 视为根之后的树结构。第一个图表示初始树，第二个图表示选择节点 0 并使其价格减半后的树。 
第 1 次旅行，选择路径 [0] 。路径的价格总和为 1 。 
所有旅行的价格总和为 1 。可以证明，1 是可以实现的最小答案。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= n <= 50</code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>0 <= a<sub>i</sub>, b<sub>i</sub> <= n - 1</code></li>
	<li><code>edges</code> 表示一棵有效的树</li>
	<li><code>price.length == n</code></li>
	<li><code>price[i]</code> 是一个偶数</li>
	<li><code>1 <= price[i] <= 1000</code></li>
	<li><code>1 <= trips.length <= 100</code></li>
	<li><code>0 <= start<sub>i</sub>, end<sub>i</sub><= n - 1</code></li>
</ul>
