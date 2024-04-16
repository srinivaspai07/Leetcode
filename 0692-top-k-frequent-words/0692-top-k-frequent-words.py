from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words:
            return []

        # Count the frequency of each word
        count = Counter(words)

        # Define the min-heap to store the k most frequent words
        minHeap = []

        # Iterate through the word frequency dictionary
        for word, freq in count.items():
            # Push the word and its frequency into the min-heap
            # Sort by negative frequency and then by lexicographical order
            heapq.heappush(minHeap, (-freq, word))

        # Extract the k most frequent words from the min-heap
        result = []
        for _ in range(k):
            # Pop the word and its negative frequency from the heap
            freq, word = heapq.heappop(minHeap)
            # Append the word to the result list
            result.append(word)

        return result
