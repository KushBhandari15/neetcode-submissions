class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        dp = {}
        def helper(i):
            nonlocal n, dp
            if i >= n:
                return True
            if i in dp:
                return dp[i]

            for word in wordDict:
                if s[i:].startswith(word):
                    print(f"Found {word} in {s[i:]}")
                    if helper(i+len(word)):
                        return True
            
            dp[i] = False
            return False

        return helper(0)
