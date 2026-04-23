class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countZero=0
        countOne=0
        countTwo=0
        for i in range(len(nums)):
            if nums[i]==0:
                countZero+=1
            elif nums[i]==1:
                countOne+=1
            else:
                countTwo+=1
        for i in range(len(nums)):
            if countZero>0:
                nums[i]=0
                countZero-=1
                continue
            if countOne>0:
                nums[i]=1
                countOne-=1
                continue
            nums[i]=2
        return nums

        