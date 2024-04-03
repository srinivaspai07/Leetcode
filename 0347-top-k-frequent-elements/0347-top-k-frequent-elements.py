import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        counter = Counter(nums)
        
        # Step 2: Create a min heap to keep track of the k most frequent elements
        min_heap = []
        for num, freq in counter.items():
            # Push elements onto the heap with frequency as the key
            """
            n a min heap, elements are ordered based on the first value of each tuple in the heap. 
            In this case, the tuples being pushed onto the heap have the frequency (freq) as the first element.
            Therefore, when you push a tuple (freq, num) onto the min heap, the priority (or ordering) of 
            elements in the heap will be determined primarily by their frequencies (freq). 
            If two elements have the same frequency, then the tiebreaker will be the second value of the tuple, 
            which is num. However, within the context of the problem, it's unlikely for elements to have the same 
            frequency, so the primary sorting criterion will be the frequency itself.
            """

            heapq.heappush(min_heap, (freq, num))
            # If the heap size exceeds k, pop the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # Step 3: Return the elements from the min heap
        return [elem for _, elem in min_heap]
