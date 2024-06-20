#
# @lc app=leetcode id=1552 lang=python3
#
# [1552] Magnetic Force Between Two Balls
#

# @lc code=start
import math
from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        sortedPosition = sorted(position)
        minPos = sortedPosition[0]
        maxPos = sortedPosition[-1]

        minForce = 1
        maxForce = (maxPos - minPos) // (m - 1)
        force = math.ceil((maxForce + minForce) / 2)

        def check(force):
            count = 0
            prev = sortedPosition[0]

            for i in range(1, len(sortedPosition)):
                if sortedPosition[i] - prev >= force:
                    count += 1
                    prev = sortedPosition[i]

                if count == m - 1:
                    return True

            return False

        while minForce < maxForce:
            if check(force):
                minForce = force
            else:
                maxForce = force - 1

            force = math.ceil((maxForce + minForce) / 2)

        return force


# @lc code=end
