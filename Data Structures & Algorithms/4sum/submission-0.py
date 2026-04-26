class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        retVal=[]
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
                break
            if nums[i]+nums[n-1]+nums[n-2]+nums[n-3]<target:
                continue
            for j in range(i+1,n-2):
                l=j+1
                r=n-1
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                if nums[i]+nums[j]+nums[j+1]+nums[j+2]>target:
                    break
                if nums[i]+nums[j]+nums[n-1]+nums[n-2]<target:
                    continue
                while l<r:
                    total=nums[i]+nums[j]+nums[l]+nums[r]
                    if total==target:
                        retVal.append([nums[i],nums[j],nums[l],nums[r]])
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r]==nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
                    elif total<target:
                        l+=1
                    else:
                        r-=1
        return retVal



        

        