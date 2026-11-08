class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            idx=abs(nums[i])-1
            nums[idx]=-1*abs(nums[idx])

        retArr=[]
        for i in range(len(nums)):
            if nums[i]>0:
                retArr.append(i+1)
        return retArr
            

        