class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stck=[]
        prev=0
        for i in asteroids:
            while stck and i<0 and stck[-1]>0:
                diff=i+stck[-1]
                if diff<0:
                    stck.pop()
                elif diff>0:
                    i=0
                else:
                    i=0
                    stck.pop()
            if i:
                stck.append(i)
        return stck
        