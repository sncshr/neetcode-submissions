class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hm={}
        for i in arr:
            if i not in hm:
                hm[i]=1
            else:
                hm[i]+=1
        largest=-1
        for key in hm.keys():
            if hm[key]==key:
                if key>largest:
                    largest=key
        return largest
        
        