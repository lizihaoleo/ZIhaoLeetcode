# ZIhaoLeetcode
Leetcode problem practices
# 题型归纳
大致归拢一下我遇到比较常见的题型
1. dp
2. 双指针
    * 快慢指针
    * 左右指针
    * 二分查找
    * 滑动窗口
3. 哈系表
    * prefix sum及优化
4. 树
    * DFS/BFS
5. 回溯
    * DFS的一种变形
    * 求所有可能的解
    * 排列/组合
    * 子集
6. 链表 （不大熟悉）
    * 反转链表
    * 环
7. 图
    * topological sort （依赖关系）
    * DFS/BFS
    * 环/critical connections
8. bit位操作 （不大熟悉）
9. stack
    * 单调栈/队列
    * 区间合并
    * 区间集合
10. OOP/Design
11. 常有数据结构/算法
    * sort => bucket sort
    * dict/set
    * heap （min heap）
    * xor
    * union find
    * tries
    * min/max queue
    * segement line tree (optional)
    * KMP (optional)

## 一些套路

### DP：
    矩阵和 Array 通常都是 DP
    问数量的通常都是 DP
    问是否可以，也很有可能 DP
    找Max， Min的问题
    发现可能性的问题
    输出所有解的个数问题

    *不适用场景
    列出所有具体方案（起码是指数级别的复杂度，通常是递归，backtracking）
    集合问题

    *套路
    状态
    转移方程
    初始化条件
    返回结果

    矩阵DP:
    这种问题需要初始化DP数组，第0行和第0列，这样会方便之后的操作

    通常这种问题是只能向右或者向下操作，否则则需要用BFS–求最短路径；DFS来解决

如果问题存在时间O(n2)和空间O(1), 那么可能有 

    1）用dict或set转为时间空间O(n) 

    2）用排序实现时间O(nlgn) 空间O(1)

如果input排序好了，二分法或者双指针

如果 top/max/min/closest k element, 用heap

递归都可以借助while stack转化为迭代

Array问题可以双指针或左右两方向遍历再结合

找两个字符串的公共子串，需要dict或trie

链表并且不能有额外空间，快慢指针

如果问最短，最少，BFS

如果问连通性，静态就是 DFS, BFS，动态就 UnionFind

如果问依赖性就 topo sort

DAG 的问题就 dfs+memo (不懂)

求所有解的，基本 backtracking

排序总是可以想一想的，尤其排序O(1), 很可能bucket sort

万事总可以想HashMap

找规律试试Stack