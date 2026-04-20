class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm={}
        retArr=[]
        for i in range(len(s)-1,-1,-1):
            if s[i] not in hm:
                hm[s[i]]=i
        end=0
        start=0
        for i,v in enumerate(s):
            end=max(end,hm[v])
            print(end)
            if i==end:
                retArr.append(end-start+1)
                start=i+1
        return retArr

        
        