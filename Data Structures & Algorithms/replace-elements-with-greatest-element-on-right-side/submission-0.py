class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)<=1:
            return [-1]
        maxVal=-1
        for i in range(len(arr)-1,-1,-1):
            curr=arr[i]
            arr[i]=maxVal
            maxVal=max(maxVal, curr)
        return arr


        