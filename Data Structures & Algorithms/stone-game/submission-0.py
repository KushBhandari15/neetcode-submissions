class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        alice = 0
        bob = 0
        i, j = 0, len(piles) - 1
        player1 = True
        while i <= j:
            if piles[i] > piles[j]:
                if player1:
                    alice += piles[i]
                    i += 1
                else:
                    bob += piles[i]
                    j -= 1
            else:
                if player1:
                    alice += piles[j]
                    j -= 1
                else:
                    bob += piles[j]
                    j -= 1
        
        return alice > bob