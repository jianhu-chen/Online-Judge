# 第 339 场周赛

> 企业: 安贤量化

## 2609.最长平衡子字符串

[打开力扣](https://leetcode.cn/problems/find-the-longest-balanced-substring-of-a-binary-string) [我的代码](2609.find_the_longest_balanced_substring_of_a_binary_string.py)

给你一个仅由 <code>0</code> 和 <code>1</code> 组成的二进制字符串 <code>s</code> 。<span style=""></span><span style=""></span>

如果子字符串中 <strong>所有的<span style=""> </span></strong><code><span style="">0</span></code><strong><span style=""> </span>都在 </strong><code>1</code><strong> 之前</strong> 且其中 <code>0</code> 的数量等于 <code>1</code> 的数量，则认为 <code>s</code> 的这个子字符串是平衡子字符串。请注意，空子字符串也视作平衡子字符串。<span style=""></span>

返回<span style=""> </span><code>s</code> 中最长的平衡子字符串长度。

子字符串是字符串中的一个连续字符序列。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>s = "01000111"
<strong>输出：</strong>6
<strong>解释：</strong>最长的平衡子字符串是 "000111" ，长度为 6 。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>s = "00111"
<strong>输出：</strong>4
<strong>解释：</strong>最长的平衡子字符串是 "0011" ，长度为 <span style=""></span>4 。
</pre>

<strong>示例 3：</strong>

<pre>
<strong>输入：</strong>s = "111"
<strong>输出：</strong>0
<strong>解释：</strong>除了空子字符串之外不存在其他平衡子字符串，所以答案为 0 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= s.length <= 50</code></li>
	<li><code>'0' <= s[i] <= '1'</code></li>
</ul>

## 2610.转换二维数组

[打开力扣](https://leetcode.cn/problems/convert-an-array-into-a-2d-array-with-conditions) [我的代码](2610.convert_an_array_into_a_2d_array_with_conditions.py)

给你一个整数数组 <code>nums</code> 。请你创建一个满足以下条件的二维数组：

<ul>
	<li>二维数组应该 <strong>只</strong> 包含数组 <code>nums</code> 中的元素。</li>
	<li>二维数组中的每一行都包含 <strong>不同</strong> 的整数。</li>
	<li>二维数组的行数应尽可能 <strong>少</strong> 。</li>
</ul>

返回结果数组。如果存在多种答案，则返回其中任何一种。

请注意，二维数组的每一行上可以存在不同数量的元素。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>nums = [1,3,4,1,2,3,1]
<strong>输出：</strong>[[1,3,4,2],[1,3],[1]]
<strong>解释：</strong>根据题目要求可以创建包含以下几行元素的二维数组：
- 1,3,4,2
- 1,3
- 1
nums 中的所有元素都有用到，并且每一行都由不同的整数组成，所以这是一个符合题目要求的答案。
可以证明无法创建少于三行且符合题目要求的二维数组。</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>[[4,3,2,1]]
<strong>解释：</strong>nums 中的所有元素都不同，所以我们可以将其全部保存在二维数组中的第一行。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 200</code></li>
	<li><code>1 <= nums[i] <= nums.length</code></li>
</ul>

## 2611.老鼠和奶酪

[打开力扣](https://leetcode.cn/problems/mice-and-cheese) [我的代码](2611.mice_and_cheese.py)

有两只老鼠和<code>n</code>块不同类型的奶酪，每块奶酪都只能被其中一只老鼠吃掉。

下标为 <code>i</code>处的奶酪被吃掉的得分为：

<ul>
	<li>如果第一只老鼠吃掉，则得分为<code>reward1[i]</code>。</li>
	<li>如果第二只老鼠吃掉，则得分为<code>reward2[i]</code>。</li>
</ul>

给你一个正整数数组<code>reward1</code>，一个正整数数组<code>reward2</code>，和一个非负整数<code>k</code>。

请你返回第一只老鼠恰好吃掉 <code>k</code>块奶酪的情况下，<strong>最大</strong>得分为多少。



<strong>示例 1：</strong>

<pre>
<b>输入：</b>reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2
<b>输出：</b>15
<b>解释：</b>这个例子中，第一只老鼠吃掉第 2和 3 块奶酪（下标从 0 开始），第二只老鼠吃掉第 0 和 1 块奶酪。
总得分为 4 + 4 + 3 + 4 = 15 。
15 是最高得分。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>reward1 = [1,1], reward2 = [1,1], k = 2
<b>输出：</b>2
<b>解释：</b>这个例子中，第一只老鼠吃掉第 0 和 1 块奶酪（下标从 0 开始），第二只老鼠不吃任何奶酪。
总得分为 1 + 1 = 2 。
2 是最高得分。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= n == reward1.length == reward2.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= reward1[i],reward2[i] <= 1000</code></li>
	<li><code>0 <= k <= n</code></li>
</ul>

## 2612.最少翻转操作数

[打开力扣](https://leetcode.cn/problems/minimum-reverse-operations) [我的代码](2612.minimum_reverse_operations.py)

给你一个整数<code>n</code>和一个在范围 <code>[0, n - 1]</code>以内的整数<code>p</code>，它们表示一个长度为 <code>n</code> 且下标从 <strong>0</strong>开始的数组<code>arr</code>，数组中除了下标为<code>p</code>处是 <code>1</code>以外，其他所有数都是 <code>0</code>。

同时给你一个整数数组<code>banned</code>，它包含数组中的一些位置。<code>banned</code>中第<strong>i</strong>个位置表示<code>arr[banned[i]] = 0</code>，题目保证<code>banned[i] != p</code>。

你可以对 <code>arr</code>进行 <strong>若干次</strong>操作。一次操作中，你选择大小为 <code>k</code>的一个 <strong>子数组</strong>，并将它 <b>翻转</b>。在任何一次翻转操作后，你都需要确保 <code>arr</code>中唯一的 <code>1</code>不会到达任何 <code>banned</code>中的位置。换句话说，<code>arr[banned[i]]</code>始终<strong>保持</strong><code>0</code>。

请你返回一个数组<code>ans</code>，对于<em></em><code>[0, n - 1]</code>之间的任意下标<code>i</code>，<code>ans[i]</code>是将<code>1</code>放到位置<code>i</code>处的<strong>最少</strong>翻转操作次数，如果无法放到位置<code>i</code>处，此数为<code>-1</code>。

<ul>
	<li><strong>子数组</strong>指的是一个数组里一段连续 <strong>非空</strong>的元素序列。</li>
	<li>对于所有的 <code>i</code>，<code>ans[i]</code>相互之间独立计算。</li>
	<li>将一个数组中的元素 <strong>翻转</strong> 指的是将数组中的值变成 <strong>相反顺序</strong>。</li>
</ul>



<strong>示例 1：</strong>

<pre>
<b>输入：</b>n = 4, p = 0, banned = [1,2], k = 4
<b>输出：</b>[0,-1,-1,1]
<b>解释：</b><code>k = 4，所以只有一种可行的翻转操作，就是将整个数组翻转。一开始 </code>1<strong> </strong>在位置 0 处，所以将它翻转到位置 0 处需要的操作数为 0 。
我们不能将 1 翻转到 banned 中的位置，所以位置 1 和 2 处的答案都是 -1 。
通过一次翻转操作，可以将 1 放到位置 3 处，所以位置 3 的答案是 1 。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>n = 5, p = 0, banned = [2,4], k = 3
<b>输出：</b>[0,-1,-1,-1,-1]
<b>解释：</b>这个例子中 1 一开始在位置 0 处，所以此下标的答案为 0 。
翻转的子数组长度为 k = 3 ，1 此时在位置 0 处，所以我们可以翻转子数组 [0, 2]，但翻转后的下标 2 在 banned 中，所以不能执行此操作。
由于 1 没法离开位置 0 ，所以其他位置的答案都是 -1 。
</pre>

<strong>示例 3：</strong>

<pre>
<b>输入：</b>n = 4, p = 2, banned = [0,1,3], k = 1
<b>输出：</b>[-1,-1,0,-1]
<b>解释：</b>这个例子中，我们只能对长度为 1 的子数组执行翻转操作，所以 1 无法离开初始位置。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= n <= 10<sup>5</sup></code></li>
	<li><code>0 <= p <= n - 1</code></li>
	<li><code>0 <= banned.length <= n - 1</code></li>
	<li><code>0 <= banned[i] <= n - 1</code></li>
	<li><code>1 <= k <= n</code></li>
	<li><code>banned[i] != p</code></li>
	<li><code>banned</code>中的值 <strong>互不相同</strong>。</li>
</ul>
