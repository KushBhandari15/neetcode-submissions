class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        matched = [False, False, False]

        for triplet in triplets:
            
            if any(triplet[i] > target[i] for i in range(3)):
                continue

            for i in range(3):
                if triplet[i] == target[i]:
                    matched[i] = True
        
        return all(matched)