class Solution:
        # Recursion dosent work as its n^2 and a n memory
        # def canCompleteRecur(i,tank,visited):
        #     if visited==n:
        #         return True
        #     tank+=gas[i]
        #     if tank<cost[i]:
        #         return False
        #     return canCompleteRecur((i + 1) % n, tank - cost[i], visited + 1)

        # for i in range(n):
        #     if canCompleteRecur(i,0,0):
        #         return i
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        if sum(gas)<sum(cost):
            return -1
        tank=0
        start=0
        for i in range(n):
            tank+=gas[i]
            if tank>=cost[i]:
                tank-=cost[i]
            else:
                tank=0
                start=i+1
        return start

        