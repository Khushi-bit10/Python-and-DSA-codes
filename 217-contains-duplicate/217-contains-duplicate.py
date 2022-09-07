class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=set(nums)
        if len(n)==len(nums):
            return False
        return True
        