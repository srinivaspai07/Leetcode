class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ballCount = dict()
        ballNum = [lowLimit,highLimit]
        for num in range(lowLimit,highLimit+1,1):
            digits = list(map(int, str(abs(num))))
            ballCount[(sum(digits))] = ballCount.get(sum(digits) , 0) +1
        max_value = max(ballCount.values())
        return max_value