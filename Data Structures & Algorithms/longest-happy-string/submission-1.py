import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        counts = [a, b, c]
        letters = ['a', 'b', 'c']
        my_heap = []
        for i in range(3):
            if counts[i] > 0:
                heapq.heappush(my_heap, (-counts[i], i))

        res = []

        while my_heap:
            freq, most = heapq.heappop(my_heap)

            if len(res) >= 2 and res[-1] == res[-2] == letters[most]:
                if not my_heap:
                    break

                freq_2, most_2 = heapq.heappop(my_heap)
                res.append(letters[most_2])
                freq_2 += 1

                if freq_2 < 0:
                    heapq.heappush(my_heap, (freq_2, most_2))
                
                heapq.heappush(my_heap, (freq, most))
            else:
                res.append(letters[most])
                freq += 1
                if freq < 0:
                    heapq.heappush(my_heap, (freq, most))
    
        return "".join(res)