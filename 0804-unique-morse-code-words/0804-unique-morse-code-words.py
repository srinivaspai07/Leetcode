class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        character_list = list(string.ascii_lowercase)
        code_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_code = dict(zip(character_list,code_list))
        unique_code_set = set()
        for word in words:
            code = ""
            for char in word:
                code += morse_code.get(char)
            unique_code_set.add(code)
        return(len(unique_code_set))