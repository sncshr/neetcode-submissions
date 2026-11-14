class Solution:
    def check(self, nums: List[int]) -> bool:
        l=1
        n=len(nums)
        for r in range(1,2*n):
            if nums[(r-1)%n]<=nums[(r%n)]:
                l+=1
            else:
                l=1
            if l==n:
                return True
        return n==1
            
