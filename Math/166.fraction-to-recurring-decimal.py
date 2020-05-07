#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return '0'
        res = []
        res += '-' if numerator/denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        ans,rem = divmod(numerator,denominator)
        res.append(ans)
        # print('*',ans,rem,res)
        if rem == 0:
            return ''.join(map(str,res))
        res.append('.')
        d = dict()
        while rem:
            if rem in d:
                res.insert(d[rem],'(')
                res.append(')')
                return ''.join(map(str,res))
            d[rem] = len(res)

            rem *= 10
            ans,rem = divmod(rem,denominator)
            res.append(ans)
            # print(res)
        return ''.join(map(str,res))
# @lc code=end

