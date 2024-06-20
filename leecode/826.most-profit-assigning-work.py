#
# @lc app=leetcode id=826 lang=python3
#
# [826] Most Profit Assigning Work
#

# @lc code=start
from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        maxp = 0

        # combine difficulty and profit
        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        best = 0

        # 双指针
        i = 0
        n = len(jobs)
        for ability in worker:
            # job with difficulty <= ability
            while i < n and jobs[i][0] <= ability:
                best = max(best, jobs[i][1])
                i += 1
            maxp += best

        return maxp


# @lc code=end
