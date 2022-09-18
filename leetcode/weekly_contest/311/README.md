# 第 311 场周赛

> 企业: 安贤量化

## 6180.最小偶倍数

[打开力扣](https://leetcode.cn/problems/smallest-even-multiple) [我的代码](6180.smallest_even_multiple.py)

给你一个正整数 <code>n</code> ，返回 <code>2</code><em> </em>和<em> </em><code>n</code> 的最小公倍数（正整数）。


<strong>示例 1：</strong>

<pre><strong>输入：</strong>n = 5
<strong>输出：</strong>10
<strong>解释：</strong>5 和 2 的最小公倍数是 10 。
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>n = 6
<strong>输出：</strong>6
<strong>解释：</strong>6 和 2 的最小公倍数是 6 。注意数字会是它自身的倍数。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= n <= 150</code></li>
</ul>

## 6181.最长的字母序连续子字符串的长度

[打开力扣](https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring) [我的代码](6181.length_of_the_longest_alphabetical_continuous_substring.py)

<strong>字母序连续字符串</strong> 是由字母表中连续字母组成的字符串。换句话说，字符串 <code>"abcdefghijklmnopqrstuvwxyz"</code> 的任意子字符串都是 <strong>字母序连续字符串</strong> 。

<ul>
	<li>例如，<code>"abc"</code> 是一个字母序连续字符串，而 <code>"acb"</code> 和 <code>"za"</code> 不是。</li>
</ul>

给你一个仅由小写英文字母组成的字符串 <code>s</code> ，返回其 <strong>最长</strong> 的 字母序连续子字符串 的长度。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>s = "abacaba"
<strong>输出：</strong>2
<strong>解释：</strong>共有 4 个不同的字母序连续子字符串 "a"、"b"、"c" 和 "ab" 。
"ab" 是最长的字母序连续子字符串。
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>s = "abcde"
<strong>输出：</strong>5
<strong>解释：</strong>"abcde" 是最长的字母序连续子字符串。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= s.length <= 10<sup>5</sup></code></li>
	<li><code>s</code> 由小写英文字母组成</li>
</ul>

## 6182.反转二叉树的奇数层

[打开力扣](https://leetcode.cn/problems/reverse-odd-levels-of-binary-tree) [我的代码](6182.reverse_odd_levels_of_binary_tree.py)

给你一棵 <strong>完美</strong> 二叉树的根节点 <code>root</code> ，请你反转这棵树中每个 <strong>奇数</strong> 层的节点值。

<ul>
	<li>例如，假设第 3 层的节点值是 <code>[2,1,3,4,7,11,29,18]</code> ，那么反转后它应该变成 <code>[18,29,11,7,4,3,1,2]</code> 。</li>
</ul>

反转后，返回树的根节点。

<strong>完美</strong> 二叉树需满足：二叉树的所有父节点都有两个子节点，且所有叶子节点都在同一层。

节点的 <strong>层数</strong> 等于该节点到根节点之间的边数。



<strong>示例 1：</strong>
<img alt="" src="https://assets.leetcode.com/uploads/2022/07/28/first_case1.png" style="width: 626px; height: 191px;" />
<pre>
<strong>输入：</strong>root = [2,3,5,8,13,21,34]
<strong>输出：</strong>[2,5,3,8,13,21,34]
<strong>解释：</strong>
这棵树只有一个奇数层。
在第 1 层的节点分别是 3、5 ，反转后为 5、3 。
</pre>

<strong>示例 2：</strong>
<img alt="" src="https://assets.leetcode.com/uploads/2022/07/28/second_case3.png" style="width: 591px; height: 111px;" />
<pre>
<strong>输入：</strong>root = [7,13,11]
<strong>输出：</strong>[7,11,13]
<strong>解释：</strong> 
在第 1 层的节点分别是 13、11 ，反转后为 11、13 。 
</pre>

<strong>示例 3：</strong>

<pre>
<strong>输入：</strong>root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
<strong>输出：</strong>[0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
<strong>解释：</strong>奇数层由非零值组成。
在第 1 层的节点分别是 1、2 ，反转后为 2、1 。
在第 3 层的节点分别是 1、1、1、1、2、2、2、2 ，反转后为 2、2、2、2、1、1、1、1 。
</pre>



<strong>提示：</strong>

<ul>
	<li>树中的节点数目在范围 <code>[1, 2<sup>14</sup>]</code> 内</li>
	<li><code>0 <= Node.val <= 10<sup>5</sup></code></li>
	<li><code>root</code> 是一棵 <strong>完美</strong> 二叉树</li>
</ul>

## 6183.字符串的前缀分数和

[打开力扣](https://leetcode.cn/problems/sum-of-prefix-scores-of-strings) [我的代码](6183.sum_of_prefix_scores_of_strings.py)

给你一个长度为 <code>n</code> 的数组 <code>words</code> ，该数组由 <strong>非空</strong> 字符串组成。

定义字符串 <code>word</code> 的 <strong>分数</strong> 等于以 <code>word</code> 作为 <strong>前缀</strong> 的 <code>words[i]</code> 的数目。

<ul>
	<li>例如，如果 <code>words = ["a", "ab", "abc", "cab"]</code> ，那么 <code>"ab"</code> 的分数是 <code>2</code> ，因为 <code>"ab"</code> 是 <code>"ab"</code> 和 <code>"abc"</code> 的一个前缀。</li>
</ul>

返回一个长度为<em> </em><code>n</code> 的数组<em> </em><code>answer</code><em> </em>，其中<em> </em><code>answer[i]</code><em> </em>是<em></em><code>words[i]</code> 的每个非空前缀的分数 <strong>总和</strong> <em>。</em>

<strong>注意：</strong>字符串视作它自身的一个前缀。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>words = ["abc","ab","bc","b"]
<strong>输出：</strong>[5,4,3,2]
<strong>解释：</strong>对应每个字符串的答案如下：
- "abc" 有 3 个前缀："a"、"ab" 和 "abc" 。
- 2 个字符串的前缀为 "a" ，2 个字符串的前缀为 "ab" ，1 个字符串的前缀为 "abc" 。
总计 answer[0] = 2 + 2 + 1 = 5 。
- "ab" 有 2 个前缀："a" 和 "ab" 。
- 2 个字符串的前缀为 "a" ，2 个字符串的前缀为 "ab" 。
总计 answer[1] = 2 + 2 = 4 。
- "bc" 有 2 个前缀："b" 和 "bc" 。
- 2 个字符串的前缀为 "b" ，1 个字符串的前缀为 "bc" 。 
总计 answer[2] = 2 + 1 = 3 。
- "b" 有 1 个前缀："b"。
- 2 个字符串的前缀为 "b" 。
总计 answer[3] = 2 。
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>words = ["abcd"]
<strong>输出：</strong>[4]
<strong>解释：</strong>
"abcd" 有 4 个前缀 "a"、"ab"、"abc" 和 "abcd"。
每个前缀的分数都是 1 ，总计 answer[0] = 1 + 1 + 1 + 1 = 4 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= words.length <= 1000</code></li>
	<li><code>1 <= words[i].length <= 1000</code></li>
	<li><code>words[i]</code> 由小写英文字母组成</li>
</ul>
