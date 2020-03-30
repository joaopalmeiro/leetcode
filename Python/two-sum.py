from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num_index, num in enumerate(nums):
            subtarget = target - num

            if subtarget in nums:
                subtarget_index = nums.index(subtarget)

                if subtarget_index != num_index:
                    return [num_index, subtarget_index]

        return []


print(Solution().twoSum([2, 7, 11, 15], 9))
