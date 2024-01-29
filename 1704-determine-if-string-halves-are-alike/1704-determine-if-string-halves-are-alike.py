class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        firstHalf = s[0:len(s)//2]
        secondHalf = s[len(s)//2:len(s)]
        vowels = ['a','e','i','o','u']
        firstHalfCount, secondHalfCount = 0,0
        for index,value in enumerate(firstHalf):
            firstHalfCount += 1 if value.lower() in vowels else 0
        for index,value in enumerate(secondHalf):
            secondHalfCount += 1 if value.lower() in vowels else 0
        return 1 if firstHalfCount == secondHalfCount else 0
