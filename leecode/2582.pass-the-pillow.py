#
# @lc app=leetcode id=2582 lang=python3
#
# [2582] Pass the Pillow
#

# @lc code=start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if n == 1:
            return 1

        if time % (2 * n - 2) == 0:
            return 1

        if time % (2 * n - 2) <= n - 1:
            return time % (2 * n - 2) + 1

        return 2 * n - 1 - time % (2 * n - 2)
        
        
# @lc code=end


