class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def insertion_sort(bucket):

            n = len(bucket)
            for i in range(1, n):
                key = bucket[i]
                j = i - 1
                while j >= 0 and bucket[j] > key:
                    bucket[j + 1] = bucket[j]
                    j -= 1
                bucket[j + 1] = key
            
        n = len(nums)
        min_val = min(nums)
        max_val = max(nums)
        num_range = max_val - min_val + 1
        buckets = [[] for _ in range(n)]

        for num in nums:
            idx = (num - min_val) * n // num_range
            print(idx)
            buckets[idx].append(num)
        
        res = []
        for bucket in buckets:
            insertion_sort(bucket)
            res.extend(bucket)
        
        return res