class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=-1
        maxLen=0
        for r in range(len(nums)):
            if nums[r]==1:
                if l==-1:
                    l=r
                maxLen=max(maxLen,r-l+1)
            else:
                l=-1
        return maxLen
                


        