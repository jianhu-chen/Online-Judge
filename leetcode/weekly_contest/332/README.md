# 第 332 场周赛

> 企业: 浩鲸科技

## 6354.找出数组的串联值

[打开力扣](https://leetcode.cn/problems/find-the-array-concatenation-value) [我的代码](6354.find_the_array_concatenation_value.py)

给你一个下标从 <strong>0</strong> 开始的整数数组<code>nums</code> 。

现定义两个数字的 <strong>串联</strong>是由这两个数值串联起来形成的新数字。

<ul>
	<li>例如，<code>15</code><span style="">和</span><code>49</code>的串联是<code>1549</code> 。</li>
</ul>

<code>nums</code>的 <strong>串联值</strong>最初等于 <code>0</code> 。执行下述操作直到<code>nums</code>变为空：

<ul>
	<li>如果<code>nums</code>中存在不止一个数字，分别选中 <code>nums</code> 中的第一个元素和最后一个元素，将二者串联得到的值加到<code>nums</code>的 <strong>串联值</strong> 上，然后从<code>nums</code>中删除第一个和最后一个元素。</li>
	<li>如果仅存在一个元素，则将该元素的值加到<code>nums</code> 的串联值上，然后删除这个元素。</li>
</ul>

返回执行完所有操作后<em></em><code>nums</code> 的串联值。



<strong>示例 1：</strong>

<pre>
<b>输入：</b>nums = [7,52,2,4]
<b>输出：</b>596
<b>解释：</b>在执行任一步操作前，nums 为 [7,52,2,4] ，串联值为 0 。
 - 在第一步操作中：
我们选中第一个元素 7 和最后一个元素 4 。
二者的串联是 74 ，将其加到串联值上，所以串联值等于 74 。
接着我们从 nums 中移除这两个元素，所以 nums 变为 [52,2] 。
 - 在第二步操作中：
我们选中第一个元素 52 和最后一个元素 2 。
二者的串联是 522 ，将其加到串联值上，所以串联值等于 596 。
接着我们从 nums 中移除这两个元素，所以 nums 变为空。
由于串联值等于 596 ，所以答案就是 596 。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>nums = [5,14,13,8,12]
<b>输出：</b>673
<b>解释：</b>在执行任一步操作前，nums 为 [5,14,13,8,12] ，串联值为 0 。
- 在第一步操作中：
我们选中第一个元素 5 和最后一个元素 12 。
二者的串联是 512 ，将其加到串联值上，所以串联值等于 512 。
接着我们从 nums 中移除这两个元素，所以 nums 变为 [14,13,8] 。
- 在第二步操作中：
我们选中第一个元素 14 和最后一个元素 8 。
二者的串联是 148 ，将其加到串联值上，所以串联值等于 660 。
接着我们从 nums 中移除这两个元素，所以 nums 变为 [13] 。
- 在第三步操作中：
nums 只有一个元素，所以我们选中 13 并将其加到串联值上，所以串联值等于 673 。
接着我们从 nums 中移除这个元素，所以 nums 变为空。
由于串联值等于 673 ，所以答案就是 673 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 1000</code></li>
	<li><code>1 <= nums[i] <= 10<sup>4</sup></code></li>
</ul>

## 6355.统计公平数对的数目

[打开力扣](https://leetcode.cn/problems/count-the-number-of-fair-pairs) [我的代码](6355.count_the_number_of_fair_pairs.py)

给你一个下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的整数数组<code>nums</code>，和两个整数<code>lower</code> 和<code>upper</code> ，返回 <strong>公平数对的数目</strong> 。

如果<code>(i, j)</code>数对满足以下情况，则认为它是一个 <strong>公平数对</strong>：

<ul>
	<li><code>0 <= i < j < n</code>，且</li>
	<li><code>lower <= nums[i] + nums[j] <= upper</code></li>
</ul>



<b>示例 1：</b>

<pre>
<b>输入：</b>nums = [0,1,7,4,4,5], lower = 3, upper = 6
<b>输出：</b>6
<b>解释：</b>共计 6 个公平数对：(0,3)、(0,4)、(0,5)、(1,3)、(1,4) 和 (1,5) 。
</pre>

<b>示例 2：</b>

<pre>
<b>输入：</b>nums = [1,7,9,2,5], lower = 11, upper = 11
<b>输出：</b>1
<b>解释：</b>只有单个公平数对：(2,3) 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>nums.length == n</code></li>
	<li><code>-10<sup>9</sup><= nums[i] <= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup><= lower <= upper <= 10<sup>9</sup></code></li>
</ul>

## 6356.子字符串异或查询

[打开力扣](https://leetcode.cn/problems/substring-xor-queries) [我的代码](6356.substring_xor_queries.py)

给你一个 <strong>二进制字符串</strong><code>s</code>和一个整数数组<code>queries</code>，其中<code>queries[i] = [first<sub>i</sub>, second<sub>i</sub>]</code>。

对于第<code>i</code>个查询，找到 <code>s</code>的 <strong>最短子字符串</strong>，它对应的 <strong>十进制</strong>值<code>val</code>与<code>first<sub>i</sub></code><b>按位异或</b>得到<code>second<sub>i</sub></code>，换言之，<code>val ^ first<sub>i</sub> == second<sub>i</sub></code>。

第<code>i</code>个查询的答案是子字符串<code>[left<sub>i</sub>, right<sub>i</sub>]</code> 的两个端点（下标从<strong>0</strong>开始），如果不存在这样的子字符串，则答案为<code>[-1, -1]</code>。如果有多个答案，请你选择<code>left<sub>i</sub></code>最小的一个。

请你返回一个数组<code>ans</code>，其中<code>ans[i] = [left<sub>i</sub>, right<sub>i</sub>]</code>是第<code>i</code>个查询的答案。

<strong>子字符串</strong>是一个字符串中一段连续非空的字符序列。



<strong>示例 1：</strong>

<pre>
<b>输入：</b>s = "101101", queries = [[0,5],[1,2]]
<b>输出：</b>[[0,2],[2,3]]
<b>解释：</b>第一个查询，端点为 <code>[0,2]</code> 的子字符串为 <strong>"101"</strong> ，对应十进制数字 <strong><code>5 ，且</code></strong> <strong><code>5 ^ 0 = 5</code></strong>，所以第一个查询的答案为 <code>[0,2]。第二个查询中，</code>端点为 <code>[2,3] 的子字符串为 </code><strong>"11" ，对应十进制数字</strong> <strong>3</strong>，且 <strong>3<code> ^ 1 = 2</code></strong><code>。所以第二个查询的答案为</code> <code>[2,3]</code> 。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>s = "0101", queries = [[12,8]]
<b>输出：</b>[[-1,-1]]
<b>解释：</b>这个例子中，没有符合查询的答案，所以返回 <code>[-1,-1] 。</code>
</pre>

<strong>示例 3：</strong>

<pre>
<b>输入：</b>s = "1", queries = [[4,5]]
<b>输出：</b>[[0,0]]
<b>解释：</b>这个例子中，端点为 <code>[0,0]</code> 的子字符串对应的十进制值为 <strong><code>1</code></strong><code>，且</code> <strong><code>1 ^ 4 = 5</code></strong><code>。所以答案为</code> <code>[0,0] 。</code>
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= s.length <= 10<sup>4</sup></code></li>
	<li><code>s[i]</code>要么是<code>'0'</code>，要么是<code>'1'</code>。</li>
	<li><code>1 <= queries.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= first<sub>i</sub>, second<sub>i</sub> <= 10<sup>9</sup></code></li>
</ul>

## 6357.最少得分子序列

[打开力扣](https://leetcode.cn/problems/subsequence-with-the-minimum-score) [我的代码](6357.subsequence_with_the_minimum_score.py)

给你两个字符串<code>s</code> 和<code>t</code>。

你可以从字符串 <code>t</code>中删除任意数目的字符。

如果没有从字符串<code>t</code>中删除字符，那么得分为<code>0</code>，否则：

<ul>
	<li>令<code>left</code>为删除字符中的最小下标。</li>
	<li>令<code>right</code>为删除字符中的最大下标。</li>
</ul>

字符串的得分为<code>right - left + 1</code>。

请你返回使<em></em><code>t</code><em> </em>成为<em></em><code>s</code>子序列的最小得分。

一个字符串的 <strong>子序列</strong>是从原字符串中删除一些字符后（也可以一个也不删除），剩余字符不改变顺序得到的字符串。（比方说<code>"ace"</code> 是<code>"<strong><em>a</em></strong>b<strong><em>c</em></strong>d<strong><em>e</em></strong>"</code>的子序列，但是<code>"aec"</code>不是）。



<strong>示例 1：</strong>

<pre>
<b>输入：</b>s = "abacaba", t = "bzaa"
<b>输出：</b>1
<b>解释：</b>这个例子中，我们删除下标 1 处的字符 "z" （下标从 0 开始）。
字符串 t 变为 "baa" ，它是字符串 "abacaba" 的子序列，得分为 1 - 1 + 1 = 1 。
1 是能得到的最小得分。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>s = "cde", t = "xyz"
<b>输出：</b>3
<b>解释：</b>这个例子中，我们将下标为 0， 1 和 2 处的字符 "x" ，"y" 和 "z" 删除（下标从 0 开始）。
字符串变成 "" ，它是字符串 "cde" 的子序列，得分为 2 - 0 + 1 = 3 。
3 是能得到的最小得分。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= s.length, t.length <= 10<sup>5</sup></code></li>
	<li><code>s</code> 和<code>t</code>都只包含小写英文字母。</li>
</ul>
