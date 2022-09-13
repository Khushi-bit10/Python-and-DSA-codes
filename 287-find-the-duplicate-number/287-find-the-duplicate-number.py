class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        answer={}
        k=answer.keys()
        for i in nums:
            if i not in k:
                answer[i]=1
            else:
                return i