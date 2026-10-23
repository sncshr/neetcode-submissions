class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        retVal=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                if retVal==0:
                    continue
                else:
                    return retVal
            else:
                retVal+=1
        return retVal


        