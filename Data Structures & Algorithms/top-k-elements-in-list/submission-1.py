class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        helper = {}
        for num in nums:
            helper[num] = helper.get(num, 0) + 1
        
        sorted_dict_desc = sorted(helper.items(), key=lambda item: item[1], reverse=True)
        values = [item[0] for item in sorted_dict_desc]
        return values[:k]