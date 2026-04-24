class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr=''.join([char for char in s if char.isalnum()])
        cleanStr=cleanStr.lower()
        print(len(cleanStr))
        i,j=0,len(cleanStr)-1
        while i<j:
            if cleanStr[i]!=cleanStr[j]:
                return False
            i+=1
            j-=1
        return True
        
        