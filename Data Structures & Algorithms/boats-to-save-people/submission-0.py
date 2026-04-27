class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        countBoats=0
        people.sort()
        l,r=0,len(people)-1
        while l<=r:
            sum=people[l]+people[r]
            if sum<=limit:
                countBoats+=1
                l+=1
                r-=1
            else:
                if people[r]<=limit:
                    countBoats+=1
                r-=1
        return countBoats
            

        