# 剑指 Offer 20. 表示数值的字符串

[打开力扣](https://leetcode.cn/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof) [我的代码](剑指 Offer 20.biao_shi_shu_zhi_de_zi_fu_chuan_lcof.py)

请实现一个函数用来判断字符串是否表示<strong>数值</strong>（包括整数和小数）。

<strong>数值</strong>（按顺序）可以分成以下几个部分：

<ol>
	<li>若干空格</li>
	<li>一个 <strong>小数</strong> 或者 <strong>整数</strong></li>
	<li>（可选）一个 <code>'e'</code> 或 <code>'E'</code> ，后面跟着一个 <strong>整数</strong></li>
	<li>若干空格</li>
</ol>

<strong>小数</strong>（按顺序）可以分成以下几个部分：

<ol>
	<li>（可选）一个符号字符（<code>'+'</code> 或 <code>'-'</code>）</li>
	<li>下述格式之一：
	<ol>
		<li>至少一位数字，后面跟着一个点 <code>'.'</code></li>
		<li>至少一位数字，后面跟着一个点 <code>'.'</code> ，后面再跟着至少一位数字</li>
		<li>一个点 <code>'.'</code> ，后面跟着至少一位数字</li>
	</ol>
	</li>
</ol>

<strong>整数</strong>（按顺序）可以分成以下几个部分：

<ol>
	<li>（可选）一个符号字符（<code>'+'</code> 或 <code>'-'</code>）</li>
	<li>至少一位数字</li>
</ol>

部分<strong>数值</strong>列举如下：

<ul>
	<li><code>["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]</code></li>
</ul>

部分<strong>非数值</strong>列举如下：

<ul>
	<li><code>["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]</code></li>
</ul>

 

<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>s = "0"
<strong>输出：</strong>true
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>s = "e"
<strong>输出：</strong>false
</pre>

<strong>示例 3：</strong>

<pre>
<strong>输入：</strong>s = "."
<strong>输出：</strong>false</pre>

<strong>示例 4：</strong>

<pre>
<strong>输入：</strong>s = "    .1  "
<strong>输出：</strong>true
</pre>

 

<strong>提示：</strong>

<ul>
	<li><code>1 <= s.length <= 20</code></li>
	<li><code>s</code> 仅含英文字母（大写和小写），数字（<code>0-9</code>），加号 <code>'+'</code> ，减号 <code>'-'</code> ，空格 <code>' '</code> 或者点 <code>'.'</code> 。</li>
</ul>
