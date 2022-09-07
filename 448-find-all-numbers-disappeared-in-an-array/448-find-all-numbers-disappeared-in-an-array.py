class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != i+1 and nums[j] != j+1:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        dis = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                dis.append(i+1)
        return dis
        