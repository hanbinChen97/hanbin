#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 1. find the a case start and end with odd
        # 2. find the number of even number before the start and after the end
        # 3. calculate the number of subarrays

        # if odd number in nums is less than k, return 0
        odd_count = len([i for i in nums if i % 2 == 1])
        if odd_count < k:
            return 0
        result = 0

        # create list of tuple:
        # (the number of even number before the odd number,
        # the number of even number after the odd number)
        even_before = 0
        even_after = 0
        odd_list = []

        first_odd = 0
        # find first even_before
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even_before += 1
            else:
                first_odd = i
                break

        # find the number of even_after
        for i in range(first_odd + 1, len(nums)):
            if nums[i] % 2 == 0:
                even_after += 1
            else:
                odd_list.append((even_before, even_after))
                even_before = even_after
                even_after = 0

        odd_list.append((even_before, even_after))

        for i in range(len(odd_list) - k + 1):
            result += (odd_list[i][0] + 1) * (odd_list[i + k - 1][1] + 1)

        return result

        # # if odd number in nums is less than k, return 0
        # odd_count = len([i for i in nums if i % 2 == 1])
        # if odd_count < k:
        #     return 0

        # # calculate the number of subarrays:
        # # calculate the number of odd number in nums
        # number_subarrays = odd_count - k + 1

        # result = 0

        # before = 0
        # after = 0

        # for i in range(len(nums)):
        #     # count befor
        #     if nums[i] % 2 == 0:
        #         before += 1

        #     if nums[i] % 2 == 1:
        #         number_subarrays -= 1

        #         last_odd_index = i

        #         # pass the next k - 1 odd numbers, find the last odd number index
        #         count = 0
        #         for j in range(i, len(nums)):
        #             if nums[j] % 2 == 1:
        #                 count += 1

        #             if count == k:
        #                 last_odd_index = j
        #                 count = 0
        #                 break

        #         # count after
        #         for j in range(last_odd_index + 1, len(nums)):
        #             if nums[j] % 2 == 0:
        #                 after += 1

        #             if nums[j] % 2 == 1:
        #                 break

        #         result += (before + 1) * (after + 1)
        #         before = 0
        #         after = 0

        #         if number_subarrays == 0:
        #             break

        # return result


# @lc code=end
