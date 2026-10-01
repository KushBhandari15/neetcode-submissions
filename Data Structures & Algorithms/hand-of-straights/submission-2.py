from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand)%groupSize:
            return False

        counter = Counter(hand)
        minH = list(counter.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
                    del counter[i]
        return True