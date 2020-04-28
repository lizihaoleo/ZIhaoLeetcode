# 正则匹配
LC 10

正则匹配很经典的dp问题，基本上就是建立二维的dp，然后遍历整个dp矩阵。
## Top down + memorization
通常来说top down的解法我觉得比较容易想出来。
top down的方法就是给2个指针，递归的遍历2个字符窜，当2个指针都超出边界时可以认为检查完成，退出递归。

这道题从右往左便利比较容易。这道题目的base case还是有点特殊的，最开始我以为
<pre><code># base case
if i < 0 and j< 0: return True
</code></pre>
很自然的想指针跳出区间则可以判定匹配成功，然而有以下情况：
<pre><code>
   i                i                          i
s: a a    -->   (1) a a             or      (2)  a a
p: a *              a *                          a *
     j            j                                j
i = 0; j = 1      i = 0; j = -1                 i=-1;j=1
</code></pre>
可以看到 i=0, j=1可以分成2种情况：

（1）是假设p里面的a\*表示a匹配0次，这种情况下只要将j-2;

（2）是假设a\*表示a出现多次，这有个前提就是\*号前的字符必须和i号字符匹配（p[j-1] == s[i] 或 .），如果是这样的话这时候j不动而i-1

在（2）的时候如果用之前的base case就会无法退出，继续匹配，无法成功退出。

那么稍作修改，对i<0和j<0进行分开讨论，可得到一下base case：
<pre><code># base case
if j==-1:
    return i == -1
if i==-1:
    if p[j]=="*" and j>=1:
        return helper(i,j-2)
    else:
        return False
</code></pre>
感觉不太优美但是有用：）

上面的例子已经讨论了遇到\*如何处理，那么遇到.的话，因为.代表任意字符，所以只需要默认当前i，j匹配成功即可,2指针同时-1.

所以最终代码如下（用了python的lru_cache做meorization，fancy）
<pre><code>def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s), len(p)
        from functools import lru_cache
        @lru_cache(None)
        # from right to left
        def helper(i,j):
            # base case
            if j==-1:
                return i == -1
            if i==-1:
                if p[j]=="*" and j>=1:
                    return helper(i,j-2)
                else:
                    return False
            # same char or p[j] is '.' -> move to right
            if s[i] == p[j] or p[j] == '.':
                return helper(i-1,j-1)
            elif p[j] == '*' and j >= 1:
                pre_match = p[j-1] in {s[i],'.'}
                return helper(i,j-2) \
                    or (pre_match and helper(i-1,j)) # char match zero or more than one time

            return False
        
        return helper(m-1,n-1)
</code></pre>

还有从左到右的匹配代码，基本思路一样的/
<pre><code>def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s), len(p)
        from functools import lru_cache
        @lru_cache(None)
        # from right to left
        def helper(i,j):
            if j==m:
                return (i==n)
            
            if i==n:
                if j+1!=m and p[j+1]=="*":
                    return helper(i,j+2)
                else:
                    return False
            
            # now i&ltn and j&ltm
            if j+1!=m and p[j+1]=="*":
                res = ((s[i]==p[j] or p[j]==".") and helper(i+1,j)) or helper(i,j+2)
                return res
            
            # now i&ltn and j&ltm and p[j+1]!="*"
            if s[i]==p[j] or p[j]==".":
                return helper(i+1,j+1)
            return False
        
        return helper(0,0)
</code></pre>

时间和空间复杂度O(M*N)

## Bottom up
Bottom up我觉得很难一下想出来，但通过top down的观察可以将矩阵和转移方程找出。这类有两个字符窜的题目很明显要建立二维数组：
|   | # | a | a |
|---|---|---|---|
| # |   |   |   |
| a |   |   |   |
| * |   |   |   |
(# 表示字符窜开头-1的位置)

如之前讨论的，当遇到\*的时候dp[i][j]取决与 dp[i][j-1] （\*前字符匹配大于0次）或 dp[i-2][j] （\*前字符匹配0次） 

（\*由于pytho矩阵先选行再选列，这里i和j的含义一上面top down掉转了）。

有一点注意的是初始化第一列的时候，当遇到\*符号时 dp[i][0] 只考虑 dp[i-2][0]，这是因为此时s字符窜是空的。观察上面的表格应该很好理解了。

有一个小技巧，因为我们的dp矩阵多一个空的字符号在两个字符窜前，我们可以给s和p前面都加一个空格，方便我们遍历字符窜。

代码如下（这是从左到右匹配）：
<pre><code>def isMatch(self, s: str, p: str) -> bool:
        s, p = ' '+ s, ' '+ p
        lenS, lenP = len(s), len(p)
        dp = [[0]*lenS for _ in range(lenP)]
        dp[0][0] = 1
        for i in range(1, lenP):
            if p[i] == '*':
                dp[i][0] = dp[i-2][0]
                
        for i in range(1,lenP):
            for j in range(1,lenS):
                if p[i] == s[j] or p[i] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i] == '*':
                    if p[i-1] == '.' or p[i-1] == s[j]:
                        dp[i][j] = dp[i][j-1] or dp[i-2][j]
                    else:
                        dp[i][j] = dp[i-2][j]

        return dp[-1][-1]
</code></pre>
时间和空间复杂度O(M*N)
