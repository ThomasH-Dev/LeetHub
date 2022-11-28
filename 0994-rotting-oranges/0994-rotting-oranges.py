class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        freshOranges = 0
        rows = len(grid)
        cols = len(grid[0])
        maxCount = 0
        q = deque()
       
            
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    freshOranges +=1
                if grid[r][c] == 2:
                    q.append((r,c))
        
                 
        while q and freshOranges > 0:
            count +=1
            for i in range(len(q)):
                
                r,c = q.popleft()
                
                
                 
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    if (r+dr) in range(rows) and (c+dc) in range(cols) and (r +dr) >= 0 and (c+dc) >=0 and grid[r +dr][c+ dc] == 1:
                        #why did rotten oranges have to be subtracted here and not above
                        q.append((r+dr,c+dc))
                        grid[r+dr][c+dc] = 2
                        freshOranges -=1
        print(freshOranges)
        if freshOranges != 0:
            return -1
        else: 
            return count
        
                        
                    
                    
                
                
                
        