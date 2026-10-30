class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum=nums[0]
        curSum=nums[0]
        for r in range(1,len(nums)):
            if nums[r]>nums[r-1]:
                curSum+=nums[r]
            else:
                curSum=nums[r]
            maxSum=max(curSum,maxSum)
        return max(curSum,maxSum)



        