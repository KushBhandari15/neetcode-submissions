class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        queue_R, queue_D = deque(), deque()

        for idx in range(len(senate)):
            senator = senate[idx]
            if senator == "R":
                queue_R.append(idx)
            else:
                queue_D.append(idx)
        
        
        while queue_R and queue_D:
            idx_R = queue_R.popleft()
            idx_D = queue_D.popleft()

            if idx_R < idx_D:
                queue_R.append(len(senate) + idx_R)
            else:
                queue_D.append(len(senate) + idx_D)
        
        return "Dire" if queue_D else "Radiant"

        


