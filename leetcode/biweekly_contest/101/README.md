# 第 101 场双周赛

> 企业: 微观博易

## 2605.从两个数字数组里生成最小数字

[打开力扣](https://leetcode.cn/problems/form-smallest-number-from-two-digit-arrays) [我的代码](2605.form_smallest_number_from_two_digit_arrays.py)

给你两个只包含 1 到 9 之间数字的数组<code>nums1</code> 和<code>nums2</code>，每个数组中的元素 <strong>互不相同</strong>，请你返回 <strong>最小</strong> 的数字，两个数组都 <strong>至少</strong> 包含这个数字的某个数位。


<strong>示例 1：</strong>

<pre><b>输入：</b>nums1 = [4,1,3], nums2 = [5,7]
<b>输出：</b>15
<b>解释：</b>数字 15 的数位 1 在 nums1 中出现，数位 5 在 nums2 中出现。15 是我们能得到的最小数字。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>nums1 = [3,5,2,6], nums2 = [3,1,7]
<b>输出：</b>3
<b>解释：</b>数字 3 的数位 3 在两个数组中都出现了。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums1.length, nums2.length <= 9</code></li>
	<li><code>1 <= nums1[i], nums2[i] <= 9</code></li>
	<li>每个数组中，元素 <strong>互不相同</strong>。</li>
</ul>

## 2606.找到最大开销的子字符串

[打开力扣](https://leetcode.cn/problems/find-the-substring-with-maximum-cost) [我的代码](2606.find_the_substring_with_maximum_cost.py)

给你一个字符串<code>s</code>，一个字符<strong>互不相同</strong>的字符串<code>chars</code>和一个长度与 <code>chars</code>相同的整数数组<code>vals</code>。

<strong>子字符串的开销</strong>是一个子字符串中所有字符对应价值之和。空字符串的开销是 <code>0</code>。

<strong>字符的价值</strong>定义如下：

<ul>
	<li>如果字符不在字符串<code>chars</code>中，那么它的价值是它在字母表中的位置（下标从 <strong>1</strong>开始）。

	<ul>
		<li>比方说，<code>'a'</code>的价值为<code>1</code>，<code>'b'</code>的价值为<code>2</code>，以此类推，<code>'z'</code>的价值为<code>26</code>。</li>
	</ul>
	</li>
	<li>否则，如果这个字符在 <code>chars</code>中的位置为 <code>i</code>，那么它的价值就是<code>vals[i]</code>。</li>
</ul>

请你返回字符串 <code>s</code>的所有子字符串中的最大开销。



<strong>示例 1：</strong>

<pre><b>输入：</b>s = "adaa", chars = "d", vals = [-1000]
<b>输出：</b>2
<b>解释：</b>字符 "a" 和 "d" 的价值分别为 1 和 -1000 。
最大开销子字符串是 "aa" ，它的开销为 1 + 1 = 2 。
2 是最大开销。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>s = "abc", chars = "abc", vals = [-1,-1,-1]
<b>输出：</b>0
<b>解释：</b>字符 "a" ，"b" 和 "c" 的价值分别为 -1 ，-1 和 -1 。
最大开销子字符串是 "" ，它的开销为 0 。
0 是最大开销。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= s.length <= 10<sup>5</sup></code></li>
	<li><code>s</code>只包含小写英文字母。</li>
	<li><code>1 <= chars.length <= 26</code></li>
	<li><code>chars</code>只包含小写英文字母，且 <strong>互不相同</strong>。</li>
	<li><code>vals.length == chars.length</code></li>
	<li><code>-1000 <= vals[i] <= 1000</code></li>
</ul>

## 2607.使子数组元素和相等

[打开力扣](https://leetcode.cn/problems/make-k-subarray-sums-equal) [我的代码](2607.make_k_subarray_sums_equal.py)

给你一个下标从 <strong>0</strong> 开始的整数数组 <code>arr</code> 和一个整数 <code>k</code> 。数组 <code>arr</code> 是一个循环数组。换句话说，数组中的最后一个元素的下一个元素是数组中的第一个元素，数组中第一个元素的前一个元素是数组中的最后一个元素。

你可以执行下述运算任意次：

<ul>
	<li>选中 <code>arr</code> 中任意一个元素，并使其值加上 <code>1</code> 或减去 <code>1</code> 。</li>
</ul>

执行运算使每个长度为 <code>k</code> 的 <strong>子数组</strong> 的元素总和都相等，返回所需要的最少运算次数。

<strong>子数组</strong> 是数组的一个连续部分。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>arr = [1,4,1,3], k = 2
<strong>输出：</strong>1
<strong>解释：</strong>在下标为 1 的元素那里执行一次运算，使其等于 3 。
执行运算后，数组变为 [1,3,1,3] 。
- 0 处起始的子数组为 [1, 3] ，元素总和为 4 
- 1 处起始的子数组为 [3, 1] ，元素总和为 4 
- 2 处起始的子数组为 [1, 3] ，元素总和为 4 
- 3 处起始的子数组为 [3, 1] ，元素总和为 4 
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>arr = [2,5,5,7], k = 3
<strong>输出：</strong>5
<strong>解释：</strong>在下标为 0 的元素那里执行三次运算，使其等于 5 。在下标为 3 的元素那里执行两次运算，使其等于 5 。
执行运算后，数组变为 [5,5,5,5] 。
- 0 处起始的子数组为 [5, 5, 5] ，元素总和为 15
- 1 处起始的子数组为 [5, 5, 5] ，元素总和为 15
- 2 处起始的子数组为 [5, 5, 5] ，元素总和为 15
- 3 处起始的子数组为 [5, 5, 5] ，元素总和为 15
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= k <= arr.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= arr[i] <= 10<sup>9</sup></code></li>
</ul>

## 2608.图中的最短环

[打开力扣](https://leetcode.cn/problems/shortest-cycle-in-a-graph) [我的代码](2608.shortest_cycle_in_a_graph.py)

现有一个含 <code>n</code> 个顶点的 <strong>双向</strong> 图，每个顶点按从 <code>0</code> 到 <code>n - 1</code> 标记。图中的边由二维整数数组 <code>edges</code> 表示，其中 <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> 表示顶点 <code>u<sub>i</sub></code> 和 <code>v<sub>i</sub></code> 之间存在一条边。每对顶点最多通过一条边连接，并且不存在与自身相连的顶点。

返回图中 <strong>最短</strong> 环的长度。如果不存在环，则返回 <code>-1</code> 。

<strong>环</strong> 是指以同一节点开始和结束，并且路径中的每条边仅使用一次。



<strong>示例 1：</strong>
<img alt="" src="https://assets.leetcode.com/uploads/2023/01/04/cropped.png" style="width: 387px; height: 331px;">
<pre><strong>输入：</strong>n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
<strong>输出：</strong>3
<strong>解释：</strong>长度最小的循环是：0 -> 1 -> 2 -> 0 
</pre>

<strong>示例 2：</strong>
<img alt="" src="https://assets.leetcode.com/uploads/2023/01/04/croppedagin.png" style="width: 307px; height: 307px;">
<pre><strong>输入：</strong>n = 4, edges = [[0,1],[0,2]]
<strong>输出：</strong>-1
<strong>解释：</strong>图中不存在循环
</pre>



<strong>提示：</strong>

<ul>
	<li><code>2 <= n <= 1000</code></li>
	<li><code>1 <= edges.length <= 1000</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 <= u<sub>i</sub>, v<sub>i</sub> < n</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li>不存在重复的边</li>
</ul>
