# ZIhaoLeetcode
Leetcode problem practices
# 题型归纳
大致归拢一下我遇到比较常见的题型 

(感谢 **@labuladong** 公众号，大部分总结资料源自他的repo)
1. 动态规划
    * [简介](https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E8%AF%A6%E8%A7%A3%E8%BF%9B%E9%98%B6.md)
    * [进阶](https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E8%AF%A6%E8%A7%A3%E8%BF%9B%E9%98%B6.md)
2. [双指针](https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E5%8F%8C%E6%8C%87%E9%92%88%E6%8A%80%E5%B7%A7.md)
    * 快慢指针
    * 左右指针
    * [二分查找](https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE%E8%AF%A6%E8%A7%A3.md)
    * [滑动窗口](https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%8A%80%E5%B7%A7.md)
3. 哈系表
    * [prefix sum及优化](https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E5%89%8D%E7%BC%80%E5%92%8C%E6%8A%80%E5%B7%A7.md)
4. 树
    * DFS/BFS
5. [回溯](https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E8%AF%A6%E8%A7%A3%E4%BF%AE%E8%AE%A2%E7%89%88.md)
    * （DFS的一种变形，一般用来求**所有可能的解**）
    * [排列组合/子集](https://github.com/labuladong/fucking-algorithm/blob/master/%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E7%B3%BB%E5%88%97/%E5%AD%90%E9%9B%86%E6%8E%92%E5%88%97%E7%BB%84%E5%90%88.md)
6. [链表](https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E5%8F%8C%E6%8C%87%E9%92%88%E6%8A%80%E5%B7%A7.md)
    * 反转链表
    * 环
7. 图
    * topological sort （依赖关系）
    * DFS/BFS
    * 环/critical connections
8. bit位操作 （不大熟悉）
9. stack
    * [单调栈](https://github.com/labuladong/fucking-algorithm/blob/master/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E7%B3%BB%E5%88%97/%E5%8D%95%E8%B0%83%E6%A0%88.md)
    * [区间调度](https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E4%B9%8B%E5%8C%BA%E9%97%B4%E8%B0%83%E5%BA%A6%E9%97%AE%E9%A2%98.md)
    * [区间合并](https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E5%8C%BA%E9%97%B4%E8%B0%83%E5%BA%A6%E9%97%AE%E9%A2%98%E4%B9%8B%E5%8C%BA%E9%97%B4%E5%90%88%E5%B9%B6.md)
    * [区间交集](https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E5%8C%BA%E9%97%B4%E4%BA%A4%E9%9B%86%E9%97%AE%E9%A2%98.md)
10. OOP/Design
11. 常有数据结构/算法
    * sort => bucket sort
    * dict/set
    * heap （min heap）
    * xor
    * [union find](https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/UnionFind%E7%AE%97%E6%B3%95%E8%AF%A6%E8%A7%A3.md)
        * [union find sudo code](./UnionFind/uf.md)
    * tries
    * [min/max queue](https://github.com/labuladong/fucking-algorithm/blob/master/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E7%B3%BB%E5%88%97/%E5%8D%95%E8%B0%83%E9%98%9F%E5%88%97.md)
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
