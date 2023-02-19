# 剑指 Offer 18. 删除链表的节点

[打开力扣](https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof) [我的代码](剑指 Offer 18.shan_chu_lian_biao_de_jie_dian_lcof.py)

给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

<strong>注意：</strong>此题对比原题有改动

<strong>示例 1:</strong>

<pre><strong>输入:</strong> head = [4,5,1,9], val = 5
<strong>输出:</strong> [4,1,9]
<strong>解释: </strong>给定你链表中值为5的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
</pre>

<strong>示例 2:</strong>

<pre><strong>输入:</strong> head = [4,5,1,9], val = 1
<strong>输出:</strong> [4,5,9]
<strong>解释: </strong>给定你链表中值为1的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
</pre>



<strong>说明：</strong>

<ul>
	<li>题目保证链表中节点的值互不相同</li>
	<li>若使用 C 或 C++ 语言，你不需要 <code>free</code> 或 <code>delete</code> 被删除的节点</li>
</ul>
