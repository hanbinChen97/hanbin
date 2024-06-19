#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#

# @lc code=start
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if m * k > len(bloomDay):
            return -1

        bloomDay_sorted = sorted(bloomDay)

        min = m * k - 1
        max = len(bloomDay_sorted) - 1
        mid = min + (max - min) // 2

        def checkDay(day):
            count = 0
            count_bouquet = 0

            for flower in bloomDay:
                if flower <= day:
                    count += 1

                    if count == k:
                        count_bouquet += 1
                        count = 0

                        if count_bouquet == m:
                            return True

                else:
                    count = 0

            return False

        while min < max:
            if checkDay(bloomDay_sorted[mid]):
                max = mid
            else:
                min = mid + 1
                
            mid = min + (max - min) // 2

        return bloomDay_sorted[mid]


# @lc code=end
