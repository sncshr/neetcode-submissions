class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        n=len(nums)
        count=0
        while i<n:
            if nums[i]==val:
                nums[i]=nums[n-1]
                n-=1
                count+=1
            else:
                i+=1
        return len(nums)-count