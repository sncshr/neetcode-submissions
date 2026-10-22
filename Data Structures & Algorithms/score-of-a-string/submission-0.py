class Solution:
    def scoreOfString(self, s: str) -> int:
        score=0
        for i in range(len(s)-1):
            a,b=tuple(s[i:i+2])
            print(a)
            print(b)
            diff=abs(ord(b)-ord(a))
            score+=diff
        return score

        