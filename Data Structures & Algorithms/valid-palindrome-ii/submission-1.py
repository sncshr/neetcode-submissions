class Solution:
    def isPalindrome(self,cleanStr,i,j):
        while i<j:
            if cleanStr[i]!=cleanStr[j]:
                return False
            i+=1
            j-=1
        return True
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return (self.isPalindrome(s,l+1,r)or self.isPalindrome(s,l,r-1))
            l+=1
            r-=1
        return True


        
        