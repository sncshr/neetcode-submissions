class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        while l<=r:
            mid=l+(r-l)//2
            if x==(mid*mid):
                return mid
            elif x>(mid*mid):
                l=mid+1
            else:
                r=mid-1

        return r


        