class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        retVal=r
        def canShip(mid):
            ships,curr=1,mid
            for w in weights:
                if curr-w<0:
                    ships+=1
                    curr=mid
                curr-=w
            return ships<=days
        while l<=r:
            mid=l+((r-l)//2)
            if canShip(mid):
                retVal=min(mid, retVal)
                r=mid-1
            else:
                l=mid+1
        return retVal


        