"""
https://leetcode.com/problems/merge-sorted-array/description/
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n >= m:
            nums1[:] = nums1[:-n]
            nums1[:] = nums1 + nums2
            nums1[:] = sorted(nums1)

    def merge_ref_1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a, b, write_index = m - 1, n - 1, m + n - 1

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a -= 1
            else:
                nums1[write_index] = nums2[b]
                b -= 1

            write_index -= 1


if __name__ == '__main__':
    solution = Solution()
    solution.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
    solution.merge_ref_1(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
