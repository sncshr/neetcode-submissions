class Solution:
    def reverse(self, x: int) -> int:
        retVal=0
        minVal= -2147483648
        maxVal=2147483648
        while x:
            dgit= int(math.fmod(x,10))
            x=int(x/10)
            if (retVal>maxVal//10 or (retVal==maxVal//10 and dgit>=maxVal%10)):
                return 0
            if (retVal<minVal//10 or (retVal==minVal//10 and dgit<=minVal%10)):
                return 0
            retVal=(retVal*10)+dgit
        return retVal

        