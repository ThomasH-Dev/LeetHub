class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        
        q = collections.deque()
        rows = len(rooms)
        cols = len(rooms[0])
        visit = set()

        
        
        
        """
        Do not return anything, modify rooms in-place instead.
        """
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    visit.add((r,c))
                    q.append((r,c))
        print(q)
        while q:
            
            r, c = q.popleft()
            # print(r,c)
           
            
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            
            for dr, dc in directions:
                drows = r + dr
                dcols = c + dc
                if drows in range(rows) and dcols in range(cols) and (drows,dcols) not in visit and rooms[drows][dcols] != -1:
                    visit.add((drows,dcols))
                    q.append((drows,dcols))
                    rooms[drows][dcols] = rooms[r][c] + 1
        print(rooms)
        return rooms