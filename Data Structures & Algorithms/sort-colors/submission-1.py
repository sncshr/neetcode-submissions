class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #one pass dutch national flag algo
        l,r=0,len(nums)-1
        i=0
        def swap(i,j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        while i<=r:
            if nums[i]==0:
                swap(l,i)
                l+=1
            elif nums[i]==2:
                swap(i,r)
                r-=1
                i-=1
            i+=1

        #intuitive 2 pass
        # countZero=0
        # countOne=0
        # countTwo=0
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         countZero+=1
        #     elif nums[i]==1:
        #         countOne+=1
        #     else:
        #         countTwo+=1
        # for i in range(len(nums)):
        #     if countZero>0:
        #         nums[i]=0
        #         countZero-=1
        #         continue
        #     if countOne>0:
        #         nums[i]=1
        #         countOne-=1
        #         continue
        #     nums[i]=2
        # return nums

        