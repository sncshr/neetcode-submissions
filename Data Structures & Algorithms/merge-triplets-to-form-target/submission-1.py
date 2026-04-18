class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tx,ty,tz=target
        a,b,c=False,False,False
        for x,y,z in triplets:
            if x<=tx and y<=ty and z<=tz:
                if x==tx:
                    a=True
                if y==ty:
                    b=True
                if z==tz:
                    c=True
        return a and b and c

        