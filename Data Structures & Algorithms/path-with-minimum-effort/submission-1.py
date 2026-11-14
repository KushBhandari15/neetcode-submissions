class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [[0, 0, 0]]
        visited = set()
        neigh = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if (r, c) == (ROWS - 1, COLS - 1):
                return diff
            
            for x, y in neigh:
                newR, newC = r + x, c + y
                if (0 <= newR < ROWS and 0 <= newC < COLS and 
                    (newR, newC) not in visited):
                    new_diff = max(
                        diff, abs(heights[r][c] - heights[newR][newC])
                    )
                    heapq.heappush(minHeap, [new_diff, newR, newC])
        

