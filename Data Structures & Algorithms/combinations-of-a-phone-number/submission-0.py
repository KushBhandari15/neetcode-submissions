class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
            
        mapped = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        res, sol = [], []
        n = len(digits)

        def helper(i):

            if i >= n:
                res.append("".join(sol))
                return
            
            for letter in mapped[digits[i]]:
                sol.append(letter)
                helper(i+1)
                sol.pop()
            
        helper(0)
        return res

