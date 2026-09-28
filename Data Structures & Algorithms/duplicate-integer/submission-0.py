class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        snum = set()
        for num in nums:
            if num in snum:
                return True 
            snum.add(num)
        return False