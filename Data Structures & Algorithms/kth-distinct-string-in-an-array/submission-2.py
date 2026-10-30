class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        retVal=''
        hm={}
        for i in arr:
            if i not in hm:
                hm[i]=1
            else:
                hm[i]+=1
        for x in hm.keys():
            if hm[x]==1:
                k-=1
                if k==0:
                    return x
        return retVal
        