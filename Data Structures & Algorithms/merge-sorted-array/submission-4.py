class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(m, len(nums1)):
            nums1[i] = nums2[i - m]
        
        j = m
        while j < m + n:
            i = 0
            for i in range(j):
                if nums1[i] > nums1[j]:
                    nums1[i], nums1[j] = nums1[j], nums1[i]
            j += 1
        
