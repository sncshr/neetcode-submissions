class Solution:
    def jump(self, nums: List[int]) -> int:
        memo={}
        def recurJump(curr):
            if curr>=len(nums)-1:
                return 0
            if curr in memo:
                return memo[curr]
            minVal=float('inf')
            for i in range(1,nums[curr]+1):
                res=recurJump(curr+i)
                if res!=float('inf'):
                    minVal=min(minVal,1+res)
            memo[curr]=minVal
            return minVal
        def greedyJump():
            retVal=0
            l=r=0
            end=0
            farthest=0
            while r<(len(nums)-1):
                farthest=max(farthest,r+nums[r])
                if r==end:
                    retVal+=1
                    end=farthest
                r+=1
            return retVal




        return greedyJump()



        