class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a dictionary to store anagrams
        anagrams = {}
        
        for word in strs:
            # Sort the characters of the word
            sorted_word = ''.join(sorted(word))
            
            # Check if the sorted word is already a key in the dictionary
            if sorted_word not in anagrams:
                # If not, create a new key-value pair with the sorted word as key and a list containing the word as value
                anagrams[sorted_word] = [word]
            else:
                # If the sorted word is already a key, append the word to the list associated with that key
                anagrams[sorted_word].append(word)
        
        # Convert the values of the dictionary into a list of lists to get the final result
        result = list(anagrams.values())
        
        return result
