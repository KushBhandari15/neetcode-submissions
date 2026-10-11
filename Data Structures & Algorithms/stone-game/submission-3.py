class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        dp = {}

        def helper(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            even = True if (r - l) % 2 else False
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            dp[(l, r)] = max(helper(l + 1, r) + left,
                            helper(l, r - 1) + right)

            return dp[(l, r)]

        res = helper(0, len(piles) - 1)
        if res > sum(piles) - res:
            return True
        