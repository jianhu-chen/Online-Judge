# 第 335 场周赛

> 企业: 力扣

## 6307.递枕头

[打开力扣](https://leetcode.cn/problems/pass-the-pillow) [我的代码](6307.pass_the_pillow.py)

<code>n</code> 个人站成一排，按从 <code>1</code> 到 <code>n</code> 编号。

最初，排在队首的第一个人拿着一个枕头。每秒钟，拿着枕头的人会将枕头传递给队伍中的下一个人。一旦枕头到达队首或队尾，传递方向就会改变，队伍会继续沿相反方向传递枕头。

<ul>
	<li>例如，当枕头到达第 <code>n</code> 个人时，TA 会将枕头传递给第 <code>n - 1</code> 个人，然后传递给第 <code>n - 2</code> 个人，依此类推。</li>
</ul>

给你两个正整数 <code>n</code> 和 <code>time</code> ，返回 <code>time</code> 秒后拿着枕头的人的编号。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>n = 4, time = 5
<strong>输出：</strong>2
<strong>解释：</strong>队伍中枕头的传递情况为：1 -> 2 -> 3 -> 4 -> 3 -> 2 。
5 秒后，枕头传递到第 2 个人手中。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>n = 3, time = 2
<strong>输出：</strong>3
<strong>解释：</strong>队伍中枕头的传递情况为：1 -> 2 -> 3 。
2 秒后，枕头传递到第 3 个人手中。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>2 <= n <= 1000</code></li>
	<li><code>1 <= time <= 1000</code></li>
</ul>

## 6308.二叉树中的第 K 大层和

[打开力扣](https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree) [我的代码](6308.kth_largest_sum_in_a_binary_tree.py)

给你一棵二叉树的根节点 <code>root</code> 和一个正整数 <code>k</code> 。

树中的 <strong>层和</strong> 是指 <strong>同一层</strong> 上节点值的总和。

返回树中第 <code>k</code> 大的层和（不一定不同）。如果树少于 <code>k</code> 层，则返回 <code>-1</code> 。

<strong>注意</strong>，如果两个节点与根节点的距离相同，则认为它们在同一层。



<strong>示例 1：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/12/14/binaryytreeedrawio-2.png" style="width: 301px; height: 284px;" />

<pre>
<strong>输入：</strong>root = [5,8,9,2,1,3,7,4,6], k = 2
<strong>输出：</strong>13
<strong>解释：</strong>树中每一层的层和分别是：
- Level 1: 5
- Level 2: 8 + 9 = 17
- Level 3: 2 + 1 + 3 + 7 = 13
- Level 4: 4 + 6 = 10
第 2 大的层和等于 13 。
</pre>

<strong>示例 2：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/12/14/treedrawio-3.png" style="width: 181px; height: 181px;" />

<pre>
<strong>输入：</strong>root = [1,2,null,3], k = 1
<strong>输出：</strong>3
<strong>解释：</strong>最大的层和是 3 。
</pre>



<strong>提示：</strong>

<ul>
	<li>树中的节点数为 <code>n</code></li>
	<li><code>2 <= n <= 10<sup>5</sup></code></li>
	<li><code>1 <= Node.val <= 10<sup>6</sup></code></li>
	<li><code>1 <= k <= n</code></li>
</ul>

## 6309.分割数组使乘积互质

[打开力扣](https://leetcode.cn/problems/split-the-array-to-make-coprime-products) [我的代码](6309.split_the_array_to_make_coprime_products.py)

给你一个长度为 <code>n</code> 的整数数组 <code>nums</code> ，下标从 <strong>0</strong> 开始。

如果在下标 <code>i</code> 处 <strong>分割</strong> 数组，其中 <code>0 <= i <= n - 2</code> ，使前 <code>i + 1</code> 个元素的乘积和剩余元素的乘积互质，则认为该分割 <strong>有效</strong> 。

<ul>
	<li>例如，如果 <code>nums = [2, 3, 3]</code> ，那么在下标 <code>i = 0</code> 处的分割有效，因为 <code>2</code> 和 <code>9</code> 互质，而在下标 <code>i = 1</code> 处的分割无效，因为 <code>6</code> 和 <code>3</code> 不互质。在下标 <code>i = 2</code> 处的分割也无效，因为 <code>i == n - 1</code> 。</li>
</ul>

返回可以有效分割数组的最小下标 <code>i</code> ，如果不存在有效分割，则返回 <code>-1</code> 。

当且仅当 <code>gcd(val1, val2) == 1</code> 成立时，<code>val1</code> 和 <code>val2</code> 这两个值才是互质的，其中 <code>gcd(val1, val2)</code> 表示 <code>val1</code> 和 <code>val2</code> 的最大公约数。



<strong>示例 1：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/12/14/second.PNG" style="width: 450px; height: 211px;" />

<pre>
<strong>输入：</strong>nums = [4,7,8,15,3,5]
<strong>输出：</strong>2
<strong>解释：</strong>上表展示了每个下标 i 处的前 i + 1 个元素的乘积、剩余元素的乘积和它们的最大公约数的值。
唯一一个有效分割位于下标 2 。</pre>

<strong>示例 2：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/12/14/capture.PNG" style="width: 450px; height: 215px;" />

<pre>
<strong>输入：</strong>nums = [4,7,15,8,3,5]
<strong>输出：</strong>-1
<strong>解释：</strong>上表展示了每个下标 i 处的前 i + 1 个元素的乘积、剩余元素的乘积和它们的最大公约数的值。
不存在有效分割。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 <= n <= 10<sup>4</sup></code></li>
	<li><code>1 <= nums[i] <= 10<sup>6</sup></code></li>
</ul>

## 6310.获得分数的方法数

[打开力扣](https://leetcode.cn/problems/number-of-ways-to-earn-points) [我的代码](6310.number_of_ways_to_earn_points.py)

考试中有 <code>n</code> 种类型的题目。给你一个整数 <code>target</code> 和一个下标从 <strong>0</strong> 开始的二维整数数组 <code>types</code> ，其中 <code>types[i] = [count<sub>i</sub>, marks<sub>i</sub>] </code>表示第 <code>i</code> 种类型的题目有 <code>count<sub>i</sub></code> 道，每道题目对应 <code>marks<sub>i</sub></code> 分。

返回你在考试中恰好得到 <code>target</code> 分的方法数。由于答案可能很大，结果需要对 <code>10<sup>9</sup> +7</code> 取余。

<strong>注意</strong>，同类型题目无法区分。

<ul>
	<li>比如说，如果有 <code>3</code> 道同类型题目，那么解答第 <code>1</code> 和第 <code>2</code> 道题目与解答第 <code>1</code> 和第 <code>3</code> 道题目或者第 <code>2</code> 和第 <code>3</code> 道题目是相同的。</li>
</ul>



<strong>示例 1：</strong>

<pre><strong>输入：</strong>target = 6, types = [[6,1],[3,2],[2,3]]
<strong>输出：</strong>7
<strong>解释：</strong>要获得 6 分，你可以选择以下七种方法之一：
- 解决 6 道第 0 种类型的题目：1 + 1 + 1 + 1 + 1 + 1 = 6
- 解决 4 道第 0 种类型的题目和 1 道第 1 种类型的题目：1 + 1 + 1 + 1 + 2 = 6
- 解决 2 道第 0 种类型的题目和 2 道第 1 种类型的题目：1 + 1 + 2 + 2 = 6
- 解决 3 道第 0 种类型的题目和 1 道第 2 种类型的题目：1 + 1 + 1 + 3 = 6
- 解决 1 道第 0 种类型的题目、1 道第 1 种类型的题目和 1 道第 2 种类型的题目：1 + 2 + 3 = 6
- 解决 3 道第 1 种类型的题目：2 + 2 + 2 = 6
- 解决 2 道第 2 种类型的题目：3 + 3 = 6
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>target = 5, types = [[50,1],[50,2],[50,5]]
<strong>输出：</strong>4
<strong>解释：</strong>要获得 5 分，你可以选择以下四种方法之一：
- 解决 5 道第 0 种类型的题目：1 + 1 + 1 + 1 + 1 = 5
- 解决 3 道第 0 种类型的题目和 1 道第 1 种类型的题目：1 + 1 + 1 + 2 = 5
- 解决 1 道第 0 种类型的题目和 2 道第 1 种类型的题目：1 + 2 + 2 = 5
- 解决 1 道第 2 种类型的题目：5
</pre>

<strong>示例 3：</strong>

<pre><strong>输入：</strong>target = 18, types = [[6,1],[3,2],[2,3]]
<strong>输出：</strong>1
<strong>解释：</strong>只有回答所有题目才能获得 18 分。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= target <= 1000</code></li>
	<li><code>n == types.length</code></li>
	<li><code>1 <= n <= 50</code></li>
	<li><code>types[i].length == 2</code></li>
	<li><code>1 <= count<sub>i</sub>, marks<sub>i</sub> <= 50</code></li>
</ul>
