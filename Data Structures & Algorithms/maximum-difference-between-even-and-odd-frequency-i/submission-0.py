class Solution:
    def maxDifference(self, s: str) -> int:
        counts=Counter(s)
        oddMax,evenMin=0,len(s)
        for c in counts.values():
            if c & 1:
                oddMax=max(c,oddMax)
            else:
                evenMin=min(evenMin,c)
        return oddMax-evenMin
        