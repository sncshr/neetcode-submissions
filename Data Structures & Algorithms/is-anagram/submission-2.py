class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersA=[0]*26
        if len(s)!=len(t):
            return False
        for i in s:
            lettersA[ord(i)-97]+=1
        for i in t:
            if lettersA[ord(i)-97]==0:
                return False
            lettersA[ord(i)-97]-=1
        return sum(lettersA)==0
        