# 第 325 场周赛

> 企业: 西门子数字化工业

## 2515.到目标字符串的最短距离

[打开力扣](https://leetcode.cn/problems/shortest-distance-to-target-string-in-a-circular-array) [我的代码](2515.shortest_distance_to_target_string_in_a_circular_array.py)

给你一个下标从 <strong>0</strong> 开始的 <strong>环形</strong> 字符串数组 <code>words</code> 和一个字符串 <code>target</code> 。<strong>环形数组</strong> 意味着数组首尾相连。

<ul>
	<li>形式上， <code>words[i]</code> 的下一个元素是 <code>words[(i + 1) % n]</code> ，而 <code>words[i]</code> 的前一个元素是 <code>words[(i - 1 + n) % n]</code> ，其中 <code>n</code> 是 <code>words</code> 的长度。</li>
</ul>

从 <code>startIndex</code> 开始，你一次可以用 <code>1</code> 步移动到下一个或者前一个单词。

返回到达目标字符串 <code>target</code> 所需的最短距离。如果 <code>words</code> 中不存在字符串 <code>target</code> ，返回 <code>-1</code> 。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
<strong>输出：</strong>1
<strong>解释：</strong>从下标 1 开始，可以经由以下步骤到达 "hello" ：
- 向右移动 3 个单位，到达下标 4 。
- 向左移动 2 个单位，到达下标 4 。
- 向右移动 4 个单位，到达下标 0 。
- 向左移动 1 个单位，到达下标 0 。
到达 "hello" 的最短距离是 1 。
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>words = ["a","b","leetcode"], target = "leetcode", startIndex = 0
<strong>输出：</strong>1
<strong>解释：</strong>从下标 0 开始，可以经由以下步骤到达 "leetcode" ：
- 向右移动 2 个单位，到达下标 3 。
- 向左移动 1 个单位，到达下标 3 。
到达 "leetcode" 的最短距离是 1 。</pre>

<strong>示例 3：</strong>

<pre><strong>输入：</strong>words = ["i","eat","leetcode"], target = "ate", startIndex = 0
<strong>输出：</strong>-1
<strong>解释：</strong>因为 words 中不存在字符串 "ate" ，所以返回 -1 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= words.length <= 100</code></li>
	<li><code>1 <= words[i].length <= 100</code></li>
	<li><code>words[i]</code> 和 <code>target</code> 仅由小写英文字母组成</li>
	<li><code>0 <= startIndex < words.length</code></li>
</ul>

## 2516.每种字符至少取 K 个

[打开力扣](https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right) [我的代码](2516.take_k_of_each_character_from_left_and_right.py)

给你一个由字符 <code>'a'</code>、<code>'b'</code>、<code>'c'</code> 组成的字符串 <code>s</code> 和一个非负整数 <code>k</code> 。每分钟，你可以选择取走 <code>s</code> <strong>最左侧</strong> 还是 <strong>最右侧</strong> 的那个字符。

你必须取走每种字符 <strong>至少</strong> <code>k</code> 个，返回需要的 <strong>最少</strong> 分钟数；如果无法取到，则返回<em> </em><code>-1</code> 。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>s = "aabaaaacaabc", k = 2
<strong>输出：</strong>8
<strong>解释：</strong>
从 s 的左侧取三个字符，现在共取到两个字符 'a' 、一个字符 'b' 。
从 s 的右侧取五个字符，现在共取到四个字符 'a' 、两个字符 'b' 和两个字符 'c' 。
共需要 3 + 5 = 8 分钟。
可以证明需要的最少分钟数是 8 。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>s = "a", k = 1
<strong>输出：</strong>-1
<strong>解释：</strong>无法取到一个字符 'b' 或者 'c'，所以返回 -1 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= s.length <= 10<sup>5</sup></code></li>
	<li><code>s</code> 仅由字母 <code>'a'</code>、<code>'b'</code>、<code>'c'</code> 组成</li>
	<li><code>0 <= k <= s.length</code></li>
</ul>

## 2517.礼盒的最大甜蜜度

[打开力扣](https://leetcode.cn/problems/maximum-tastiness-of-candy-basket) [我的代码](2517.maximum_tastiness_of_candy_basket.py)

给你一个正整数数组 <code>price</code> ，其中 <code>price[i]</code> 表示第 <code>i</code> 类糖果的价格，另给你一个正整数 <code>k</code> 。

商店组合 <code>k</code> 类 <strong>不同</strong> 糖果打包成礼盒出售。礼盒的 <strong>甜蜜度</strong> 是礼盒中任意两种糖果 <strong>价格</strong> 绝对差的最小值。

返回礼盒的 <strong>最大 </strong>甜蜜度<em>。</em>



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>price = [13,5,1,8,21,2], k = 3
<strong>输出：</strong>8
<strong>解释：</strong>选出价格分别为 [13,5,21] 的三类糖果。
礼盒的甜蜜度为 min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8 。
可以证明能够取得的最大甜蜜度就是 8 。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>price = [1,3,1], k = 2
<strong>输出：</strong>2
<strong>解释：</strong>选出价格分别为 [1,3] 的两类糖果。
礼盒的甜蜜度为 min(|1 - 3|) = min(2) = 2 。
可以证明能够取得的最大甜蜜度就是 2 。
</pre>

<strong>示例 3：</strong>

<pre>
<strong>输入：</strong>price = [7,7,7,7], k = 2
<strong>输出：</strong>0
<strong>解释：</strong>从现有的糖果中任选两类糖果，甜蜜度都会是 0 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= price.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= price[i] <= 10<sup>9</sup></code></li>
	<li><code>2 <= k <= price.length</code></li>
</ul>

## 2518.好分区的数目

[打开力扣](https://leetcode.cn/problems/number-of-great-partitions) [我的代码](2518.number_of_great_partitions.py)

给你一个正整数数组 <code>nums</code> 和一个整数 <code>k</code> 。

<strong>分区</strong> 的定义是：将数组划分成两个有序的 <strong>组</strong> ，并满足每个元素 <strong>恰好</strong> 存在于 <strong>某一个</strong> 组中。如果分区中每个组的元素和都大于等于 <code>k</code> ，则认为分区是一个好分区。

返回 <strong>不同</strong> 的好分区的数目。由于答案可能很大，请返回对 <code>10<sup>9</sup> + 7</code> <strong>取余</strong> 后的结果。

如果在两个分区中，存在某个元素 <code>nums[i]</code> 被分在不同的组中，则认为这两个分区不同。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>nums = [1,2,3,4], k = 4
<strong>输出：</strong>6
<strong>解释：</strong>好分区的情况是 ([1,2,3], [4]), ([1,3], [2,4]), ([1,4], [2,3]), ([2,3], [1,4]), ([2,4], [1,3]) 和 ([4], [1,2,3]) 。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>nums = [3,3,3], k = 4
<strong>输出：</strong>0
<strong>解释：</strong>数组中不存在好分区。
</pre>

<strong class="example">示例 3：</strong>

<pre>
<strong>输入：</strong>nums = [6,6], k = 2
<strong>输出：</strong>2
<strong>解释：</strong>可以将 nums[0] 放入第一个分区或第二个分区中。
好分区的情况是 ([6], [6]) 和 ([6], [6]) 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length, k <= 1000</code></li>
	<li><code>1 <= nums[i] <= 10<sup>9</sup></code></li>
</ul>
