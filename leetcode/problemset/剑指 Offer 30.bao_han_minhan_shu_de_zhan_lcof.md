# 剑指 Offer 30. 包含min函数的栈

[打开力扣](https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof) [我的代码](剑指 Offer 30.bao_han_minhan_shu_de_zhan_lcof.py)

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。



<strong>示例:</strong>

<pre>MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
</pre>



<strong>提示：</strong>

<ol>
	<li>各函数的调用总次数不超过 20000 次</li>
</ol>



注意：本题与主站 155 题相同：<a href="https://leetcode-cn.com/problems/min-stack/">https://leetcode-cn.com/problems/min-stack/</a>
