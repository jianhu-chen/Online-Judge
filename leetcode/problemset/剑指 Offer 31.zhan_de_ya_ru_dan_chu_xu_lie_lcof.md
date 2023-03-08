# 剑指 Offer 31. 栈的压入、弹出序列

[打开力扣](https://leetcode.cn/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof) [我的代码](剑指 Offer 31.zhan_de_ya_ru_dan_chu_xu_lie_lcof.py)

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
<strong>输出：</strong>true
<strong>解释：</strong>我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
<strong>输出：</strong>false
<strong>解释：</strong>1 不能在 2 之前弹出。
</pre>



<strong>提示：</strong>

<ol>
	<li><code>0 <= pushed.length == popped.length <= 1000</code></li>
	<li><code>0 <= pushed[i], popped[i] < 1000</code></li>
	<li><code>pushed</code>是<code>popped</code>的排列。</li>
</ol>

注意：本题与主站 946 题相同：<a href="https://leetcode-cn.com/problems/validate-stack-sequences/">https://leetcode-cn.com/problems/validate-stack-sequences/</a>
