class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc=dec=ret=1
        for r in range(1,len(nums)):
            if nums[r]>nums[r-1]:
                inc+=1
                dec=1
            elif nums[r]<nums[r-1]:
                dec+=1
                inc=1
            else:
                inc=dec=1
            ret=max(inc,dec,ret)
        return max(inc,dec,ret)
        