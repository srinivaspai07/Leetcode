class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index_word1 = -1  # Initialize the index of word1
        index_word2 = -1  # Initialize the index of word2
        min_distance = float('inf')  # Initialize the minimum distance
        
        # Iterate through the words in the list
        for i, word in enumerate(wordsDict):
            # If the current word matches word1, update its index
            if word == word1:
                index_word1 = i
            # If the current word matches word2, update its index
            elif word == word2:
                index_word2 = i
            
            # If both word1 and word2 have been found, calculate the distance
            if index_word1 != -1 and index_word2 != -1:
                min_distance = min(min_distance, abs(index_word1 - index_word2))
        
        return min_distance
