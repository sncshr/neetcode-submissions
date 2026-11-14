class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        l=0
        for r in range(n):
            if nums[r]>nums[(r+1)%n]:
                l+=1
            if l>1:
                return False
        return True
            
