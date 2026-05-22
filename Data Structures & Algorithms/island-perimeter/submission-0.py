from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    visited.add((i, j))
                    break
            if q:
                break

        perimeter = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            i, j = q.popleft()

            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    perimeter += 1

                elif grid[ni][nj] == 0:
                    perimeter += 1

                elif (ni, nj) not in visited:
                    visited.add((ni, nj))
                    q.append((ni, nj))

        return perimeter