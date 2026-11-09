class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        hmA={}
        hmB={}
        if len(words)!=len(pattern):
            return False
        for c in range(len(pattern)):
            pat=pattern[c]
            wrd=words[c]
            if pat in hmA:
                if hmA[pat]!=wrd:
                    return False
            else:
                hmA[pat]=wrd
            if wrd in hmB:
                if hmB[wrd]!=pat:
                    return False
            else:
                hmB[wrd]=pat
            
        return True
        