"""
228. Summary Ranges

Easy

https://leetcode.com/problems/summary-ranges/description/
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output_list = []

        # Catch empty list
        if len(nums) == 0:
            return output_list

        smallest_number = nums[0]
        for idx, number in enumerate(nums):
            if number + 1 not in nums:
                if number == smallest_number:
                    output_list.append(f'{smallest_number}')
                else:
                    output_list.append(f'{smallest_number}->{number}')

                if idx < len(nums) - 1:
                    smallest_number = nums[idx + 1]
        return output_list


if __name__ == '__main__':
    # nums = [0, 1, 2, 4, 5, 7]
    nums = [0, 2, 3, 4, 6, 8, 9]

    solution = Solution()
    solution.summaryRanges(nums=nums)
