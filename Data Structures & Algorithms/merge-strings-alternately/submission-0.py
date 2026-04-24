class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        retWord=""
        while i<len(word1) and j<len(word2):
            retWord=retWord+word1[i]+word2[j]
            i+=1
            j+=1
        if i<len(word1):
            retWord=retWord+word1[i:]
        
        if j<len(word2):
            retWord=retWord+word2[j:]
        return retWord 
        