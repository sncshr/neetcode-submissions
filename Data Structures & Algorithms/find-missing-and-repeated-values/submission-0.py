class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        hm=defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                hm[grid[i][j]]+=1
        double, missing=0,0
        for i in range(1, n*n +1):
            if hm[i]==0:
                missing=i
            if hm[i]==2:
                double=i
        return [double, missing]
        

        