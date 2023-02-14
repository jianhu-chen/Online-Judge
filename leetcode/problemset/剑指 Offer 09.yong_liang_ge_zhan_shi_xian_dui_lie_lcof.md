# 剑指 Offer 09. 用两个栈实现队列

[打开力扣](https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof) [我的代码](剑指 Offer 09.yong_liang_ge_zhan_shi_xian_dui_lie_lcof.py)

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 <code>appendTail</code> 和 <code>deleteHead</code> ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，<code>deleteHead</code>操作返回 -1 )



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>
["CQueue","appendTail","deleteHead","deleteHead","deleteHead"]
[[],[3],[],[],[]]
<strong>输出：</strong>[null,null,3,-1,-1]
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
<strong>输出：</strong>[null,-1,null,null,5,2]
</pre>

<strong>提示：</strong>

<ul>
	<li><code>1 <= values <= 10000</code></li>
	<li>最多会对<code>appendTail、deleteHead </code>进行<code>10000</code>次调用</li>
</ul>
