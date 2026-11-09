class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter=[0]*101
        for h in heights:
            counter[h]+=1
        retVal=0
        idx=0
        for h in range(1,101):
            while counter[h]>0:
                if heights[idx]!=h:
                    retVal+=1
                idx+=1
                counter[h]-=1
        return retVal
        