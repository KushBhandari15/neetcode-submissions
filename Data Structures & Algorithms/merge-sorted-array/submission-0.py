class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        counter = n
        while counter > 0:
            nums1.pop()
            counter -= 1
        
        print(f"Array after popping: {nums1}")

        nums1 += nums2


        return nums1.sort()