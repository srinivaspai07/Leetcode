class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.lstrip()
        specialSymbols = [' ', '.']
        result = 0
        firstDigit = 0
        setSign = 0
        sign = 1

        for str in s:

            if str == ".":
                break                
            if str == "-" or str == "+":

                if setSign:
                    break
                
                setSign = 1
                
                if str == "-":
                    
                    sign = -1
                continue
            if not str.isdigit():
                break

            setSign = 1
            result = result * 10 + int(str)
        
        result *= sign

        if result > 2**31 - 1:
            return  2**31 - 1
        elif result < -2**31:
            return -2**31
        else:
            return result
        