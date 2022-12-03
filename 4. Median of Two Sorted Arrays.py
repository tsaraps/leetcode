from typing import List
# Task
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Solution
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        nums1_len = len(nums1)
        median_index = nums1_len // 2
        if nums1_len % 2 == 0:
            median = (nums1[median_index - 1] + nums1[median_index ]) / 2
        else:
            median = nums1[median_index]
        return median


s = Solution()
result = s.findMedianSortedArrays([1, 2], [3, 4])
print(result)
