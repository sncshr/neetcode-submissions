class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        memo={}
        def recurEdit(w1,w2):
            if w1==m:
                return n-w2
            if w2==n:
                return m-w1
            if (w1,w2) in memo:
                return memo[(w1,w2)]
            if word1[w1]==word2[w2]:
                return recurEdit(w1+1,w2+1)
            minVal=min(recurEdit(w1+1,w2),recurEdit(w1,w2+1))
            minVal=min(minVal,recurEdit(w1+1,w2+1))
            memo[(w1,w2)]=minVal+1
            return minVal+1
        return recurEdit(0,0)


        