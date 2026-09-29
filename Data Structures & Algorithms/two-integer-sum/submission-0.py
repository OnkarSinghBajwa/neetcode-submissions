class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preM = {}

        for i, j in enumerate(nums):
            diff = target - j
            if diff in preM:
                return [preM[diff], i]
            preM[j] = i
        return []