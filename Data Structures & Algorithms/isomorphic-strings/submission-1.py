class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hSet={}
        bSet={}
        for i in range(len(s)):
            if s[i] not in hSet:
                hSet[s[i]]=t[i]
            if t[i] not in bSet:
                bSet[t[i]]=s[i]
            if s[i] in hSet and hSet[s[i]]!=t[i]:
                return False
            if t[i] in bSet and bSet[t[i]]!=s[i]:
                return False
        return True                


        