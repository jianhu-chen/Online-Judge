# 第 331 场周赛

> 企业: 力扣 LeetCode

## 6348.从数量最多的堆取走礼物

[打开力扣](https://leetcode.cn/problems/take-gifts-from-the-richest-pile) [我的代码](6348.take_gifts_from_the_richest_pile.py)

给你一个整数数组 <code>gifts</code> ，表示各堆礼物的数量。每一秒，你需要执行以下操作：

<ul>
	<li>选择礼物数量最多的那一堆。</li>
	<li>如果不止一堆都符合礼物数量最多，从中选择任一堆即可。</li>
	<li>选中的那一堆留下平方根数量的礼物（向下取整），取走其他的礼物。</li>
</ul>

返回在 <code>k</code> 秒后剩下的礼物数量<em>。</em>



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>gifts = [25,64,9,4,100], k = 4
<strong>输出：</strong>29
<strong>解释：</strong>
按下述方式取走礼物：
- 在第一秒，选中最后一堆，剩下 10 个礼物。
- 接着第二秒选中第二堆礼物，剩下 8 个礼物。
- 然后选中第一堆礼物，剩下 5 个礼物。
- 最后，再次选中最后一堆礼物，剩下 3 个礼物。
最后剩下的礼物数量分别是 [5,8,9,4,3] ，所以，剩下礼物的总数量是 29 。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>gifts = [1,1,1,1], k = 4
<strong>输出：</strong>4
<strong>解释：</strong>
在本例中，不管选中哪一堆礼物，都必须剩下 1 个礼物。
也就是说，你无法获取任一堆中的礼物。
所以，剩下礼物的总数量是 4 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= gifts.length <= 10<sup>3</sup></code></li>
	<li><code>1 <= gifts[i] <= 10<sup>9</sup></code></li>
	<li><code>1 <= k <= 10<sup>3</sup></code></li>
</ul>

## 6347.统计范围内的元音字符串数

[打开力扣](https://leetcode.cn/problems/count-vowel-strings-in-ranges) [我的代码](6347.count_vowel_strings_in_ranges.py)

给你一个下标从 <strong>0</strong> 开始的字符串数组 <code>words</code> 以及一个二维整数数组 <code>queries</code> 。

每个查询 <code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code> 会要求我们统计在 <code>words</code> 中下标在 <code>l<sub>i</sub></code> 到 <code>r<sub>i</sub></code> 范围内（<strong>包含</strong> 这两个值）并且以元音开头和结尾的字符串的数目。

返回一个整数数组，其中数组的第 <code>i</code> 个元素对应第 <code>i</code> 个查询的答案。

<strong>注意：</strong>元音字母是 <code>'a'</code>、<code>'e'</code>、<code>'i'</code>、<code>'o'</code> 和 <code>'u'</code> 。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
<strong>输出：</strong>[2,3,0]
<strong>解释：</strong>以元音开头和结尾的字符串是 "aba"、"ece"、"aa" 和 "e" 。
查询 [0,2] 结果为 2（字符串 "aba" 和 "ece"）。
查询 [1,4] 结果为 3（字符串 "ece"、"aa"、"e"）。
查询 [1,1] 结果为 0 。
返回结果 [2,3,0] 。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
<strong>输出：</strong>[3,2,1]
<strong>解释：</strong>每个字符串都满足这一条件，所以返回 [3,2,1] 。</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= words.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= words[i].length <= 40</code></li>
	<li><code>words[i]</code> 仅由小写英文字母组成</li>
	<li><code>sum(words[i].length) <= 3 * 10<sup>5</sup></code></li>
	<li><code>1 <= queries.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= queries[j][0] <= queries[j][1] <words.length</code></li>
</ul>

## 6346.打家劫舍 IV

[打开力扣](https://leetcode.cn/problems/house-robber-iv) [我的代码](6346.house_robber_iv.py)

沿街有一排连续的房屋。每间房屋内都藏有一定的现金。现在有一位小偷计划从这些房屋中窃取现金。

由于相邻的房屋装有相互连通的防盗系统，所以小偷 <strong>不会窃取相邻的房屋</strong> 。

小偷的 <strong>窃取能力</strong> 定义为他在窃取过程中能从单间房屋中窃取的 <strong>最大金额</strong> 。

给你一个整数数组 <code>nums</code> 表示每间房屋存放的现金金额。形式上，从左起第 <code>i</code> 间房屋中放有 <code>nums[i]</code> 美元。

另给你一个整数数组 <code>k</code> ，表示窃贼将会窃取的 <strong>最少</strong> 房屋数。小偷总能窃取至少 <code>k</code> 间房屋。

返回小偷的 <strong>最小</strong> 窃取能力。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>nums = [2,3,5,9], k = 2
<strong>输出：</strong>5
<strong>解释：</strong>
小偷窃取至少 2 间房屋，共有 3 种方式：
- 窃取下标 0 和 2 处的房屋，窃取能力为 max(nums[0], nums[2]) = 5 。
- 窃取下标 0 和 3 处的房屋，窃取能力为 max(nums[0], nums[3]) = 9 。
- 窃取下标 1 和 3 处的房屋，窃取能力为 max(nums[1], nums[3]) = 9 。
因此，返回 min(5, 9, 9) = 5 。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>nums = [2,7,9,3,1], k = 2
<strong>输出：</strong>2
<strong>解释：</strong>共有 7 种窃取方式。窃取能力最小的情况所对应的方式是窃取下标 0 和 4 处的房屋。返回 max(nums[0], nums[4]) = 2 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i] <= 10<sup>9</sup></code></li>
	<li><code>1 <= k <= (nums.length + 1)/2</code></li>
</ul>

## 6345.重排水果

[打开力扣](https://leetcode.cn/problems/rearranging-fruits) [我的代码](6345.rearranging_fruits.py)

你有两个果篮，每个果篮中有 <code>n</code> 个水果。给你两个下标从 <strong>0</strong> 开始的整数数组 <code>basket1</code> 和 <code>basket2</code> ，用以表示两个果篮中每个水果的成本。

你希望两个果篮相等。为此，可以根据需要多次执行下述操作：

<ul>
	<li>选中两个下标 <code>i</code> 和 <code>j</code> ，并交换 <code>basket1</code> 中的第 <code>i</code> 个水果和 <code>basket2</code> 中的第 <code>j</code> 个水果。</li>
	<li>交换的成本是 <code>min(basket1<sub>i</sub>,basket2<sub>j</sub>)</code> 。</li>
</ul>

根据果篮中水果的成本进行排序，如果排序后结果完全相同，则认为两个果篮相等。

返回使两个果篮相等的最小交换成本，如果无法使两个果篮相等，则返回<em> </em><code>-1</code><em> </em>。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>basket1 = [4,2,2,2], basket2 = [1,4,1,2]
<strong>输出：</strong>1
<strong>解释：</strong>交换 basket1 中下标为 1 的水果和 basket2 中下标为 0 的水果，交换的成本为 1 。此时，basket1 = [4,1,2,2] 且 basket2 = [2,4,1,2] 。重排两个数组，发现二者相等。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>basket1 = [2,3,4,1], basket2 = [3,2,5,1]
<strong>输出：</strong>-1
<strong>解释：</strong>可以证明无法使两个果篮相等。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>basket1.length == bakste2.length</code></li>
	<li><code>1 <= basket1.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= basket1<sub>i</sub>,basket2<sub>i</sub> <= 10<sup>9</sup></code></li>
</ul>
