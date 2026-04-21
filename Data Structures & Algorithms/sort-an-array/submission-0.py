class Solution:
    def merge(self,nums,L,mid,R):
        left,right=nums[L:mid+1],nums[mid+1:R+1]
        i,j,k=L,0,0
        while j<len(left) and k<len(right):
            if left[j]<=right[k]:
                nums[i]=left[j]
                j+=1
            else:
                nums[i]=right[k]
                k+=1
            i+=1
        while j<len(left):
            nums[i]=left[j]
            j+=1
            i+=1
        while k<len(right):
            nums[i]=right[k]
            k+=1
            i+=1
        return nums

    def mergeSort(self,nums,l,r):
        if l==r:
            return nums
        mid=(l+r)//2
        self.mergeSort(nums,l,mid)
        self.mergeSort(nums,mid+1,r)
        self.merge(nums,l,mid,r)
        return nums


    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums,0,len(nums)-1)
        