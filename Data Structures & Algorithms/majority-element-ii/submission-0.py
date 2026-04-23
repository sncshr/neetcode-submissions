class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm=defaultdict(int)
        totalKeys=0
        prev=-1
        for i in nums:
            hm[i]+=1
            if len(hm)<=2:
                continue
            newHM=defaultdict(int)
            for n,c in hm.items():
                if c>1:
                    newHM[n]=c-1
            hm=newHM
        retVal=[]
        for i in hm:
            if nums.count(i)>len(nums)//3:
                retVal.append(i)
        return retVal

        