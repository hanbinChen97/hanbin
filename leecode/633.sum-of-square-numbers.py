#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c ** 0.5)
        while left <= right:

            if left ** 2 + right ** 2 == c:
                return True

            elif left ** 2 + right ** 2 < c:
                left += 1

            else:
                right -= 1
        return False


# @lc code=end
