class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # 1 2 3 0 0 0
        # 2 5 6

        curr = len(nums1) - 1
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0 and curr >= 0:
            if nums1[i] <= nums2[j]:
                nums1[curr] = nums2[j]
                j -= 1
            else:
                nums1[curr] = nums1[i]
                i -= 1
            curr -= 1
        
        while i >= 0:
            nums1[curr] = nums1[i]
            i -= 1
            curr -= 1
        while j >= 0:
            nums1[curr] = nums2[j]
            j -= 1
            curr -= 1
            
