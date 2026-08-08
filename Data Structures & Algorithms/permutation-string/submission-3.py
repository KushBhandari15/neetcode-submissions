class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        helper = {}

        def fill_set():
            helper.clear()
            for char in s1:
                helper[char] = helper.get(char, 0) + 1
        
        left, right = 0, 0
        count = 0
        fill_set()

        while right < len(s2):
            
            if helper.get(s2[right], 0) > 0:
                helper[s2[right]] -= 1
                count += 1
                if count == len(s1):
                    return True
                right += 1
            else:
                left += 1
                right = left
                fill_set()
                count = 0
        
        return False