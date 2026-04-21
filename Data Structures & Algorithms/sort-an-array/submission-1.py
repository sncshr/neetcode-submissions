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

    def heapify(self,nums,n,i):
        largest=i
        left=(2*i)+1
        right=(2*i)+2
        if left<n and nums[left]>nums[largest]:
            largest=left
        if right<n and nums[right]>nums[largest]:
            largest=right
        if largest!=i:
            nums[i],nums[largest]=nums[largest],nums[i]
            self.heapify(nums,n,largest)
    def heapSort(self,nums):
        n=len(nums)
        #second half of this array is all leaves bc node k has children located at 2k+2,2k+1
        #calling heapify on internal nodes to store max nodes
        for i in range((n//2)-1,-1,-1):
            self.heapify(nums,n,i)
        for i in range(n-1,0,-1):
            nums[0],nums[i]=nums[i],nums[0]
            self.heapify(nums,i,0)
        return nums
        
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.heapSort(nums)
        