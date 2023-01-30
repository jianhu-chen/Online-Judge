# 第 96 场双周赛

> 企业: 力扣

## 2540.最小公共值

[打开力扣](https://leetcode.cn/problems/minimum-common-value) [我的代码](2540.minimum_common_value.py)

给你两个整数数组<code>nums1</code> 和<code>nums2</code>，它们已经按非降序排序，请你返回两个数组的 <strong>最小公共整数</strong>。如果两个数组<code>nums1</code> 和<code>nums2</code>没有公共整数，请你返回<code>-1</code>。

如果一个整数在两个数组中都 <strong>至少出现一次</strong>，那么这个整数是数组<code>nums1</code> 和<code>nums2</code><strong>公共</strong>的。



<strong>示例 1：</strong>

<pre><b>输入：</b>nums1 = [1,2,3], nums2 = [2,4]
<b>输出：</b>2
<b>解释：</b>两个数组的最小公共元素是 2 ，所以我们返回 2 。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>nums1 = [1,2,3,6], nums2 = [2,3,4,5]
<b>输出：</b>2
<b>解释：</b>两个数组中的公共元素是 2 和 3 ，2 是较小值，所以返回 2 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums1.length, nums2.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums1[i], nums2[j] <= 10<sup>9</sup></code></li>
	<li><code>nums1</code> 和<code>nums2</code>都是 <strong>非降序</strong>的。</li>
</ul>

## 2541.使数组中所有元素相等的最小操作数 II

[打开力扣](https://leetcode.cn/problems/minimum-operations-to-make-array-equal-ii) [我的代码](2541.minimum_operations_to_make_array_equal_ii.py)

给你两个整数数组<code>nums1</code> 和<code>nums2</code>，两个数组长度都是<code>n</code>，再给你一个整数<code>k</code>。你可以对数组<code>nums1</code>进行以下操作：

<ul>
	<li>选择两个下标<code>i</code> 和<code>j</code>，将<code>nums1[i]</code>增加<code>k</code>，将<code>nums1[j]</code>减少<code>k</code>。换言之，<code>nums1[i] = nums1[i] + k</code> 且<code>nums1[j] = nums1[j] - k</code>。</li>
</ul>

如果对于所有满足<code>0 <= i < n</code>都有<code>num1[i] == nums2[i]</code>，那么我们称<code>nums1</code> <strong>等于</strong><code>nums2</code>。

请你返回使<em></em><code>nums1</code><em> </em>等于<em></em><code>nums2</code>的<strong>最少</strong>操作数。如果没办法让它们相等，请你返回<code>-1</code>。



<strong>示例 1：</strong>

<pre><b>输入：</b>nums1 = [4,3,1,4], nums2 = [1,3,7,1], k = 3
<b>输出：</b>2
<b>解释：</b>我们可以通过 2 个操作将 nums1 变成 nums2 。
第 1 个操作：i = 2 ，j = 0 。操作后得到 nums1 = [1,3,4,4] 。
第 2 个操作：i = 2 ，j = 3 。操作后得到 nums1 = [1,3,7,1] 。
无法用更少操作使两个数组相等。</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>nums1 = [3,8,5,2], nums2 = [2,4,1,6], k = 1
<b>输出：</b>-1
<b>解释：</b>无法使两个数组相等。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>n == nums1.length == nums2.length</code></li>
	<li><code>2 <= n <= 10<sup>5</sup></code></li>
	<li><code>0 <= nums1[i], nums2[j] <= 10<sup>9</sup></code></li>
	<li><code>0 <= k <= 10<sup>5</sup></code></li>
</ul>

## 2542.最大子序列的分数

[打开力扣](https://leetcode.cn/problems/maximum-subsequence-score) [我的代码](2542.maximum_subsequence_score.py)

给你两个下标从 <strong>0</strong>开始的整数数组<code>nums1</code>和<code>nums2</code>，两者长度都是<code>n</code>，再给你一个正整数<code>k</code>。你必须从<code>nums1</code>中选一个长度为 <code>k</code>的 <strong>子序列</strong>对应的下标。

对于选择的下标<code>i<sub>0</sub></code>，<code>i<sub>1</sub></code>，...，<code>i<sub>k - 1</sub></code>，你的<strong>分数</strong>定义如下：

<ul>
	<li><code>nums1</code>中下标对应元素求和，乘以<code>nums2</code>中下标对应元素的<strong>最小值</strong>。</li>
	<li>用公示表示：<code>(nums1[i<sub>0</sub>] + nums1[i<sub>1</sub>] +...+ nums1[i<sub>k - 1</sub>]) * min(nums2[i<sub>0</sub>] , nums2[i<sub>1</sub>], ... ,nums2[i<sub>k - 1</sub>])</code>。</li>
</ul>

请你返回 <strong>最大</strong>可能的分数。

一个数组的 <strong>子序列</strong>下标是集合<code>{0, 1, ..., n-1}</code>中删除若干元素得到的剩余集合，也可以不删除任何元素。



<strong>示例 1：</strong>

<pre><b>输入：</b>nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
<b>输出：</b>12
<b>解释：</b>
四个可能的子序列分数为：
- 选择下标 0 ，1 和 2 ，得到分数 (1+3+3) * min(2,1,3) = 7 。
- 选择下标 0 ，1 和 3 ，得到分数 (1+3+2) * min(2,1,4) = 6 。
- 选择下标 0 ，2 和 3 ，得到分数 (1+3+2) * min(2,3,4) = 12 。
- 选择下标 1 ，2 和 3 ，得到分数 (3+3+2) * min(1,3,4) = 8 。
所以最大分数为 12 。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
<b>输出：</b>30
<b>解释：</b>
选择下标 2 最优：nums1[2] * nums2[2] = 3 * 10 = 30 是最大可能分数。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>n == nums1.length == nums2.length</code></li>
	<li><code>1 <= n <= 10<sup>5</sup></code></li>
	<li><code>0 <= nums1[i], nums2[j] <= 10<sup>5</sup></code></li>
	<li><code>1 <= k <= n</code></li>
</ul>

## 2543.判断一个点是否可以到达

[打开力扣](https://leetcode.cn/problems/check-if-point-is-reachable) [我的代码](2543.check_if_point_is_reachable.py)

给你一个无穷大的网格图。一开始你在<code>(1, 1)</code>，你需要通过有限步移动到达点<code>(targetX, targetY)</code>。

<b>每一步</b>，你可以从点<code>(x, y)</code>移动到以下点之一：

<ul>
	<li><code>(x, y - x)</code></li>
	<li><code>(x - y, y)</code></li>
	<li><code>(2 * x, y)</code></li>
	<li><code>(x, 2 * y)</code></li>
</ul>

给你两个整数<code>targetX</code> 和<code>targetY</code>，分别表示你最后需要到达点的 X 和 Y 坐标。如果你可以从<code>(1, 1)</code>出发到达这个点，请你返回<code>true</code> ，否则返回<em></em><code>false</code><em></em>。



<strong>示例 1：</strong>

<pre><b>输入：</b>targetX = 6, targetY = 9
<b>输出：</b>false
<b>解释：</b>没法从 (1,1) 出发到达 (6,9) ，所以返回 false 。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>targetX = 4, targetY = 7
<b>输出：</b>true
<b>解释：</b>你可以按照以下路径到达：(1,1) -> (1,2) -> (1,4) -> (1,8) -> (1,7) -> (2,7) -> (4,7) 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= targetX, targetY<= 10<sup>9</sup></code></li>
</ul>
