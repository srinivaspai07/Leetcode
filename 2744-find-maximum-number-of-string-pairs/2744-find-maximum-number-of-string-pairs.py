from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen_pairs = set()
        count = 0

        for word in words:
            reversed_word = word[::-1]

            # Check if the reversed pair has been seen before
            if reversed_word in seen_pairs:
                count += 1
                seen_pairs.remove(reversed_word)  # Remove the pair to avoid double-counting
            else:
                seen_pairs.add(word)

        return count
