class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hSet=set()
        for i in nums:
            if i not in hSet:
                hSet.add(i)
        maxVal=len(nums)
        retArr=[]
        for i in range(1,maxVal+1):
            if i not in hSet:
                retArr.append(i)
        return retArr
            

        