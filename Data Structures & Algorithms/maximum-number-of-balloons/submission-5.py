class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hm={}
        for i in text:
            if i not in hm:
                hm[i]=1
            else:
                hm[i]+=1
        strX="balloon"
        minCount=float('inf')
        for i in strX:
            count=hm.get(i,0)
            if i=='l' or i=='o':
                count//=2
            minCount=min(minCount,count)
        return minCount



        